from operator import truediv

grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo',
            'Steve', 'Khendrik',
            'Aaron'}
sorted_students = list(students)
sorted_students.sort()

# Если мы не знаем операторов цикла и других функций библиотеки
diary = {sorted_students[0]: sum(grades[0]) / len(grades[0]),
         sorted_students[1]: sum(grades[1]) / len(grades[1]),
         sorted_students[2]: sum(grades[2]) / len(grades[2]),
         sorted_students[3]: sum(grades[3]) / len(grades[3]),
         sorted_students[4]: sum(grades[4]) / len(grades[4])}
print("Method 1:", diary)

# Если мы знаем for
d1 = dict.fromkeys(sorted_students, 0.0)
for i in range(len(students)):
    d1[sorted_students[i]] = sum(grades[i]) / len(grades[i])
print("Method 2:", d1)

# Или так, если мы знаем for и индекс по списку
d3 = dict.fromkeys(sorted_students, 0.0)
i = 0
for val in grades:
    d3[sorted_students[i]] = sum(val) / len(val)
    i = i + 1
print("Method 3:", d3)

# Или так, если мы знаем for и индекс по ZIP
d5 = dict.fromkeys(sorted_students, 0.0)
for key, val in zip(sorted_students, grades):
    d5[key] = sum(val) / len(val)
print("Method 4:", d5)

# Или так, если мы знаем for, индекс по ZIP и MAP
d4 = dict.fromkeys(sorted_students, 0.0)


# Функция вычмсление среднего балла
def average(x):
    return float(sum(x)) / float(len(x))


ga = map(average, grades)
ga_list = list(ga)
for i, j in zip(sorted_students, ga_list):
    d4[i] = j
print("Method 5:", d4)

# Если мы знаем while
d2 = dict.fromkeys(sorted_students, 0.0)
i = True
while i:
    try:
        key = sorted_students.pop(0)
        value = grades.pop(0)
        d2[key] = sum(value) / len(value)
    except IndexError:
        i = False
print("Method 6:", d2)
