-- LEARN private analytics schema. No raw replies, sessions or students.
CREATE TABLE IF NOT EXISTS learn_quest_daily (
 day DATE NOT NULL DEFAULT CURRENT_DATE, topic_id VARCHAR(32) NOT NULL,
 language VARCHAR(2) NOT NULL CHECK(language IN ('en','ro')),
 question_slot SMALLINT NOT NULL CHECK(question_slot BETWEEN 1 AND 3),
 variant VARCHAR(20) NOT NULL DEFAULT 'original', attempts INTEGER NOT NULL DEFAULT 0 CHECK(attempts>=0),
 correct INTEGER NOT NULL DEFAULT 0 CHECK(correct>=0),
 confused_term INTEGER NOT NULL DEFAULT 0, confused_example INTEGER NOT NULL DEFAULT 0,
 confused_diagram INTEGER NOT NULL DEFAULT 0, confused_too_fast INTEGER NOT NULL DEFAULT 0,
 PRIMARY KEY(day,topic_id,language,question_slot,variant),CHECK(correct<=attempts)
);
CREATE TABLE IF NOT EXISTS learn_quest_request_cap (day DATE PRIMARY KEY, accepted INTEGER NOT NULL DEFAULT 0 CHECK(accepted>=0));
CREATE TABLE IF NOT EXISTS learn_quest_topic_cap (day DATE NOT NULL, topic_id VARCHAR(32) NOT NULL, accepted INTEGER NOT NULL DEFAULT 0 CHECK(accepted>=0), PRIMARY KEY(day,topic_id));
CREATE TABLE IF NOT EXISTS learn_chokepoints(topic_id VARCHAR(32) NOT NULL,language VARCHAR(2) NOT NULL,question_slot SMALLINT NOT NULL,sample_size INTEGER NOT NULL,failure_rate NUMERIC(6,4) NOT NULL,severity VARCHAR(10) NOT NULL,diagnosis TEXT NOT NULL,created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),PRIMARY KEY(topic_id,language,question_slot));

CREATE OR REPLACE FUNCTION public.learn_record_quest(p_topic text, p_lang text, p_c1 boolean, p_c2 boolean, p_c3 boolean, p_confusion text, p_variant text DEFAULT 'original'::text)
 RETURNS text
 LANGUAGE plpgsql
AS $function$
DECLARE v_total INTEGER; v_topic INTEGER; v_flag TEXT;
BEGIN
IF p_topic !~ '^(fund|ai|dc|front|invis|lang|data)-[0-9]{2}$'
  OR p_lang NOT IN ('en','ro') OR p_confusion NOT IN ('term','example','diagram','too_fast','other','none','not_selected')
  OR p_variant NOT IN ('original') OR p_c1 IS NULL OR p_c2 IS NULL OR p_c3 IS NULL
  THEN RETURN 'invalid'; END IF;
INSERT INTO learn_quest_request_cap(day,accepted) VALUES(CURRENT_DATE,1)
ON CONFLICT(day) DO UPDATE SET accepted=learn_quest_request_cap.accepted+1
WHERE learn_quest_request_cap.accepted < 5000 RETURNING accepted INTO v_total;
IF v_total IS NULL THEN RETURN 'quota'; END IF;
INSERT INTO learn_quest_topic_cap(day,topic_id,accepted) VALUES(CURRENT_DATE,p_topic,1)
ON CONFLICT(day,topic_id) DO UPDATE SET accepted=learn_quest_topic_cap.accepted+1
WHERE learn_quest_topic_cap.accepted < 300 RETURNING accepted INTO v_topic;
IF v_topic IS NULL THEN RETURN 'topic_quota'; END IF;
FOR i IN 1..3 LOOP
  v_flag := CASE WHEN i=3 THEN p_confusion ELSE 'not_selected' END;
  INSERT INTO learn_quest_daily(day,topic_id,language,question_slot,variant,attempts,correct,confused_term,confused_example,confused_diagram,confused_too_fast)
  VALUES(CURRENT_DATE,p_topic,p_lang,i,p_variant,1,
  CASE i WHEN 1 THEN p_c1::INTEGER WHEN 2 THEN p_c2::INTEGER ELSE p_c3::INTEGER END,
  (v_flag='term')::INTEGER,(v_flag='example')::INTEGER,(v_flag='diagram')::INTEGER,(v_flag='too_fast')::INTEGER)
  ON CONFLICT(day,topic_id,language,question_slot,variant)
  DO UPDATE SET attempts=learn_quest_daily.attempts+1,
    correct=learn_quest_daily.correct+EXCLUDED.correct,
    confused_term=learn_quest_daily.confused_term+EXCLUDED.confused_term,
    confused_example=learn_quest_daily.confused_example+EXCLUDED.confused_example,
    confused_diagram=learn_quest_daily.confused_diagram+EXCLUDED.confused_diagram,
    confused_too_fast=learn_quest_daily.confused_too_fast+EXCLUDED.confused_too_fast;
END LOOP;
RETURN 'accepted';
END $function$


CREATE OR REPLACE VIEW learn_quest_diagnostics AS
 SELECT topic_id,
    language,
    question_slot,
    sum(attempts)::integer AS attempts,
    sum(correct)::integer AS correct,
    round(1::numeric - sum(correct)::numeric / NULLIF(sum(attempts), 0)::numeric, 4) AS failure_rate,
        CASE
            WHEN sum(attempts) < 30 THEN 'INSUFFICIENT'::text
            WHEN (1::numeric - sum(correct)::numeric / NULLIF(sum(attempts), 0)::numeric) >= 0.50 THEN 'CRITICAL'::text
            WHEN (1::numeric - sum(correct)::numeric / NULLIF(sum(attempts), 0)::numeric) >= 0.30 THEN 'REVIEW'::text
            ELSE 'OK'::text
        END AS priority,
    sum(confused_term)::integer AS term_flags,
    sum(confused_example)::integer AS example_flags,
    sum(confused_diagram)::integer AS diagram_flags,
    sum(confused_too_fast)::integer AS pacing_flags
   FROM learn_quest_daily
  WHERE day >= (CURRENT_DATE - 27)
  GROUP BY topic_id, language, question_slot;;

CREATE OR REPLACE VIEW learn_revision_candidates AS
 SELECT topic_id,
    language,
    question_slot,
    attempts,
    correct,
    failure_rate,
    priority,
    attempts - correct AS missed_answers,
        CASE
            WHEN priority = 'INSUFFICIENT'::text THEN 'Collect more opt-in evidence; do not change the lesson.'::text
            WHEN question_slot = 2 OR term_flags > example_flags AND term_flags > diagram_flags THEN 'Check first-use and prerequisite term definitions; verify the question is unambiguous.'::text
            WHEN question_slot = 3 THEN 'Test whether the analogy creates a misconception; review both distractors and limits of the metaphor.'::text
            WHEN diagram_flags > example_flags THEN 'Simplify arrows, labels, ordering, and diagram legend; re-test with a beginner.'::text
            ELSE 'Rewrite the first concrete example; test the concept and the question with a novice.'::text
        END AS suggested_revision,
        CASE
            WHEN priority = 'INSUFFICIENT'::text THEN 'NO_ACTION'::text
            WHEN priority = ANY (ARRAY['REVIEW'::text, 'CRITICAL'::text]) THEN 'HUMAN_REVIEW_REQUIRED'::text
            ELSE 'MONITOR'::text
        END AS revision_gate
   FROM learn_quest_diagnostics
  ORDER BY (attempts - correct) DESC;;
