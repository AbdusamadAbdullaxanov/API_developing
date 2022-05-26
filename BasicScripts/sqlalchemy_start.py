from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
try:
    from . import config
except:
    import config as conf
BASICCONNECTION = f'postgresql://{conf.settings.user}:{conf.settings.password}@{conf.settings.host}/{conf.settings.database}'
engine = create_engine(BASICCONNECTION)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=True)
start = declarative_base()
