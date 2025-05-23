import random
level=1
print('Welcome to level based guess game!!!')
max_number=level*10
secret_number=random.randint(1,max_number)
attempt=0
print(f'\n Level{level}: guess between 1 and {max_number}')
while True:
    guess=int(input('Enter a number :'))
    attempt+=1
    if guess==secret_number:
        print('Yes its correct, you made',attempt,'attempts.')
        break
    elif guess<secret_number:
        print('Too low, Try again')
    else:
        print('Too high, Try again')
next_level=input('Do you want to go to next level? (Yes/No):').lower()
if next_level=="yes":
     level+= 1
     print("Here is the next level '2'")
     print('Welcome to level based guess game!!!')
max_number=level*10
secret_number=random.randint(1,max_number)
attempt=0
print(f'\n Level{level}: guess between 1 and {max_number}')
while True:
    guess=int(input('Enter a number :'))
    attempt+=1
    if guess==secret_number:
        print('Yes its correct, you made',attempt,'attempts.')
        break
    elif guess<secret_number:
        print('Too low, Try again')
    else:
        print('Too high, Try again')
else:
    print('Thanks for playing')

    
    