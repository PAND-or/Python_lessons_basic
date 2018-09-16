__author__ = "Андрей Петров"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    
    str_number = str(number)
    
    dot_index = str_number.find(".")
    integer_number = str_number[:dot_index]
    dec_number = str_number[dot_index+1:]
    
      
    list_number = [int(i) for i in dec_number] #преобразование в список
    j = 0
    for k, num,  in enumerate(reversed(list_number)): #проход по списку в обратном порядке
        if j > 0: 
            num += 1
            j = 0
        if (num >= 10) & (len(list_number) - k - 2 >= 0):
                list_number[-k-2] += 1
                num = num - 10
        elif(num >= 10) & (ndigits == 0):
            integer_number = int(integer_number) + 1
        if k < len(list_number) - ndigits: #До какой точности считаем + 0 и точка 
            list_number[-k-1] = 0
            j = 1 if int(num) > 5 else 0
        else:
            list_number[-k-1] = num


    return int(integer_number) + int(''.join(str(x) for x in list_number))/(10**len(list_number))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    #str_number = str(ticket_number)
    list_number = [int(i) for i in str(ticket_number)] 
    lenght = len(list_number)
    if(lenght % 2 == 0):
        sumone = sum(list_number[:int(lenght / 2)])
        sumtwo = sum(list_number[int(lenght / 2):])
        return True if sumone == sumtwo else  False
    else:
        sumone = sum(list_number[:int((lenght-1) / 2)])
        sumtwo = sum(list_number[int((lenght+1) / 2):])
        return sumone == sumtwo
    
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
