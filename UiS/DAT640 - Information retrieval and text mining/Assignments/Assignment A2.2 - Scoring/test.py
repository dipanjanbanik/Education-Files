def abc():
    preprocessData = {"title": [], "body": []}
    preprocessDataCounter = {"title": ct(), "body": ct()}
            testList = {"doc_id": doc[1], "title": doc[2], "body": doc[3]}

            for field in preprocessDataCounter:
                if testList[field] != None:
                    preprocessData.update({field: preprocess(testList[field])})
                    preprocessDataCounter.update({field: ct(preprocessData[field])})

                for itemTerm, itemFrequency in preprocessDataCounter[field].items():
                    if field in index.index:
                        if itemTerm in index.index[field]:
                            index.index[field][itemTerm].update(
                                {testList["doc_id"]: itemFrequency}
                            )
                        else:
                            index.index[field][itemTerm] = {
                                testList["doc_id"]: itemFrequency
                            }
                    else:
                        index.index[field] = {}
                        index.index[field][itemTerm] = {
                            testList["doc_id"]: itemFrequency
                        }