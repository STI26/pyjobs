FROM node:lts-alpine3.12
# FROM node:latest
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build
