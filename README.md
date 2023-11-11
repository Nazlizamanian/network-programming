# Network programming
Lab assigmenets completed in the course Network Programming course code TNPK18 using python.

## Smaller labs 1-4
- ###  Lab 2
This lab assignment involves creating a script to extract and analyze data from a file named "score2.txt." The script calculates and identifies the top scorers, displaying their names and respective scores. It's an exercise in data processing and analysis. 

- ### Lab 3
This program simulates a card game with three classes: CardClass representing individual playing cards, CardDeck for managing a deck of cards, and CardGame for playing the game. It creates and shuffles a deck of cards, then draws and displays cards with their values.

- ### Lab 4 
Implemented a function called fibbonacci(limit) that employs the 'yield' keyword to produce Fibonacci numbers. It calculates Fibonacci numbers until the value reaches or exceeds the specified limit. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.


## Using network connections lab 5-12
## Lab 5 
### Description
A basic program that enables two users to engage in a simplified Rock, Paper and Scissors game through a network connection. One user can act as the server, while the other can be the client. The server is first intalized in order for the client to make a connection. Then they take turns making moves and determine the winner based on the game's rules. The game continues until one player accumulates 10 points, and the overall winner is declared.

## Lab 6 
### Description 
This program creates a basic HTTP server. It listens on a port and responds to incoming HTTP requests with a simple HTML page that displays the client's response. 

## Lab 7 
### Description 
A program that essentially sets up a basic chat server where multiple clients can connect and exchange messages in a chat room. The server acts as an intermediary that forwards messages from one client to all other connected clients. It uses non-blocking sockets to handle multiple clients simultaneously, and the communication is in plain text format.

## Lab 11 
### Description 
Establishes a connection to an SQLite database and creates two tables, 'persons' and 'scores'. It then reads data from the file ('score2.txt') and populates the tables with the parsed information, and performs two SQL queries. The first query retrieves the top 10 persons with the highest total points, while the second one identifies the 10 most difficult tasks based on minimal total points. The script also includes functions to print the contents of the 'persons' and 'scores' tables, as well as the results of the SQL queries.
