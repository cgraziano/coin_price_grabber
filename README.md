##Coin Price Grabber
Allows one to ping coinmarketcap.com to retrieve current 
coin prices by the coin's symbol.

An empty string will be returned if an empty string is found.

#Build
docker build -t coin_price_grabber:latest coin_price_grabber

#Run
docker run -t coin_price_grabber:latest ./key.txt

#Running Docker on Windows Home OS 
-Double-click on 'Docker Quickstart Terminal' (downloaded with docker toolkit)
-Open up Oracle VM VirtualBox Manager and start the 'default' container

#Running docker-compose (more for experimentation and not used to run this application)
-cd into the root directory of the code
-run 'docker-compose up' to start the service

