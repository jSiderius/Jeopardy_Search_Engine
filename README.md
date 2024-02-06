## Jeopardy Questions Vector Embeddings Search Engine


## Description
This project is a Jeopardy questions search engine that utilizes vector embeddings to efficiently search through a large database of Jeopardy questions. The system consists of several components including a Python server, a client-side JavaScript script, and various supporting files.

## Usage
1. Add your personal OpenAI API key to the server.py file
2. Run the server.py file with the command 'python3 server.py' (this must be done first so that the server get port 8080)
3. Run the js with the command 'http-server'
4. Open the address to the js server in your browser
5. Use the search feature!

## Files
- server.py: The Python server acts as the backend for handling database queries and returning search results to the client. It interfaces with the ChromaDB vector database and handles incoming requests from the client.
- client.js: The client-side JavaScript script is responsible for capturing user input, sending queries to the server, and displaying the results on the user interface. It communicates with the server asynchronously to provide a seamless search experience.
- load_data.py: The database loader script (load_data.py) is used to preprocess and load the Jeopardy questions dataset into the ChromaDB vector database. It transforms the raw question data into vector embeddings using an embedding engine before storing them in the database. (You will likely not need to run this file at all)

## Notes
- You will need to add your own OpenAI API key
- Only 1000 data points are in the db in the repo for demonstration purposes, this is because the entire db is too large to upload
- The Demo.mkv file is a demo video of the engine searching all 216,000 data points (sorry for poor audio quality)

## Author
Josh Siderius
