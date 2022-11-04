## install Express

cd backend
# Make sure you have node installed
npm init -y
npm install express
# run application
node server.js

# build docker image i current directory
docker build -t ctf/demo .

# run image with port forwarding
## go to localhost 8000
docker run -p 8000:8080 ctf/demo

-- burde fikse slik at jeg ikke kopierer
-- over node_modules