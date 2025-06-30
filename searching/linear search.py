'''Arr=[5,6,2,3,4,1,0,7,8,9]
def Linearsearch(key,arr,len):
    for i in range(len):
        if arr[i]==key:
            return i
    return None
res=Linearsearch(1,Arr,10)
if res==None:
    print("Element is not found")
else:
    print(f"Element found at {res} index")
'''

def Linearsearch(key,arr,len):
    count=0
    for i in range(len):
        count+=1
        print(f"{count} Iteration")
        if arr[i]==key:
            print(f"Element found at index {i}")
            break
    else:
        print(f"Element not found ")
res=Linearsearch(9,[5,6,2,3,4,1,0,7,8,9],10)