import config
import atexit
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(config.PG_DSN)
Base = declarative_base(engine)


class UserModel(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class AdvertModel(Base):

    __tablename__ = "adverts"

    advert_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_time = Column(DateTime, server_default=func.now())
    author = Column(String, ForeignKey("users.email", ondelete="CASCADE"))


Base.metadata.create_all()
Session = sessionmaker(engine)
atexit.register(lambda: engine.dispose())