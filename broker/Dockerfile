FROM node:14
RUN npm install -g nodemon
RUN npm install express
RUN npm install socket.io
RUN npm install got
# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

EXPOSE 8000
CMD [ "node", "server.js" ]
