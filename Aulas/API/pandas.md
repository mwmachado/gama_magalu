# Mysql

pymysql, mysql.connect
SQL Alchemy
- connection string
pandas
  - read_sql_table("tabela", con)
    - columns
    - index_col
  - read_sql_query("query", con)
    - index_col
    - param = ["param1"]
    - param = `{
      "named_param1":"value",
      "named_param1":"value"
      }`
  - to_sql("tabela", con)
    - index, index_label
    - if_exists
mysql -> pandas -> csv
csv -> pandas -> mysql

# MongoDB

from pymongo import MongoClient
mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
conn = MongoClient(mongo_uri)
db = conn[database]
cursor = db[colecao]
docs = cursor.find(query)
df = pd.DataFrame(list(docs))
json -> pandas -> mongo
mongo -> pandas -> json