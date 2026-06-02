array = [1,2,3,4,5,6,7,8,9]

def linearsearch (array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    
    return -1
        
index = linearsearch(array, 10)

print(index)
