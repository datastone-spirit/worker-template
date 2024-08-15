import asyncio
from time import sleep
from typing import Any, Dict

from sprite_gpu import start
from sprite_gpu.env import Env


def handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {request}"
    request.get('localhost:8000')
    return bytes(output, "utf-8")


start({"handler": handler)
