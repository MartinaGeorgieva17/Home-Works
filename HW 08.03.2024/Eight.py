#Напишете програма, която преобразува дадено число в интервала [0..999] в текст, 
#съответстващ на българското произношение. Примери:
#-0 -> “Нула”
#-273 -> ”Двеста седемдесет и три”
#-400 -> ”Четиристотин”
#-501 -> “Петстотин и едно”
#-711 -> “Седемстотин и единадесет” 

def convert_to_words(number):
     # Списъци за текстовото представяне на цифрите и десетките
    units = ['', 'едно', 'две', 'три', 'четири', 'пет', 'шест', 'седем', 'осем', 'девет']
    tens = ['', 'десет', 'двадесет', 'тридесет', 'четиридесет', 'петдесет', 'шестдесет', 'седемдесет', 'осемдесет', 'деветдесет']
    # Списък за текстовото представяне на стотиците
    hundreds = ['', 'сто', 'двеста', 'триста', 'четиристотин', 'петстотин', 'шестстотин', 'седемстотин', 'осемстотин', 'деветстотин']
 
 # Проверка за числа в интервала [0, 999]
    if number <0 or number > 999:
        return('Грешка')
    
    # Проверка за 0
    if number == 0:
        return('Нула')
    
    # Изчисляване на стотиците, десетиците и единиците
    hundred = number // 100
    ten = (number % 100) // 10
    unit = number % 10

    # Генериране на текстовото представяне на числото
    words = ''
    if hundred != 0:
        words += hundreds[hundred] + ' '
    if ten != 0:
        if ten == 1:
            if unit == 0:
                words += 'десет'
            elif unit == 1:
                words += 'единадесет'
            elif unit == 2:
                words += 'дванадесет'
            elif unit == 3:
                words += 'тринадесет'
            elif unit == 4:
                words += 'четиринадесет'
            elif unit == 5:
                words += 'петнадесет'
            elif unit == 6:
                words += 'шестнадесет'
            elif unit == 7:
                words += 'седемнадесет'
            elif unit == 8:
                words += 'осемнадесет'
            elif unit == 9:
                words += 'деветнадесет'
            return words.strip()
        else:
            words += tens[ten] + ' '
    if unit != 0:
        words += units[unit]

    return words.strip()

# Примери на преобразуване на числата в текст
print(convert_to_words(0))
print(convert_to_words(273))
print(convert_to_words(400))
print(convert_to_words(501))
print(convert_to_words(711))


