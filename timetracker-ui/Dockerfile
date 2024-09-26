FROM node:18-alpine
WORKDIR /ui/

COPY package.json .
RUN npm install

COPY public/ public
COPY src/ src
COPY eslint.config.js .
COPY index.html .
COPY vite.config.js .

CMD ["npm", "run", "dev"]
