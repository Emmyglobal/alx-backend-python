#!/usr/bin/env python3
"""Async Comprehensions"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """A coroutine that iterates through the async gen"""
    comp = [num async for num in async_generator()]
    return comp
