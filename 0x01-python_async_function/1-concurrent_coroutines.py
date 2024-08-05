#!/usr/bin/env python3
"""Concurrent coroutines"""


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay between 0 and max_delay"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
