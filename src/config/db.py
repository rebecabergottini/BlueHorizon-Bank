from sqlalchemy import create_engine, MetaData
import os

# Acceder a las variables de entorno
db_host = os.getenv("MYSQL_HOST")
db_user = os.getenv("MYSQL_ROOT_USER")
db_password = os.getenv("MYSQL_ROOT_PASSWORD")
db_name = os.getenv("MYSQL_NAME")

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}")

meta = MetaData()

conn = engine.connect()