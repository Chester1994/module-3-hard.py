data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_nested_sum(*args):
    summa = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            summa += calculate_nested_sum(*arg)
        elif isinstance(arg, dict):
            summa += calculate_nested_sum(*arg.items())
        elif isinstance(arg,(int, float)):
            summa += arg
        elif isinstance(arg,str):
            summa += len(arg)
    return summa
print(calculate_nested_sum(data_structure))
