from bubble_sort import BubbleSort
from merge_sort import MergeSort

list_to_sort = [5, 4, 3, 2, 1]
# list_to_sort = [1, 2, 3, 4, 5]
sorting_algo = BubbleSort()
sorting_algo.sort(list_to_sort)

print "Sorted using bubble-sort:"
print list_to_sort

list_to_sort = [5, 3, 4, 2, 1]
sorting_algo = MergeSort()
sorting_algo.sort(list_to_sort)

print "Sorted using merge-sort:"
print list_to_sort
