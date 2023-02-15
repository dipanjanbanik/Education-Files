import os
import re
from typing import Any, List
from collections import Counter
import ir_datasets
import nltk
import requests
from sqlitedict import SqliteDict

nltk.download("stopwords")
STOPWORDS = set(nltk.corpus.stopwords.words("english"))


def download_dataset(filename: str, force: bool = False) -> None:
    """Download a dataset to be used with ir_datasets.

    Args:
        filename: Name of the file to download.
        force (optional): Downloads a file and overwrites if already exists.
            Defaults to False.
    """
    filepath = os.path.expanduser(f"~/.ir_datasets/wapo/{filename}")
    if force or not os.path.isfile(filepath):
        print("File downloading...")
        response = requests.get(f"https://gustav1.ux.uis.no/dat640/{filename}")
        if response.ok:
            print("File downloaded; saving to file...")
        with open(filepath, "wb") as f:
            f.write(response.content)

    print("First document:\n")
    # print(next(ir_datasets.load("wapo/v2/trec-core-2018").docs_iter()))


def preprocess(doc: str) -> List[str]:
    """Preprocesses a string of text.

    Arguments:
        doc: A string of text.

    Returns:
        List of strings.
    """
    return [
        term
        for term in re.sub(r"[^\w]|_", " ", doc).lower().split()
        if term not in STOPWORDS
    ]


class InvertedIndex(SqliteDict):
    def __init__(
        self,
        filename: str = "inverted_index.sqlite",
        fields: List[str] = ["title", "body"],
        new: bool = False,
    ) -> None:
        super().__init__(filename, flag="n" if new else "c")
        self.fields = fields
        self.index = {} if new else self

    # TODO
    ...

    def add_posting(
        self, typeof: str, term: str, doc_id: int, payload: Any = None
    ) -> None:
        # # append new posting to the posting list
        if typeof in self.index:
            if term in self.index[typeof]:
                self.index[typeof][term].update({doc_id: payload})
            else:
                self.index[typeof][term] = {doc_id: payload}
        else:
            self.index[typeof] = {}
            self.index[typeof][term] = {doc_id: payload}

    # def add_posting(
    #     self, typeof: str, term: str, doc_id: int, payload: Any = None
    # ) -> None:
    #     # # append new posting to the posting list
    #     if typeof in self.index:
    #         if term in self.index[typeof]:
    #             self.index[typeof][term].update({doc_id: payload})
    #         else:
    #             self.index[typeof][term] = {doc_id: payload}
    #     else:
    #         self.index[typeof] = {}
    #         self.index[typeof][term] = {doc_id: payload}

    def get_postings(self, field: str, term: str) -> List[Any]:
        """Fetches the posting list for a given field and term.

        Args:
            field: Field for which to get postings.
            term: Term for which to get postings.

        Returns:
            List of postings for the given term in the given field.
        """
        # TODO
        ...
        if field in self.index and term in self.index[field]:

            return self.index[field][term].items()  ## converts to list
        else:
            return 0

    def get_term_frequency(self, field: str, term: str, doc_id: str) -> int:
        """Return the frequency of a given term in a document.

        Args:
            field: Index field.
            term: Term for which to find the count.
            doc_id: Document ID

        Returns:
            Term count in a document.
        """
        # TODO
        ...
        # if (
        #     field in self.index
        #     and term in self.index[field]
        #     and doc_id in self.index[field][term]
        # ):
        #     return self.index[field][term][doc_id]
        if field in self.index:
            if term in self.index[field]:
                if doc_id in self.index[field][term]:
                    return self.index[field][term][doc_id]
                else:
                    return 0
        else:
            return 0

    def get_terms(self, field: str) -> List[str]:
        """Returns all unique terms in the index.

        Args:
            field: Field for which to return the terms.

        Returns:
            Set of all terms in a given field.
        """
        # TODO
        ...
        if field in self.index:
            return list(self.index[field].keys())
        else:
            return []

    def __exit__(self, *exc_info):
        if self.flag == "n":
            self.update(self.index)
            self.commit()
            print("Index updated.")
        super().__exit__(*exc_info)


def index_collection(
    collection: str = "wapo/v2/trec-core-2018",
    filename: str = "inverted_index.sqlite",
    num_documents: int = 595037,
) -> None:
    """Builds an inverted index from a document collection.

    Note: WashingtonPost collection has 595037 documents. This might take a very
        long time to index on an average computer.


    Args:
        collection: Collection from ir_datasets.
        filename: Sqlite filename to save index to.
        num_documents: Number of documents to index.
    """
    dataset = ir_datasets.load(collection)
    with InvertedIndex(filename, new=True) as index:
        for i, doc in enumerate(dataset.docs_iter()):
            if (i + 1) % (num_documents // 100) == 0:
                print(f"{round(100*(i/num_documents))}% indexed.")
            if i == num_documents:
                break

            # TODO
            ...
            # 0 = 'doc_id'
            # 1 = 'url'
            # 2 = 'title'
            # 3 = 'author'
            # 4 = 'published_date'
            # 5 = 'kicker'
            # 6 = 'body'
            # 7 = 'body_paras_html'
            # 8 = 'body_media'

            # doc_id                        b2e89334-33f9-11e1-825f-dabc29fd7071
            # url              https://www.washingtonpost.com/sports/colleges...
            # title            Danny Coale, Jarrett Boykin are a perfect 1-2 ...
            # author                                              Mark Giannotto
            # published_date                                       1325376562000
            # kicker                                                    Colleges
            # body             Virginia Tech wide receiver Danny Coale (19) w...
            # body_paras_html  (<span class="dateline">NEW ORLEANS —</span> W...
            # body_media       ((image, https://img.washingtonpost.com/rw/201...

            doc_id, title, body = doc[0], doc[2], doc[6]
            freqtitle = freqbody = dict()
            preprocessData = {"title": [], "body": []}
            preprocessDataCounter = {"title": Counter(), "body": Counter()}
            testList = {"doc_id": doc[0], "title": doc[2], "body": doc[6]}
            if testList["title"]:
                # preprocessData["title"] = preprocess(testList["title"])
                preprocessData.update({"title": preprocess(testList["title"])})
                # print(preprocessData["title"])
                freqtitle = Counter(preprocessData["title"])
                preprocessDataCounter.update({"title": freqtitle})
                # print(freqtitle)

            if testList["body"]:
                # preprocessData["body"] = preprocess(testList["body"])
                preprocessData.update({"body": preprocess(testList["body"])})
                freqbody = Counter(preprocessData["body"])
                preprocessDataCounter.update({"body": freqbody})

            # print(preprocessDataCounter["body"])
            testy = ["title", "body"]
            typeof = "body"

            for key in preprocessDataCounter:
                for term, freq in preprocessDataCounter[key].items():
                    # index.add_posting(typeof, term, doc_id, freq)
                    if key in index.index:
                        if term in index.index[key]:
                            index.index[key][term].update({testList["doc_id"]: freq})
                        else:
                            index.index[key][term] = {testList["doc_id"]: freq}
                    else:
                        index.index[key] = {}
                        index.index[key][term] = {testList["doc_id"]: freq}

            ######################################################################
            # typeof = "body"
            # for key in preprocessDataCounter:
            #     for term, freq in preprocessDataCounter[key].items():
            #         # index.add_posting(typeof, term, doc_id, freq)
            #         if typeof in index.index:
            #             if term in index.index[typeof]:
            #                 index.index[typeof][term].update({doc_id: freq})
            #             else:
            #                 index.index[typeof][term] = {doc_id: freq}
            #         else:
            #             index.index[typeof] = {}
            #             index.index[typeof][term] = {doc_id: freq}
            #########################################################################
            # typeof = "body"
            # for term, freq in (preprocessDataCounter["body"]).items():
            #     # index.add_posting(typeof, term, doc_id, freq)
            #     if typeof in index.index:
            #         if term in index.index[typeof]:
            #             index.index[typeof][term].update({doc_id: freq})
            #         else:
            #             index.index[typeof][term] = {doc_id: freq}
            #     else:
            #         index.index[typeof] = {}
            #         index.index[typeof][term] = {doc_id: freq}
            # typeof = "title"
            # for term, freq in (preprocessDataCounter["title"]).items():
            #     # index.add_posting(typeof, term, doc_id, freq)
            #     if typeof in index.index:
            #         if term in index.index[typeof]:
            #             index.index[typeof][term].update({doc_id: freq})
            #         else:
            #             index.index[typeof][term] = {doc_id: freq}
            #     else:
            #         index.index[typeof] = {}
            #         index.index[typeof][term] = {doc_id: freq}
            #######################################################################
            # for fields in list(preprocessData.keys()):
            #     for term, freq in freqbody.items():
            #         if fields in index.index:
            #             if term in index.index[fields]:
            #                 index.index[fields][term].update({doc_id: freq})
            #             else:
            #                 index.index[fields][term] = {doc_id: freq}
            #         else:
            #             index.index[fields] = {}
            #             index.index[fields][term] = {doc_id: freq}

            # typeof = "body"
            # for term, freq in freqbody.items():
            #     # index.add_posting(typeof, term, doc_id, freq)
            #     if typeof in index.index:
            #         if term in index.index[typeof]:
            #             index.index[typeof][term].update({doc_id: freq})
            #         else:
            #             index.index[typeof][term] = {doc_id: freq}
            #     else:
            #         index.index[typeof] = {}
            #         index.index[typeof][term] = {doc_id: freq}

            # typeof = "title"
            # for term, freq in freqtitle.items():
            #     # index.add_posting(typeof, term, doc_id, freq)
            #     if typeof in index.index:
            #         if term in index.index[typeof]:
            #             index.index[typeof][term].update({doc_id: freq})
            #         else:
            #             index.index[typeof][term] = {doc_id: freq}
            #     else:
            #         index.index[typeof] = {}
            #         index.index[typeof][term] = {doc_id: freq}
            ################################################################################
            # print(preprocessData["body"])
            # freqtitle, freqbody = {}, {}
            # doc_id = doc[0]
            # title = doc[2]
            # body = doc[6]
            # if title:
            #     pptitle = preprocess(title)
            #     # print(pptitle)
            #     freqtitle = Counter(pptitle)
            #     # print(freqtitle)

            # if body:
            #     ppbody = preprocess(body)
            #     freqbody = Counter(ppbody)
            # print(pptitle)
            # typeof = "title"
            # for term, freq in freqtitle.items():
            #     index.add_posting(typeof, term, doc_id, freq)

            # typeof = "body"
            # for term, freq in freqbody.items():
            #     index.add_posting(typeof, term, doc_id, freq)

            # print(freqbody)

            # print(freqtitle.items())
            # for term, freq in freqtitle.items():
            #     index.add_posting("title", term, doc_id, freq)
            # for term, freq in freqtitle.items():
            #     index.add_posting("body", term, doc_id, freq)


if __name__ == "__main__":
    download_dataset("WashingtonPost.v2.tar.gz")
    collection = "wapo/v2/trec-core-2018"
    index_file = "inverted_index.sqlite"

    # Comment out this line or delete the index file to re-index.
    # if not os.path.isfile(index_file):
    #     # There are total 595037 documents in the collection.
    #     # Consider using a smaller subset while developing the index because
    #     # indexing the entire collection might take a considerable amount of
    #     # time.
    #     index_collection(collection, index_file, 1000)

    if os.path.exists(index_file):
        os.remove(index_file)
    index_collection(collection, index_file, 1000)

    index = InvertedIndex(index_file)
    print(len(index.get_postings("body", "norway")))
    print(
        index.get_term_frequency("body", "norway", "ebff82c9cd96407d2ef1ba620313f011")
    )
    print(len(index.get_terms("title")))
    index.close()
