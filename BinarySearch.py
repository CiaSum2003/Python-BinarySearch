# Cianee Sumowalt
# Binary Search
# 4 November 2022

import random


def createList(L):
    L = []
    for int in range (desiredSize):
        ran = random.randint(0,1000)
        L.append (ran)
        list(set(L))
# Created a list of 20 unique integers. Now sorting them
    return L

def find_target (new_list):
    target_list = []
    algorithm = input (f"\n Choose the algorithm: 'I' for Iterative, 'R' for Recursive: ")
    foundit = False
    while foundit == False:
        target = random.randint(0, 1001)
        if target not in target_list:
            target = target
            target_list.append(target)
        print ("\n Target =",target)
        if algorithm == "I":
            if binarySearchIterative(new_list,target) == True:
                foundit = True
        else:
            if binarySearchRecursive(new_list,target) == True:
                foundit = True
    print ("\n It took",len(target_list),"attempts to find the number selected.")

def binarySearchIterative(L, element):
    low = 0
    high = len(L) - 1
    middle = 0
    while low <= high:
        middle = (high + low) // 2
        if L[middle] > element:
            high = middle - 1
        elif L[middle] < element:
            low = middle + 1
        else:
            return True
    return False

def binarySearchRecursive(L, element):
    low = 0
    high = len(L)-1
    if low <= high:
        middle = (high+low)//2
        if L[middle] == element:
            return True
        elif L[middle] > element:
            high = middle-1
            return binarySearchRecursive((L[:high]),element)
        elif L[middle] < element:
            low = middle+1
            return binarySearchRecursive((L[low:]),element)
    return False

def sortem(L):
    for index in range (0, len(L)-1):
        minVal = L[index]
        minIndex = index
        for k in range (index+1,len(L)):
            if L[k] < minVal:
                minVal = L[k]
                minIndex = k
        L[minIndex] = L[index]
        L[index] = minVal
    return L

print ("\nThis program creates a list of random integers and then sorts them")
print ("It then picks random integers in the same interval until it gets a hit")
print ("using the binary search algorithm")

desiredSize = int(input("\nEnter the desired list size: "))

num_list = createList(desiredSize)
print ("\nOriginal List:", num_list, "\n")

new_list = sortem(num_list)
print ("\nSorted List", new_list,"\n")

count = find_target (new_list)




