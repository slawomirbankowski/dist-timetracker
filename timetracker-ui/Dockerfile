FROM node:18-alpine
WORKDIR /ui/

RUN apt-get update && \
    apt-get install -y curl

COPY package.json .
RUN npm install

COPY public/ public
COPY src/ src
COPY eslint.config.js .
COPY index.html .
COPY vite.config.js .

EXPOSE 8090

CMD ["npm", "run", "dev"]
