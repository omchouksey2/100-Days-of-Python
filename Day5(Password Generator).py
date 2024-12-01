import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
specail_char=['!','@','#','$','%','&','*','(',')','+']

print("Welcome to Om's Password Generator:")
in_letter=int(input("How many letters would you like in your Password?\n"))
in_number=int(input("How many nubers would you like in your Passwors?\n")) 
in_special_char=int(input("How many special charecter would you like in your password?\n"))  

password_list=[]

for i in range(0,in_letter):
    password_list.append(random.choice(letter))

for i in range(0,in_number):
    password_list.append(random.choice(number)) 

for i in range(0,in_special_char):
    password_list.append(random.choice(specail_char))
 
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(f"Your Generated Password is {password}")   