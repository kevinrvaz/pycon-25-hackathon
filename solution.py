"""
Pseudo Algorithm:-

1. Load the dataset from a JSON file.
2. Initialize the Google Generative AI Embeddings model.
3. Generate embeddings for each entry in the dataset.
4. Store embeddings of agent skills along with metadata of agent id in a vector store.
5. iterate through the dataset and perform similarity search for a ticket description and title combination with the created vector store
6. after vector search we can get a unique list of agent ids
7. in round robin fashion assign the ticket to the agents
8. return the final json with ticket id and assigned agent ids

"""


from langchain_google_genai import GoogleGenerativeAIEmbeddings
import json

with open("dataset.json", "r") as f:
    data = json.load(f)



