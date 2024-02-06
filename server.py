import os
import csv
import ast
import json
import openai 
import chromadb
import socketserver

import numpy as np
import pandas as pd

from colorama import Fore
from getpass import getpass
from urllib.parse import urlparse, parse_qs
from http.server import SimpleHTTPRequestHandler
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

# Set up constant variables
CLIENT_DIRECTORY = os.getcwd() + "/jeopardy.sqlite3"
COLLECTION_NAME = "JeopardyCollection"
PORT = 8080

# Set up the OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Initialize the database client and collection
client = chromadb.PersistentClient(CLIENT_DIRECTORY)
collection = client.get_or_create_collection(COLLECTION_NAME)

# HTTP request handler for the search endpoint
# More endpoints could be added but the project only handles search 
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/search'):
            print("Search query received")

            # Parse the search query from the URL
            search_message = self.path.split('=', 1)[-1].replace('%20', ' ')
            print(f'{Fore.GREEN}Search: {Fore.RESET}{search_message}')

            # Search the database for the query
            response = search(search_message)["documents"]

            # Format the response as a JSON object
            dict = {} 
            index = 0
            for x in response[0]:
                x = ast.literal_eval(x)

                sub_dict = {}
                sub_dict['Question'] = x[0]
                sub_dict['Answer'] = x[1]
                sub_dict['Category'] = x[2]
                sub_dict['Value'] = x[3]
                sub_dict['Round'] = x[4]
                sub_dict['Air_Date'] = x[5]
                sub_dict['Show_Number'] = x[6]

                dict[index] = sub_dict
                index += 1
            json_response = json.dumps(dict)

            # Send the response to the client
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Origin, Content-Type')
            self.end_headers()
            self.wfile.write(json_response.encode('utf-8'))
        else:
            super().do_GET()

# Function to search the database for a given query
def search(search_term): 
    results = collection.query(
            query_embeddings =  get_embedding(search_term, engine='text-embedding-ada-002'), #embeddingArray[0],
            n_results = 10,
    )
    return results

# Main function to start the server
def main(): 
    print(f'{Fore.GREEN}Starting server...{Fore.RESET}')
    print(f'{Fore.GREEN}Listening on port: {Fore.RESET}{PORT}')
    print(f'{Fore.GREEN}Collections in client: {Fore.RESET}{client.list_collections()}')
    print(f'{Fore.GREEN}Documents in collection {COLLECTION_NAME}: {Fore.RESET}{collection.count()}')

    try: 
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print("Serving at port", PORT)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server")
        httpd.server_close()
        exit()

if __name__ == "__main__":
    main() 




