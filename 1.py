from random import randint

#exsersize5.1
'''quantity = int(input("Enter the number of words:"))
words = []
for i in range(quantity):
    word = input(f"enter the word:")
    words.append(word)
line = " ".join(words)
print(line)'''

#exsersize5.2
'''words = []
while True:
    word = input("Enter the word:")
    if word.lower() == 'stop':
        print("the program is completed")
        break
    words.append(word)
line = " ".join(words)
print(line)'''

#exsersize5.3
def check_word(word):
    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

'''word = input("Enter the word:")
check_word(word)'''

#exsersize5.4
wrong_answers = 0
right_answers = 0
attempts = 0
'''while wrong_answers < 3 or right_answers < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    right_answer = num1 + num2
    print(f"Сколько будет {num1} + {num2}?")
    try:
        user_answer = int(input("Enter the answer:"))
    except ValueError:
        print("Incorrect input")
        continue
    attempts += 1
    if user_answer == right_answer:
        print("Right!")
        right_answers += 1
    else:
        print("Wrong!")
        wrong_answers += 1
    if right_answers == 3:
        print("The game is completed! You have 3 right answers!")
        break
    elif wrong_answers == 3:
        right_answers = attempts - wrong_answers
        print(f"The game is over! You have {right_answers} right answers!")
        break'''
#exsersize6.1
def if_divisible_by_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


'''num = int(input("Enter the number:"))
if if_divisible_by_3(num):
    print("The number is divisible by 3")
else:
    print("The number isn't divisible by 3")
if_divisible_by_3(num)'''

#exsersize6.2
def if_divisible_by_100(num):
    try:
        result = 100/num
        return result
    except ValueError:
        return "Incorrect input!"
    except ZeroDivisionError:
        return "Mistake!"


'''num = int(input("Enter the number: "))
try:
    result = if_divisible_by_100(num)
    print("Result: ", result)
except ValueError:
    print("Incorrect input!")
if_divisible_by_100(num)'''
#exsersize6.3
def magical_data(data):
    try:
        day, month, year = map(int, data.split("."))
        last_digit_year = year % 100
        return day*month == last_digit_year
    except ValueError:
        return False


'''data = input("Enter the data in format DD.MM.YYYY: ")
if magical_data(data):
    print("The data is magical!")
else:
    print("The data isn't magical =(")'''
#exsersize6.4
def lucky_ticket(num):
    length = len(num)
    if length % 2 != 0:
        return False
    middle = length//2
    amount_first_length = 0
    amount_second_length = 0
    for i in range(middle):
        amount_first_length += int(num[i])
        amount_second_length += int(num[i+1])
    return amount_first_length == amount_second_length

num = input("Enter the number of ticket: ")
if lucky_ticket(num):
    print("The ticket is lucky!")
else:
    print("The ticket isn't lucky =(")
lucky_ticket(num)
