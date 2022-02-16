"""
Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
"""
def f(val):
    # print(type(val))
    # print(val)
    if type(val) == list:
        c = []
        c = val * 2
        return c
    else:
        return val*2


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = map(f, lst)
print(list(greeting_doubled))
