FROM node:22-alpine
ENV NODE_ENV=production PORT=8080
WORKDIR /app
COPY --chown=10001:10001 server.mjs ./server.mjs
USER 10001:10001
EXPOSE 8080
CMD ["node", "server.mjs"]
