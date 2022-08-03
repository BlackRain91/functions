# Создать проект и добавить его в гитхаб
# В проекте реализовать следующие функции:
# 1 конвертировать даты в разные форматы
# 2 сделать функцию которая принимает неограниченное количество именованных параметров с информацией о
# человеке и выводит их в файл имя которого также передаётся при вызове
# 3 функция принимает список и баланс
# Приходится по списку, если число положительное то оно прибавляется к балансу , если отрицательное то
# вызывается другая функция которая возвращает квадрат отрицательно числа и также прибавляет к балансу ,
# сделать проверку что число приходит именно отрицательное , первая функция в итоге должна вернуть баланс

def convector(data):
    while True:
        num = int(input("В какой формат времени конвертировать: "
                    "\n1.США. \n2.Великобритания. \n3.Россия. \n4.Венгрия \n5.Назад. "
                    "\nВведите номер выбраного варианта:  "))

        if num == 1:
            n = data.replace(" ","")
            print(n[2:4],"-",n[0:2],"-",n[4:],sep="")
        elif num == 2:
            n = data.replace(" ", "")
            print(n[0:2], "/", n[2:4], "/", n[4:], sep="")
        elif num == 3:
            n = data.replace(" ", "")
            print(n[0:2], ".", n[2:4], ".", n[4:], sep="")
        elif num == 4:
            n = data.replace(" ", "")
            print(n[4:], "-", n[2:4], "-", n[0:2], sep="")
        elif num == 5:
            break

def info(**data):
    f = open("Info.txt", "a")
    for k,v in data.items():
        f.write('{}:{}\n'.format(k,v))
    f.close()

def negative(i,balans):
    if i < 0:
        t = (i)**2
        balans = balans + t
        return balans

def positive(spis,balans):
    for i in spis:
        if i > 0:
            balans += i
            print(balans)
        if i < 0:
            balans += negative(i,balans)
    return balans

def main():
    while True:
        vvod = int(input("Выберите из предложенного списка: \n1.Конвертация даты. "
                         "\n2.Работа с файлом и данными. \n3.Баланс. \n4.Выход."
                         "\nДля выбора введите номер зачади:  "))

        if vvod == 1:
            data = input("Введите число,месяц и год: ")
            convector(data)

        elif vvod == 2:
            info(Surname="Семенов",Name="Антон",Age=26,Profession="Слесарь")
            info(Surname="Нульман", Name="Павел", Age=40, Profession="Фармацевт")
            info(Surname="Крижнев", Name="Семён", Age=19, Profession="Студент")

        elif vvod == 3:
            spis = [2,5,-12,22,54,-1,-64,22]
            balans = 0
            positive(spis,balans)

        elif vvod == 4:
            print("Программа завершена. Выход.")
            break



main()