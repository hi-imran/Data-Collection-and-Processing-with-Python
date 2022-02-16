def f(item):
    if "w" in item:
        return True
    else:
        return False
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

w_lst = filter(f, lst_check)
print(list(w_lst))