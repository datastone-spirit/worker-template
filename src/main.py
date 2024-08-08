import asyncio
from time import sleep
from typing import Any, Dict

from sprite_gpu import start
from sprite_gpu.env import Env


def concurrency_modifier(current_concurrency: int) -> int:
    """
    Allow 5 job to run concurrently.
    Be careful with this function.
    You should fully understand python GIL and related problems before setting this value bigger than 1.
    """
    return 1


async def async_handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {input}"
    await asyncio.sleep(0.1)
    return bytes(output, "utf-8")


async def async_gen_handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {input}"
    for i in range(10):
        await asyncio.sleep(0.01)
        yield f"{output} - {i}\n"


def gen_handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {input}"
    for i in range(10):
        sleep(0.01)
        yield f"{output} - {i}\n"


def handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {input}"
    sleep(0.1)
    return bytes(output, "utf-8")


# Start the serverless function
# start({"handler": async_handler, "concurrency_modifier": concurrency_modifier})
# start({"handler": async_gen_handler, "concurrency_modifier": concurrency_modifier})
# start({"handler": gen_handler, "concurrency_modifier": concurrency_modifier})
start({"handler": handler, "concurrency_modifier": concurrency_modifier})
