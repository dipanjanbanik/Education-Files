from msilib.schema import File
import os
import re
from turtle import title
from typing import Any, List
import pandas as pd
import ir_datasets
import nltk
import requests
from sqlitedict import SqliteDict
import collections

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
    dataset = ir_datasets.load("wapo/v2/trec-core-2018")
    datasetFields = dataset.docs_cls()._fields

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

        # df = pd.DataFrame(self.dataset.docs_iter()[:1])
        # print(df.head(1).transpose())
        # print("\n\n\n\n")

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

        index["title1"] = {"name": "second name", "manu_id": "another name"}
        print(index["title1"]["name"].items())

    def get_terms(self, field: str) -> List[str]:
        """Returns all unique terms in the index.

        Args:
            field: Field for which to return the terms.

        Returns:
            Set of all terms in a given field.
        """
        # TODO
        ...

        # index["title1"] = {"name": "second name"}
        # index["title1"] = {"manu_id": "another name"}
        # print(index["title1"])

        # index["title1"] = {"name": "second name", "manu_id": "another name"}
        # index["title1"] = {
        #     "name": "second name",
        #     "manu_id": "another name",
        #     "ano_id": "ano name",
        # }
        # index["title1"] = {
        #     "name": "second name",
        #     "manu_id": "another name",
        #     "ano_id": "anoing name",
        # }
        # index["title2"] = {"id": 2}
        # try:
        #     print(index["title1"])
        # except:
        #     print("An exception occurred")
        # print((index["title2"]["id"]) + 1)
        testdict = {}
        # get field index position
        fieldIndexPosition = (self.dataset.docs_cls()._fields).index(field)
        # test1 = self.dataset.docs_iter()[0:1]
        # print(test1[0][2])
        k = self.dataset.docs_iter()[:20]
        i = 0
        for doc in k:
            try:
                preProcessedData = preprocess(doc[fieldIndexPosition])
                # print(preProcessedData)
                for eachWord in preProcessedData:
                    try:
                        # print(index[eachWord])
                        # if index[eachWord] == eachWord:
                        #     if index[eachWord] == "football":
                        #         print("paisi")
                        #     else:
                        #         print("pai nai")
                        value = int(index[eachWord][field]) + 1
                        # index[eachWord][field] = value

                        index[eachWord] = {
                            "doc_id": index["prince"]["doc_id"],
                            "url": index["prince"]["url"],
                            "title": value + 1,
                            "author": index["prince"]["author"],
                            "published_date": index["prince"]["published_date"],
                            "kicker": index["prince"]["kicker"],
                            "body": index["prince"]["body"],
                            "body_paras_html": index["prince"]["body_paras_html"],
                            "body_media": index["prince"]["body_media"],
                        }
                        # else:
                        # if eachWord in testdict:
                        #     testdict[eachWord] = testdict[eachWord] + 1
                        # else:
                        #     testdict[eachWord] = 1
                        # print()
                    except:
                        # for eachIndexFiled in self.dataset.docs_cls()._fields:
                        # print("except")
                        index[eachWord] = {
                            self.datasetFields[0]: "1",
                            self.datasetFields[1]: "1",
                            self.datasetFields[2]: "1",
                            self.datasetFields[3]: "1",
                            self.datasetFields[4]: "1",
                            self.datasetFields[5]: "1",
                            self.datasetFields[6]: "1",
                            self.datasetFields[7]: "1",
                            self.datasetFields[8]: "1",
                        }
                        # print(index[eachWord])
                        # index[eachWord] = {field: 1}
            except:
                continue
            # print("doc id ", i, preProcessedData)

            i += 1
        # print(index["danny"]["title"])

        index.commit()

        print(index["prince"])

        # return [0]

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


if __name__ == "__main__":
    download_dataset("WashingtonPost.v2.tar.gz")
    collection = "wapo/v2/trec-core-2018"
    index_file = "inverted_index.sqlite"

    # Comment out this line or delete the index file to re-index.
    if not os.path.isfile(index_file):
        # There are total 595037 documents in the collection.
        # Consider using a smaller subset while developing the index because
        # indexing the entire collection might take a considerable amount of
        # time.
        index_collection(collection, index_file, 1000)

    index = InvertedIndex(index_file)
    # print(len(index.get_postings("body", "norway")))
    print(
        index.get_term_frequency("body", "norway", "ebff82c9cd96407d2ef1ba620313f011")
    )
    # print(len(index.get_terms("title")))
    index.close()


# index['title'][word]={doc[0]:1}
# index.commit()
