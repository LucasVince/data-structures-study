#stack = LIFO (Last In First Out)
#stores data like a tower of items
#push = add to the top of the stack
#pop = remove from the top of the stack
#peek = view the top of the stack
#is_empty = check if the stack is empty

stack: int = []

#push
def push(stack: list[int], item: int) -> list[int]:
    stack.append(item)
    return stack

print(push(stack, 1))

#pop
def pop(stack: list[int]) -> int:
    return stack.pop()

print(pop(stack))

#peek
def peek(stack: list[int]) -> int:
    if not stack:
        return []
    
    return stack[-1]

print(peek(stack))

#is_empty
def is_empty(stack: list[int]) -> bool:
    return not bool(stack)

print(is_empty(stack))

#search
def search(stack: list[int], item: int) -> int:
    if item not in stack:
        return -1
    return stack.index(item) + 1

print(search(stack, 1))
