import sys,random

print('Hello! User, !')
print('Welcome to The Comment game')
print('Lets See the comments you got')
comment=('Have a great ','Brush your ', 'Be mindful of ', 'Take care of your ', 'Good ', 'Hug a ', 'Kiss your ','Eat your y')
ending =('Burger','Teeth','Snake','Day','Mind','Flowers','Week','Frog','yourself')

while True:
    firstcomment=random.choice(comment)
    endingcomment = random.choice(ending)
    
    print('*' * 40)
    print('{},{}'.format(firstcomment,endingcomment))
    print('*' * 40)

    try_again=input('\n To Try again (Press Y )\n\n To Exit(Press Q)')
    match try_again.lower():
         case 'n':
             break
         case 'y':
               input("\nPress Enter to exit.")