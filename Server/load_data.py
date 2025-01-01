import os
import csv
import chromadb

# Set up constant variables
CHUNK_SIZE = 1000
CLIENT_DIRECTORY = os.getcwd() + "/jeopardy.sqlite3"
COLLECTION_NAME = "JeopardyCollection"
CSV_FILE_PATH = os.getcwd() + '/../csv/jeopardy_data_and_embeddings.csv' # Path to the csv file, this is not included in the repo, as it is part of a former version of the project

def main():
    client = chromadb.PersistentClient(CLIENT_DIRECTORY)
    client.reset() # Option to reset the database, must have 'ALLOW_RESET' set to True in environment
    collection = client.get_or_create_collection(COLLECTION_NAME)

    # Load documents and embeddings into the database in chunks of 40,000 or less (to account for limitations of the ChromaDB client)
    startpoint = 0
    for i in range(0, 1): # 216000 documents in total so a good number of chunks is 6 (chunks of 40000 documents each)
        load_into_db(collection, startpoint)
        startpoint += CHUNK_SIZE

# Load the documents into an array from the csv file, format the data, and load it into the database
def load_into_db(collection, startpoint):
    arr = csv_as_array(startpoint)

    documentsArray = [str(row[:7]) for row in arr]
    embeddingArray = [row[7:] for row in arr]
    idArray = []

    id = startpoint + 1
    for i in range(len(embeddingArray)):
        idArray.append(f'DocID{id}')
        id += 1

    for i, row in enumerate(embeddingArray):
        for j, element in enumerate(row):
            embeddingArray[i][j] = float(element)
            

    collection.add(
        documents = documentsArray,
        embeddings = embeddingArray,
        ids = documentsArray
    )
    
# Load the csv file into an double array, starting at the given startpoint and ending at the startpoint + CHUNK_SIZE
def csv_as_array(startpoint=0): 
    double_array = []

    with open(CSV_FILE_PATH, 'r') as file:
        csv_reader = csv.reader(file)
        for (i, row) in enumerate(csv_reader):
            if(i < startpoint):
                continue
            if(i > startpoint + CHUNK_SIZE):
                return double_array[1:]
            double_array.append(row)
    return double_array[1:]


if __name__ == "__main__":
    main()
