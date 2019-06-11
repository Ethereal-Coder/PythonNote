# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

'''
mongodb server
/usr/bin/mongod --quiet --config /etc/mongod.conf
'''

from pymongo import MongoClient


class MongoAuthManager(object):
    def __init__(self, host, port, db, collection, name, pwd):
        client = MongoClient(host=host, port=port, connect=False)
        db_auth = client.admin
        db_auth.authenticate(name, pwd)
        self.collection = client[db][collection]


class MongoManager(object):
    def __init__(self, host, port, db, collection):
        client = MongoClient(host=host, port=port, connect=False)
        self.collection = client[db][collection]


tb_material = None
tb_cats = None
pdd_info = None
pdd_cats = None
sn_goods = None
jd_goods = None


def mongo_tb_material():
    global tb_material
    if tb_material is None:
        tb_material = MongoManager('localhost', 27017, 'ec', 'tb-material')
    return tb_material


def mongo_tb_cats():
    global tb_cats
    if tb_cats is None:
        tb_cats = MongoManager('localhost', 27017, 'ec', 'tb-cats')
    return tb_cats


def mongo_pdd_cats():
    global pdd_cats
    if pdd_cats is None:
        pdd_cats = MongoManager('localhost', 27017, 'ec', 'pdd_cats')
    return pdd_cats


def mongo_pdd_info():
    global pdd_info
    if pdd_info is None:
        pdd_info = MongoManager('localhost', 27017, 'PinDuoDuoInfo', 'PDDBrandsTypes')
    return pdd_info


def mongo_sn_goods():
    global sn_goods
    if sn_goods is None:
        sn_goods = MongoManager('localhost', 27017, 'ec', 'suning-goods')
    return sn_goods


def mongo_jd_goods():
    global jd_goods
    if jd_goods is None:
        jd_goods = MongoManager('localhost', 27017, 'ec', 'jd-goods')
    return jd_goods
