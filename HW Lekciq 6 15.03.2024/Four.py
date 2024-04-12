#. Да се напише програма, която да обръща буквите на дадена дума на обратно.
#Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.
#Вход:
#Input a word to reverse: Hello
#Изход:
#olleH



def reverse_word(word): 
    reversed_word='' #Празен низ, в който ще се съхранява обратната дума
    for char in word: # Обхождане на всеки символ в думата
        reversed_word= char+reversed_word  # Добавяне на текущия символ в началото на обратната дума
    return reversed_word # Връщане на обратната дума

def main():
    word = input ('Въведете думата, която желаете:')  # Въвеждане на думата от потребителя
    reversed_word = reverse_word(word) # Обръщане на думата
    print('Обърнатата дума е:', reversed_word)  # Извеждане на обратната дума на екрана

if __name__ == "__main__":
    main()
