FROM node:latest

WORKDIR /app

COPY package*.json /app

# No to need to download all nodemodules  
RUN npm init -y
RUN npm i fs

COPY . /app

RUN cd /app/backend && npm init -y
RUN cd /app/backend && npm install --save express

ENV PORT=8080

EXPOSE 8080

CMD ["npm", "start"]
