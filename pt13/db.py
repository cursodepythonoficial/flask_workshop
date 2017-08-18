from tinymongo import TinyMongoClient

DATAFOLDER = '/tmp/flask_workshop_test'

conn = TinyMongoClient(DATAFOLDER)
db = conn.test
