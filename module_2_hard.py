while True :
    n = int(input("Введите число от 3 до 20:"))
# Выход из программы - 911
    if n == 911 :
        break
# Проверка корректного диапазона ввода
    if n < 3 or n > 20 :
        print("Некорректное число. Допустимый дипапазон от 3 до 20. Для выхода - 911")
        continue
    result = []
    for j in range(1,21):
        for k in range(j+1,21):
            if (n % (j+k) == 0) and n != j and n != k:
                result.append(j)
                result.append(k)
    print(n,"-",*result,sep="")


