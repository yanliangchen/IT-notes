import pymongo
class MongodbConn(object):
    def __init__(self):
        self.CONN = pymongo.MongoClient("163.53.91.155",27017)
    def run(self):
        database = "mydb"
        db = self.CONN[database]
        col = db.collection_names()
        col = col[0]
        collection = db.get_collection(col)
        documents = collection.find()
        with open('F:/test.txt', 'w') as f:
            for i in documents:
                f.write(str(i) + '\n')
            f.close()
if __name__ == '__main__':
    mongo_obj = MongodbConn()
    mongo_obj.run()