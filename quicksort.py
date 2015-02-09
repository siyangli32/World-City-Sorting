#Siyang Li
#2.25.2013
#Lab Assignment 4: Quicksort

#partition function that takes a list and partitions the list w/ the last item
#in list as pivot
def partition(the_list, p, r, compare_func):
    
    pivot = the_list[r] #sets the last item as pivot
    i = p-1 #initializes the two indexes i and j to partition with
    j = p
    
    while not j == r: #function runs as long as j has not reached last object in list 
       if compare_func(the_list[j], pivot): #takes in compare function to return Boolean
            i += 1 #increments i before j
            
            temp = the_list[i] #switches i value with j value
            the_list[i] = the_list[j]
            the_list[j] = temp
            
       j += 1 #increments j
        
    temp = the_list[r] #switches pivot with the first object larger than pivot
    the_list[r] = the_list[i+1]
    the_list[i+1] = temp
        
    return i+1 #returns q = i+1 (or pivot position)

#quicksort function takes in the partition function and recursively sorts list
def quicksort(the_list, p, r, compare_func):
    if p < r: #recursive
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)
    
    return the_list

#sort function sorts the entire list using quicksort      
def sort(the_list, compare_func):
    return quicksort(the_list, 0, len(the_list)-1, compare_func)
    
        