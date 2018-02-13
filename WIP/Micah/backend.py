from pymongo import MongoClient

client = MongoClient("""mongodb://admin:yhpFdVW1FF51P7qd@cluster0-shard-00-00-o8mtx.mongodb.net:27017,cluster0-shard-00-01-o8mtx.mongodb.net:27017,cluster0-shard-00-02-o8mtx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin""")

db = client['ncjw-rs']
