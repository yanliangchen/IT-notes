#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import asyncio


async def hello():

    print('Hello world! (%s)' % threading.currentThread())
    # 协程: 暂停程序的
    await asyncio.sleep(2)

    print('Hello again! (%s)' % threading.currentThread())



# 异步
loop = asyncio.get_event_loop()

tasks = [hello(),hello()]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()