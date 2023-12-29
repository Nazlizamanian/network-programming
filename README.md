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
## Lab 5 Rock Paper and Scissors game using socket
### Description
A basic program that enables two users to engage in a simplified Rock, Paper and Scissors game through a network connection. One user can act as the server, while the other can be the client. The server is first intalized in order for the client to make a connection. Then they take turns making moves and determine the winner based on the game's rules. The game continues until one player accumulates 10 points, and the overall winner is declared.

## Lab 6 
### Description 
This program creates a basic HTTP server. It listens on a port and responds to incoming HTTP requests with a simple HTML page that displays the client's response. 

## Lab 7  and Lab 8 Basic chat server 
### Description 
This program establishes a fundamental chat server allowing numerous clients to connect and share messages within a designated chat room. Serving as an intermediary, the server efficiently forwards messages from one client to all others. It employs non-blocking sockets to manage multiple clients simultaneously, enhancing scalability. Notably, the communication occurs in plain text format. This application supports concurrent connections from multiple clients, fostering a seamless exchange of messages within a straightforward chat environment. The server optimizes resource utilization through the use of the 'select' function, eliminating the necessity for separate threads or processes. Lab 7 assignment consisted of establishing a server and lab 8 consisted of the client code with an elegant GUI.

## Lab 9 Data Compression 
### Description 
Calculating the entrophy and compressing data shuffeld and unshuffled to measure the differences using zlib algorthims and the efficency. A higher entropy suggests more unpredictability and less redundancy, whereas lower entropy implies patterns and more predictability. Shuffled data typically lacks patterns or redundancy, making it less compressible, while unshuffled data may have repeating patterns, potentially resulting in better compression. Analyzing the compression ratios and sizes of compressed data.

## Lab 10 Valid email and Simpsons tv tabla regular expressions
### Description 
#### Task 1 & 2
Defines a function, is_valid_email(email), which utilizes a regular expression to check if a given email address adheres to a common format. The function prints whether each tested email address is valid or not based on the specified pattern, highlighting its conformance to typical email address structure.
#### Task 3
Uses a regular expression (regex_pattern) to extract information about each the TV show Simpsons from a html file, such as the time, season, episode, and a brief description of the show. The program then iterates through the matches found in the HTML code and prints the extracted details for each TV show in a structured format.

## Lab 11 Creating a database from a text file
### Description 
Establishes a connection to an SQLite database and creates two tables, 'persons' and 'scores'. It then reads data from the file ('score2.txt') and populates the tables with the parsed information, and performs two SQL queries. The first query retrieves the top 10 persons with the highest total points, while the second one identifies the 10 most difficult tasks based on minimal total points. The script also includes functions to print the contents of the 'persons' and 'scores' tables, as well as the results of the SQL queries.

## Lab 12 GUI chat using Push Technology to Firebase database
### Description 
Created a GUI chat client utilizing Firebase Realtime Database, subscribing to the database upon startup to receive the entire chat history in a single push from the server. Messages are displayed dynamically, with any subsequent database updates triggering real-time updates on the GUI. Sending a message involves adding an entry to the database, creating a seamless and synchronized chat experience.
