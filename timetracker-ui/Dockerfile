FROM node:18-alpine
WORKDIR /ui/

COPY package.json .
RUN npm install
RUN npm i react-router-dom

COPY public/ public
COPY src/ src
COPY eslint.config.js .
COPY index.html .
COPY vite.config.js .

EXPOSE 8090

CMD ["npm", "run", "dev"]
