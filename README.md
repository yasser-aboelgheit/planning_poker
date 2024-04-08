# Scrum Poker Estimation
Scrum Poker Estimation service based on Django framework

## Technologies

* Django Framework: Framework based on python used to create APIs 
* Docker: containerization
* SQLite3: Database
* Websocket: two-way communication channels over a single Transmission Control Protocol (TCP)


## Flow

* A user creates a poll by entering ticket title and rating scheme
* Any user with the poll created URL can vote
* Opening the poll URL you are requested to enter your username
* Then you can vote
* Votes remain hidden until show votes is clicked


## Installation

after cloning the project
use `docker-compose build`
then `docker-compose up`
