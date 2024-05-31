FROM node:20.13-slim
RUN npm install -g http-server
WORKDIR /client
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]

# FROM node:20.13-slim as build-stage
# WORKDIR /client
# COPY package*.json ./
# RUN npm install
# COPY ./ .
# RUN npm run build
#
# FROM nginx:stable-alpine
# RUN mkdir /client
# COPY --from=build-stage /client/dist /app
# COPY nginx.conf /etc/nginx/nginx.conf