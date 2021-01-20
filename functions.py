# my_list = [1,2,3,4,51,2,3,4,5]
# list_length = len(my_list)
#
# if list_length % 2 == 0:
#     print('my list is even')
# else:
#     print('my list is od')
#
# my_list = [1,2,3,4,5,1,2,3,4,5]
# list_length = len(my_list)
#
# index = 0
#
# while index < list_length:
#     list_element = my_list[index]
#     print('list_element', list_element)
#     index += 1
#
# print('index', index)

my_list = [1,2,3,4,5,1,2,3,4,5]
list_length = len(my_list)

for element in my_list:
    if element % 2 ==0:
        print(f'{element} Even number')
    else:
        print(f'{element} Od number')