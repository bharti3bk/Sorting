# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        if(cur_index == len(arr) - 1):
            break
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index+1, len(arr)):
            if(arr[j] < arr[smallest_index]):
                smallest_index = j
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
   


  # iterate Through all the array elements
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                return arr

                  


        # Because i Know last i element are already at the right Position 
         # iterate the array from 0 to n-i-1 because we are not Including last element in the Iteration  
             #  if the element found is greater than swap 
            

             


            

# STRETCH: implement the Count Sort function below
#  def count_sort( arr, maximum=-1 ):
#      return arr

     


    