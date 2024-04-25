from pymongo import MongoClient

# MongoDB 인스턴스에 연결
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://username:password@localhost:27017/')

# 데이터베이스 선택 (없으면 자동 생성)
db = client['example_db']

# 콜렉션 선택 (없으면 자동 생성)
collection = db['example_collection']

# 새 문서 삽입
example_document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(example_document)