import heapq
def merge_arrays(A):
    min_heap = []
    merged = []
    for i, arr in enumerate(A):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    while min_heap:
        element, array_index, element_index = heapq.heappop(min_heap)
        merged.append(element)
        if element_index + 1 < len(A[array_index]):
            next_element = A[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, array_index, element_index + 1))
    return merged

A = [[1, 2, 3], [2, 4, 6], [0, 9, 10]]
print(merge_arrays(A))

# Abdelrahman Mohamed 11/314a