# -*- coding: utf-8 -*-
# @Time : 2019/1/2 7:28 PM
# @Author : cxa
# @File : mongotocsv.py
# @Software: PyCharm
from db.mongohelper import get_data
import asyncio
import aiofiles
import pathlib
import datetime

async def m2f():
    data = await get_data()
    async for item in data:
        t = item.get("content").get("message").strip()
        fs = await aiofiles.open(pathlib.Path.joinpath(pathlib.Path.cwd().parent, "msg.txt"), 'a+')
        await fs.write(t)

async def get_ctime():
    data = await get_data()
    async for item in data:
        t = item.get("ctime")
        ymd=datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        fs = await aiofiles.open(pathlib.Path.joinpath(pathlib.Path.cwd().parent, "ctime.txt"), 'a+')
        await fs.write(f"{ymd}\n")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_ctime())
