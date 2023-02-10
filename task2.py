from functools import partial
from typing import Callable, List, Any


# ошибка была в том, что при определении лямбда-функции коллбек вызывался сразу,
# а не во время исполнения execute_handlers

def create_handlers(callback: Callable[[int], Any]) -> List[Callable[[int], Any]]:
    handlers = []
    for step in range(5):
        func: Callable[[int], Any] = partial(callback, step)
        handlers.append(func)
    return handlers


def execute_handlers(handlers: List[Callable[..., Any]]) -> None:
    for handler in handlers:
        handler()
