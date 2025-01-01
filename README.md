## Jeopardy Questions Vector Embeddings Search Engine


## Description
This project is a search engine that utilizes vector embedding to efficiently search through a large database of Jeopardy questions. The system consists of several components including a Python server, a client-side JavaScript script, and various supporting files.

## Purpose
The purpose of this project is a demonstration of a similar product I made at Ross. The product used embedding on product descriptions to find product codes from natural language searches. It also provided several other usefull ways to sort through and find products. The product codes themselves were often misleading and unintuitive so before memorizing all the codes it could be difficult for new employees to find the correct ones, hence the usefullness of the project. That project was one of several AI based projects I created at Ross.

## Demo 
This linked video is a demonstration video of the engine searching all 216,000 data points (sorry for poor audio quality) https://www.youtube.com/watch?v=jvnt4cNDsCM

## Usage
1. Add your personal OpenAI API key to the server.py file
2. Run 'pip install -r requirments.py' an older version of python (>3.9) may be necessary, this can be acheived with a virtual environment and pyenv
3. Run the server.py file with the command 'python3 server.py' (this must be done first so that the server gets port 8080)
4. Run the server with the command 'http-server' or 'python3 -m http.server' depending on your setup
5. Open the address to the js server in your browser
6. Use the search feature!

## Files
- Server/server.py: The Python server acts as the backend for handling database queries and returning search results to the client. It interfaces with the ChromaDB vector database and handles incoming requests from the client.
- Client/client.js: The client-side JavaScript script is responsible for capturing user input, sending queries to the server, and displaying the results on the user interface. It communicates with the server asynchronously to provide a seamless search experience.
- Server/load_data.py: The database loader script (load_data.py) is used to preprocess and load the Jeopardy questions dataset into the ChromaDB vector database. It transforms the raw question data into vector embeddings using an embedding engine before storing them in the database. (You will likely not need to run this file at all)

## Notes
- You will need to add your own OpenAI API key
- Only 1000 data points are in the db in the repo for demonstration purposes, this is because the entire db is too large to upload

## Author
Josh Siderius
