def calculate_structure_sum(data):
# Подсчёт суммы всех чисел и длин всех строк
    """
    Подсчёт суммы всех чисел и длин всех строк
    """
    SUM=0
    if isinstance(data, dict):
        data = list(data.items())
# Считаем float как строку
    if isinstance(data, float):
        data = str(data)
    for val in data:
        if isinstance(val, int):
            SUM += val
        else:
            if isinstance(val, str):
                SUM += len(val)
            else:
                SUM += calculate_structure_sum(val)
    return SUM


# MAIN V1.0 *PVS*
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
help(calculate_structure_sum)
