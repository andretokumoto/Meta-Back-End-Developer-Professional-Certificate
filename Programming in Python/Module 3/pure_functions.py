my_list = [1,2,3]

def add_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_list(my_list,10)

print(my_list)
print(new_list)