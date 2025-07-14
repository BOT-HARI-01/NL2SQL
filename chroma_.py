import chromadb

chroma_client = chromadb.PersistentClient(path="./vector_storage")
collection = chroma_client.get_or_create_collection(name='my_new_collection')

collection.add(
    ids=["id1", "id2"],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ]
)
results = collection.query(
    query_texts=["This is a query document about hawaii"], 
    n_results=2
)
print(results)
