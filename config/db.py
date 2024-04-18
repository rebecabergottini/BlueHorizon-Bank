from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:rbergottini@172.17.0.2:3306/storedb")

meta = MetaData()

conn = engine.connect()