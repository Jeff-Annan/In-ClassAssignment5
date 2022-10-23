#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

def partition(arr, low, high):
 
  pivot = arr[high]

 
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])


  return i + 1



def quicksort(arr, low, high):
    if low < high:
        
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot -1)
        quicksort(arr, pivot + 1, high)
        return arr






def main():
    with open("numbers.txt") as myfile:
        data = myfile.readline().split(',\[\]')
        print(type(data))
        
        data1 = data[0]
        data1 = data1.replace('[', "")
        data1 = data1.replace(']', "")
        print(data1)
        print(type(data1.split(',')))        
        data2 = data1.split(',')
        print(data2[0])
        print(type(data2[0]))
        data3 = list(map(int, data2))
        print(data2[0])
        print(data3[0])
        print(type(data3[0]))
        sortedlist = quicksort(data3, 0, len(data3)-1)
        print(sortedlist)
        with open(r'Sorted.txt', 'w') as fp:
            fp.writelines(str(sortedlist))


    return 


if __name__ == "__main__":
    main()




                            '''references'''
'''https://www.geeksforgeeks.org/quick-sort/
https://www.studytonight.com/python-programs/python-program-for-quicksort'''