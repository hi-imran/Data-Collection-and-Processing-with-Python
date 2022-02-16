def even_no(items):
    even_lst = [num for num in items if num % 2 ==0]
    #          [[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]]
    return even_lst
print(even_no([1,2,3,4,5,6,7,8,9,]))