from ast import Continue
import sys,random

print('Hello! User, !')
print('Welcome to The Comment game')
print('Lets See the comments you got')
comment=('Have a great ','Brush your ', 'Be mindful of ', 'Take care of your ', 'Good ', 'Hug a ', 'Kiss your ','Eat your ')
ending =('Burger','Teeth','Snakes','Day','Mind','Flowers','Week','Frog','yourself')
cont = True
while cont:
    firstcomment=random.choice(comment)
    endingcomment = random.choice(ending)
    
    print('*' * 40)
    print('{}{}'.format(firstcomment,endingcomment))
    print('*' * 40)

    try_again=input('\n To Try again (Press Y )\tTo Exit(Press Q)\n')
    match try_again.lower():
         case 'q':
             print('\nExiting game........')
             cont = False
         case 'y':
               continue
            
        