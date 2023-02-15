from elasticsearch import Elasticsearch
from pprint import pprint

from numpy import indices

es = Elasticsearch()
es.info()
index = es.indices.get_alias("*")

for x in index:
    print(x)
# pprint(es.info())
