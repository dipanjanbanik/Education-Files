from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch("http://localhost:9200")

# DOCS = {
#     1: {
#         "title": "All Along The Watchtower",
#         "content": "There must be some way out of here Said the joker to the thief \
#         There's too much confusion I can't get no relief",
#     },
#     2: {
#         "title": "Land of Confusion",
#         "content": "There's too many men, too many people Making too many problems \
#         And not much love to go round Can't you see this is a land of confusion?",
#     },
#     3: {
#         "title": "Nowhere Near",
#         "content": "How easy I forget Just how you add to my confusion So I'm out of here \
#         Cause I know I'm nowhere near What you want, What you want, What your lookin for",
#     },
# }

# query = {"match_phrase": {"content": "too much confusion"}}

# res = es.search(index="test-index", body={"query": query})

docu1 = {
    "title": "All Along The Watchtower",
    "content": "There must be some way out of here Said the joker to the thief \
        There's too much confusion I can't get no relief",
}

docu2 = {
    "title": "Land of Confusion",
    "content": "There's too many men, too many people Making too many problems \
        And not much love to go round Can't you see this is a land of confusion?",
}

docu3 = {
    "title": "Nowhere Near",
    "content": "How easy I forget Just how you add to my confusion So I'm out of here \
        Cause I know I'm nowhere near What you want, What you want, What your lookin for",
}
es.delete(index="test-index", id=1)
es.delete(index="test-index", id=2)
es.delete(index="test-index", id=3)
resp = es.index(index="test-index", id=1, document=docu1)
resp = es.index(index="test-index", id=2, document=docu2)
resp = es.index(index="test-index", id=3, document=docu3)
query = {"match_phrase": {"content": "too much confusion"}}
res = es.search(index="test-index", body={"query": query})
for hit in res["hits"]["hits"]:
    print("%(title)s" % hit["_source"])
# print(resp["result"])
tv = es.termvectors(index="test-index", id=3, fields="content", term_statistics=True)
pprint(tv["term_vectors"]["content"]["field_statistics"])
