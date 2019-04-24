# -*- coding: utf-8 -*-
# @Time : 2018/12/26 9:55 PM
# @Author : cxa
# @File : spider.py
# @Software: PyCharm
import asyncio
import aiohttp
from db.mongohelper import save_data
import async_timeout

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass
import glom

sem = asyncio.Semaphore(10)
base_url = "https://api.bilibili.com/x/v2/reply?pn={pn}&type=1&oid=19390801"


# proxy = "http://127.0.0.1:1087" 代理, proxy=proxy


async def fetch(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            with async_timeout.timeout(10):
                async with session.get(url) as res:
                    data = await res.json()
                    print(data)
                    await asyncio.sleep(2)
                    await save_data(glom.glom(data, "data.replies"))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [fetch(base_url.format(pn=i)) for i in range(1, 1260)]
    loop.run_until_complete(asyncio.wait(tasks))
