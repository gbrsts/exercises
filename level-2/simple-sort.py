# Read three integers and sort them in ascending order. After, print these values in ascending order, 
# a blank line and then the values in the sequence as they were readed.

# Input
# The input contains three integer numbers.

# Output
# Present the output as requested above.

################################### Selection Sort ###################################
# def selection_sort(int_List):
#   n = len(int_List)
#   for j in range(n - 1):
#     min_index = j
#     for i in range(j, n):
#       if int_List[i] < int_List[min_index]:
#         min_index = i
#     if int_List[j] > int_List[min_index]:
#       aux = int_List[j]
#       int_List[j] = int_List[min_index]
#       int_List[min_index] = aux
#   print(int_List)

# def reverse_selection_sort(int_List):
#   n = len(int_List)
#   for j in range(n - 1):
#     min_index = j
#     for i in range(j, n):
#       if int_List[i] > int_List[min_index]:
#         min_index = i
#     if int_List[j] < int_List[min_index]:
#       aux = int_List[j]
#       int_List[j] = int_List[min_index]
#       int_List[min_index] = aux
#   print(int_List)

# List = []
# List = input().split(" ")
# int_List = [int(i) for i in List]
# selection_sort(int_List)
# reverse_selection_sort(int_List)


################################### Bubble Sort ###################################
# def bubble_sort(int_List):
#   n = len(int_List)
#   for j in range(n - 1):
#     for i in range(n - 1):
#       if int_List[i] > int_List[i + 1]:
#         # aux = int_List[i]
#         # int_List[i] = int_List[i + 1]
#         # int_List[i + 1] = aux
#         int_List[i], int_List[i + 1] = int_List[i + 1], int_List[i]
#   print(int_List)

# def reverse_bubble_sort(int_List):
#   n = len(int_List)
#   for j in range(n - 1):
#     for i in range(n - 1):
#       if int_List[i] < int_List[i + 1]:
#         # aux = int_List[i]
#         # int_List[i] = int_List[i + 1]
#         # int_List[i + 1] = aux
#         int_List[i], int_List[i + 1] = int_List[i + 1], int_List[i]
#   print(int_List)

# List = []
# List = input().split(" ")
# int_List = [int(i) for i in List]
# bubble_sort(int_List)
# reverse_bubble_sort(int_List)


################################### Insertion Sort ###################################
def insertion_sort(int_List):
  n = len(int_List)
  for i in range(1, n):
    key = int_List[i]
    j = i - 1
    while j >= 0 and int_List[j] > key: 
      int_List[j + 1] = int_List[j]
      j = j - 1
    int_List[j + 1] = key
  print(int_List)

def reverse_insertion_sort(int_List):
  n = len(int_List)
  for i in range(n - 1, 0):
    key = int_List[i]
    j = i - 1
    while j >= 0 and int_List[j] < key: 
      int_List[j + 1] = int_List[j]
      j = j - 1
    int_List[j + 1] = key
  print(int_List)

List = []
List = input().split(" ")
int_List = [int(i) for i in List]
insertion_sort(int_List)
reverse_insertion_sort(int_List)


################################### Merge Sort ###################################
# def merge_sort(int_List, start = 0, end = None):
#   if end is None:
#     end = len(int_List)
#   if(end - start > 1):
#     mid = (end + start) // 2
#     merge_sort(int_List, start, mid)
#     merge_sort(int_List, mid, end)
#     merge(int_List, start, mid, end)
#   print(int_List)

# def merge(int_list, start, mid, end):
#   left = int_list[start:mid]
#   right = int_list[mid:end]
#   top_left, top_right = 0, 0
#   for k in range(start, end):
#     if top_left >= len(left):
#       int_list[k] = right[top_right]
#       top_right += 1
#     elif top_right >= len(right):
#       int_list[k] = left[top_left]
#       top_left += 1
#     elif left[top_left] < right[top_right]:
#       int_list[k] = left[top_left]
#       top_left += 1
#     else:
#       int_list[k] = right[top_right]
#       top_right += 1

# List = []
# List = input().split(" ")
# int_List = [int(i) for i in List]
# merge_sort(int_List)
# # reverse_merge_sort(int_List)

################################### Quick Sort ###################################
# def quick_sort(int_List, start = 0, end = None):
#   print(int_List)
#   if end is None:
#     end = len(int_List) - 1
#   if start < end:
#     p = partition(int_List, start, end)
#     quick_sort(int_List, start, p - 1)
#     quick_sort(int_List, p + 1, end)

# def partition(int_List, start, end):
#   pivot = int_List[end]
#   i = start
#   for j in range(start, end):
#     if int_List[j] <= pivot:
#       int_List[j], int_List[i] = int_List[i], int_List[j]
#       i += 1
#   int_List[i], int_List[end] = int_List[end], int_List[i]
#   return i 

# List = []
# List = input().split(" ")
# int_List = [int(i) for i in List]
# quick_sort(int_List)
# # reverse_quick_sort(int_List)