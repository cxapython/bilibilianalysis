# -*- coding: utf-8 -*-
# @Time : 2018/11/18 10:41 PM
# @Author : cxa
# @File : motordb.py
# @Software: PyCharm
import asyncio

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

from motor.motor_asyncio import AsyncIOMotorClient


class MotorBase:
    _db = {}
    _collection = {}

    def __init__(self, loop=None):
        self.motor_uri = ''
        self.loop = loop or asyncio.get_event_loop()

    def client(self, db):
        self.motor_uri = f"mongodb://localhost:27017/{db}"
        return AsyncIOMotorClient(self.motor_uri, io_loop=self.loop)

    def get_db(self, db='weixin_use_data'):
        if db not in self._db:
            self._db[db] = self.client(db)[db]

        return self._db[db]


async def save_data(items):
    mb = MotorBase().get_db('weixin_use_data')
    for item in items:
        try:
            await mb.bilibili_comments.update_one({
                'rpid': item.get("rpid")},
                {'$set': item},
                upsert=True)
        except Exception as e:
            print("数据插入出错", e.args,"此时的item是",item)

async def get_data():
    mb = MotorBase().get_db('weixin_use_data')
    data=mb.bilibili_comments.find()
    return data

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data())
