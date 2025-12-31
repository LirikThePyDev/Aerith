# __init__.py
from .interpreter import run_async, Env
import asyncio

def execute_script(script_path):
    with open(script_path, 'r') as f:
        source = f.read()
    env = Env()
    asyncio.run(run_async(source, env))

__all__ = ['execute_script', 'run_async', 'Env']
