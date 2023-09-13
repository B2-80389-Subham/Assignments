def display_elements_with_condition(my_list):
    result = []
    for items in my_list:
        if items.isdigit():
            result.append((items+' ') * 3)
        else:
            result.append(items + '#')
    return result


mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']
result_list = display_elements_with_condition(mylist)

for item in result_list:
    print(item)
