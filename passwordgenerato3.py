#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letter = []
x = 0
for letter in letters[0:nr_letters]:
 x = random.choice(letters)
 random_letter.append(x)


random_symbol = []
x1 = 0
for symbol in symbols[0:nr_symbols]:
 x1 = random.choice(symbols)
 random_symbol.append(x1)


random_number = []
x2 = 0
for number in numbers[0:nr_numbers]:
 x2 = random.choice(numbers)
 random_number.append(x2)


final_list = random_letter + random_number + random_symbol

random.shuffle(final_list)
final_list2 = ''.join(final_list)

print(f"Here's your freshly minted password: {final_list2}")