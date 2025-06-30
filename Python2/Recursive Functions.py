'''
def function_name(parameters):
    if base_conditions:
        return result
    return function_name(modified_parameters)
'''
'''List=[10,20,30,40,50,60,70,80,90,100]
def Add_List(List):
    if len(List)==0:
        return 0
    return List[0]+Add_List(List[1:])
print(Add_List(List))'''

List=[1,2,3,4,5]
def Add_List(list, Sum):
    if len(list)==0:
        return Sum
    if bool(list[len(list) - 1]):
        Sum= Sum + list[len(list) - 1]
        list.pop()
        return Add_List(list,Sum)
    return Sum
print(Add_List(List,0))

