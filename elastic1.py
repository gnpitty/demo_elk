from elasticsearch import Elasticsearch
import os

elastic_key = os.environ.get("ELASTIC_API_KEY")
host=os.environ.get("ELASTIC_HOST")

es = Elasticsearch( f"https://{host}:9200/", api_key=elastic_key,verify_certs=None)

# API key should have cluster monitor rights
print(es.info())

# Crea el indice


index_nombre = "demo2025a"
if not es.indices.exists(index=index_nombre):
    # Create the index
    es.indices.create(
        index=index_nombre,
        body={
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "nombre": {"type": "text"},
                    "edad": {"type": "integer"},
                    "identificacion":{"type": "text"},
                    "celular":{"type": "text"}
                }
            }
        }
    )
    print(f"Index '{index_nombre}' created.")
else:
    print(f"Index '{index_nombre}' already exists.")


# datos para cargar en el indice
documentos  = [
    {"nombre": "Alice", "edad": 30, "identificacion": "8-322-2988", "celular": 6554433},
    {"nombre": "Bob", "edad": 25, "identificacion": "9-102-2099", "celular": 66778990},
    {"nombre": "Charlie", "edad": 35, "identificacion": "4-039-2999", "celular": 66325522},
]

# cargando los documentos al indice
for i, doc in enumerate(documentos):
    print(i,doc,type(doc))
    response = es.index(index=index_nombre, document=doc)
    print(f"Document {i + 1} inserted: {response['result']}")


response = es.search(index=index_nombre, body={"query": {"match_all": {}}})
print("Documents in index:")
for doc in response['hits']['hits']:
    print(doc["_source"])