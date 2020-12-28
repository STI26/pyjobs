ARG VUE_APP_BASEURL
FROM node:lts-alpine3.12
# FROM node:latest
ARG VUE_APP_BASEURL
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN echo VUE_APP_BASEURL=$VUE_APP_BASEURL > .env.production
RUN npm run build