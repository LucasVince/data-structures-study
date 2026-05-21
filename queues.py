#queue = FIFO (First In First Out)
#stores data like a queue of items

queue: int = []

#enqueue
def enqueue(queue: list[int], item: int) -> list[int]:
    queue.append(item)
    return queue

print(enqueue(queue, 1))

#dequeue
def dequeue(queue: list[int]) -> int:
    return queue.pop(0)

print(dequeue(queue))

#peek
def peek(queue: list[int]) -> int:
    if not queue:
        return []
    return queue[0]

print(peek(queue))

#is_empty
def is_empty(queue: list[int]) -> bool:
    return not bool(queue)

print(is_empty(queue))

#size
def size(queue: list[int]) -> int:
    return len(queue)

print(size(queue))

#contain
def contain(queue: list[int], item: int) -> int:
    return item in queue

print(contain(queue, 1))
