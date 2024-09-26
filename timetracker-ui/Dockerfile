FROM node:18-alpine
WORKDIR /ui/
COPY public/ /ui/public
COPY src/ /ui/src
COPY eslint.config.js /ui/
COPY index.html /ui/
COPY package.json /ui/
COPY vite.config.js /ui/

RUN npm install
CMD ["npm", "start"]