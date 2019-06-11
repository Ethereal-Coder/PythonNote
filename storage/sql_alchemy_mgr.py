# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-5-5
Description:
"""

from sqlalchemy import Column, create_engine, BIGINT, VARCHAR, INT, DATETIME, BINARY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time


Base = declarative_base()


class TbCategory(Base):
    __tablename__ = 'AT_D_CATEGORY'
    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR, nullable=True)
    pid = Column(BIGINT, nullable=True)
    lev = Column(INT, nullable=True)
    keyword = Column(VARCHAR, nullable=True)
    create_by = Column(VARCHAR, default='system')
    creation_date = Column(DATETIME, nullable=True)
    last_updated_by = Column(VARCHAR, default='system')
    last_updated_date = Column(DATETIME, nullable=True)
    delete_flag = Column(BINARY, nullable=True)
    full_path = Column(VARCHAR, nullable=True)
    child_ids = Column(VARCHAR, nullable=True)
    tree_path = Column(VARCHAR, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    Base.to_dict = to_dict


class AppCategory(Base):
    __tablename__ = 'AT_D_CATEGORY_DISPLAY'
    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR, nullable=True)
    ids = Column(VARCHAR, nullable=True)
    include_words = Column(VARCHAR, nullable=True)
    exclude_words = Column(VARCHAR, nullable=True)
    pid = Column(BIGINT, nullable=True)
    lev = Column(INT, nullable=True)
    orders = Column(INT, default=1)
    image = Column(VARCHAR, nullable=True)
    create_by = Column(VARCHAR, default='system')
    creation_date = Column(DATETIME, nullable=True)
    last_updated_by = Column(VARCHAR, default='system')
    last_updated_date = Column(DATETIME, nullable=True)
    delete_flag = Column(BINARY, default=0)
    is_home = Column(BINARY, nullable=True)
    tree_path = Column(VARCHAR, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    Base.to_dict = to_dict


DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = 'db_pwd'
DB_NAME = 'db_name'

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME), encoding='utf-8', echo=False, pool_size=100,
                       pool_recycle=10)
DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    tb_category = TbCategory()
    tb_category.id = 12
    tb_category.name = 'test'
    tb_category.creation_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    tb_category.last_updated_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    session.add(tb_category)
    session.commit()
    session.close()
