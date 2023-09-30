from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DBConection:
    def __init__(self):
        self.connection_string = 'mysql+pymysql://root:123456@mysqldb/teste'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
