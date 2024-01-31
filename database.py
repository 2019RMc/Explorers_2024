from sqlalchemy import create_engine, text
from decouple import config

DATABASE_HOST= config('DATABASE_HOST')
DATABASE_USERNAME= config('DATABASE_USERNAME')
DATABASE_PASSWORD= config('DATABASE_PASSWORD')
DATABASE= config('DATABASE')

db_connection_string = "mysql+pymysql://" + DATABASE_USERNAME + ":" + DATABASE_PASSWORD + "@" + DATABASE_HOST + "/" + DATABASE + "?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  jobs = []
  print(result.all())
  print(type(result.all()))

