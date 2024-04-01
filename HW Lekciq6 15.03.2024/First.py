#Да се напише програма, която да намира тези числа, които се делят на 7 и на
#5, между 1500 и 2700.

# Инициализираме празен списък, 
#в който ще съхраняваме числата, които отговарят на условието

numbers =[]
# Итерираме през 
#всички числа в интервала от 1500 до 2700 (включително)
for i in range(1500,2701):
    ## Проверяваме дали текущото число се дели и на 7, и на 5
    if i % 7 == 0 and i%5==0:
        # Ако условието е изпълнено, добавяме числото към списъка
        numbers.append(i)
        ## Извеждаме числата, отговарящи на условието
print("Числата, които се делят на 7 и на 5 между 1500 и 2700 са:")
print(numbers)