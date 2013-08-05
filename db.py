from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://timforum:password@localhost/timforum', pool_recycle=3600)
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.__table_args__ = {'mysql_engine': 'InnoDB'}
