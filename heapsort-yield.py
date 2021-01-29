# heap sort algorithm with yield
from heapq import heappop, heappush

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    yield ordered

result = heap_sort([13, 21, 15, 5, 26, 4, 17, 18, 24, 2])
for x in result:
    print(x)