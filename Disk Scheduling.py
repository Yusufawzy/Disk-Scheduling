# Name: Yusuf Fawzy Elnady          ID:20160299
def FCFS(arr,start):
    print("First Come First Served")
    cost = 0;
    print (str(start)+'->',end='')
    temp = start
    for idx,i in enumerate(arr):
        if idx == len(arr)-1:
            print(str(i), end='')
        else:
            print(str(i)+ '->', end='')
        cost+=abs(temp-i);
        temp = i
    print("\nTotal Number of Cylinders moves is "+str(cost))
def getMin(curr,arr):
    minn = 10e9
    idx = -1
    for i in (arr):
        if (abs(curr-i)<minn):
            minn =abs(curr-i)
            idx = i
    return idx
def SSTF(arr,start):
    print("Shortest Seek Time First")
    cost = 0
    print(str(start) + '->', end='')
    temp = start
    while(True):
        if (len(arr)==0):break
        minn = getMin(temp,arr)
        if (len(arr)==1):
            print(str(minn) , end='')
        else:print(str(minn) + '->', end='')
        cost+=abs(temp-minn)
        temp = minn
        arr.pop(arr.index(minn))
    print("\nTotal Number of Cylinders moves is " + str(cost))

def getRight(arr,curr):
    temp = arr[0]
    #returns the
    arr = sorted(arr)
    print(arr)
def scan(arr,start):
    # First will start by go to the most right (0) then take all in way to left
    cost = start + max(arr)
    arr1=[];arr2=[]
    for element in (arr):
        if (element<start):
            arr1.append(element)
        else:
            arr2.append(element)
    arr1= sorted(arr1)
    arr1.reverse()
    arr2.sort()
    print('{}->'.format(start), end="")
    for element in arr1:
        print(str(element) + '->', end='')
    print('0->',end="")
    for idx,element in enumerate(arr2):
        if (idx==len(arr2)-1):
            print(str(element), end='')
        else:
            print(str(element) + '->', end='')
    print("\nTotal Number of Cylinders moves is " + str(cost))
def cScan(arr,start):
    arr1 = [];arr2 = [];Maxi = 199
    for element in (arr):
        if (element > start):
            arr1.append(element)
        else:
            arr2.append(element)
    #assuming Maxi is 200
    arr1.sort()
    arr1.append(Maxi)
    arr2.sort()
    print('{}->'.format(start), end="")
    for element in arr1:
        print(str(element) + '->', end='')
    print('0->', end="")
    for idx, element in enumerate(arr2):
        if (idx == len(arr2) - 1):
            print(str(element), end='')
        else:
            print(str(element) + '->', end='')
    cost = ( Maxi - start) + max(arr2) + Maxi
    #will always go to left then to zero then again to left
    print("\nTotal Number of Cylinders moves is " + str(cost))


def cLook(arr,start):
    arr1 = [];
    arr2 = [];
    Maxi = 199
    for element in (arr):
        if (element > start):
            arr1.append(element)
        else:
            arr2.append(element)
    # assuming Maxi is 200
    arr1.sort()
    arr2.sort()
    print('{}->'.format(start), end="")
    for element in arr1:
        print(str(element) + '->', end='')
    for idx, element in enumerate(arr2):
        if (idx == len(arr2) - 1):
            print(str(element), end='')
        else:
            print(str(element) + '->', end='')
    cost = (max(arr1) - start) +(max(arr1) - min(arr2))  +( max(arr2) - min(arr2))
    # will always go to left then to zero then again to left
    print("\nTotal Number of Cylinders moves is " + str(cost))

def optimized (arr,start=0):
    arr.sort()
    cost = max(arr) # Here I just have to send the max number
    print('0->', end='')
    for idx, element in enumerate(arr):
        if (idx == len(arr) - 1):
            print(str(element), end='')
        else:
            print(str(element) + '->', end='')
    print("\nTotal Number of Cylinders moves is " + str(cost))

def main():
    while(True):
        n = int(input("Enter number\n1-FCFS\n2-SSTF\n3-SCAN\n4-C-SCAN\n5-C-Look\n6-Optimized\n"))
        if (n>6 or n<1):
            print("Please enter a valid number")
            continue

        ''' len = int(input("Enter the length of the array"))
        arr = []
        for i in range (len):
            arr.append(int(input()))
        start = int(input("Enter the start head posistion"))
        '''

        arr = [98, 183, 37, 122, 14, 124, 65, 67]
        start = 53
        if n==1: FCFS(arr, start);
        elif n==2: SSTF(arr, start)
        elif n==2: SSTF(arr, start)
        elif n==3: scan(arr, start)
        elif n==4: cScan(arr, start)
        elif n==5: cLook(arr, start)
        elif n==6: optimized(arr)
        else : print("Enter a valid number\n")
        print('*'*100)
if __name__ == '__main__':
    main()