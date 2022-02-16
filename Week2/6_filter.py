def keep_evens(num):
    if num%2 == 0:
        return True
    else:
        return False

lst = [3, 4, 6, 7, 0, 1]
even_lst = filter(keep_evens, lst)
print(list(even_lst))