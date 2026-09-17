#queue = FIFO (First In First Out)
#stores data like a queue of items, but with itms with higher priority

queue = []

#enqueue
def enqueue(queue: list[int], item: int) -> list[int]:

    if not queue:
        queue.append(item)
    else:
        for el in queue:
            if el > item:
                queue.insert(queue.index(el), item)
                break
        else:
            queue.append(item)

#dequeue
def dequeue(queue: list[int]) -> int:
    return queue.pop(0)
