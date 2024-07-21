FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@7.24.0
RUN apk add --update python3 make g++ && rm -rf /var/cache/apk/*
RUN npm install
COPY . ./
RUN npm run build

# Use a smaller, more efficient image for serving static files
FROM node:16-alpine as production
WORKDIR /app
COPY --from=build /app/build /app/build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]


