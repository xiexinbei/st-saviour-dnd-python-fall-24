import time
import random
from highschooladv import Player
from draw import draw_d20, draw_d4, draw_d6

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print('Bludgeons & Flagons')

    # player = Tav('Xinbei', 'high school student')
    # player.print_character_sheet()
    # print()

    locations = ['art room', 'principal\'s office', 'music room']
    r = random.randint(0, len(locations) - 1)
    careers = ['artist', 'musician', 'staff member']
    c = random.randint(0, len(careers)-1)

    # collecting user input
    name = input('Name: ')
    role = careers[c]
    print('Role: ' + careers[c])
    player = Player(name, role)
    player.print_character_sheet()

    if player.role == 'musician':
       print('you\'re a musician!')
    if player.role == 'staff member':
       print('you\'re a staff member!')
    if player.role == 'artist':
       print('you\'re an artist!')

    # print(name)
    print_dramatic_text('Our story begins in an abandoned high school ... Welcome ' + name + ' to the horrible story!')
    print_dramatic_text('You start in the ' + locations[r])
    print('302: music room')
    print('201: art room')
    print('100: principal\'s office')
    print_dramatic_text('Which room do you want to enter?')
    room = input('Room number: ')
    if (room == '201'):
           print_dramatic_text('You are in Art room!')
           roll = random.randint(1,20)
           draw_d20(roll)
           if roll == 6:
              print_dramatic_text('win!')
           else:
              print_dramatic_text('Retry the gaaame!')
    if (room == '100'):
             print_dramatic_text('A ghost came to kiss you and have a crush on you! Leave the school with it!')
    if(room == '302'):
        print_dramatic_text('You enter the music room ...')
        roll = random.randint(1,20)
        draw_d20(roll)
        if roll == 1:
         room = input('Room number: ')
         if (room == '201'):
           print_dramatic_text('You are in Art room!')
           roll = random.randint(1,20)
           draw_d20(roll)
        if roll == 6:
              room = input('Room number')
              if (room == '100'):
               print_dramatic_text('A ghost came to kiss you and have a crush on you! Leave the school with it!')
        else:
         if roll >= 2:
          print_dramatic_text('You go to the dungeon! Answer this easy question to go back!')
          print_dramatic_text('1 在音乐里面是什么意思')
          if player.role == 'musician':
           print_dramatic_text('Translation: what is 1 mean music?')
          else:
           print_dramatic_text('Do you want to get buffs?')
           print_dramatic_text('Yes or no?')
           choice = input('Choice: ')
           if choice == "yes" or "Yes":
              player.level += 1
              player.print_character_sheet()
              print_dramatic_text('Translation: what is 1 mean music?')
           else :
              print_dramatic_text('Lost!!!')
         answer = input ('Answer: ')
         if answer == 'do':
          room = input('Room number: ')
         if (room == '201'):
           print_dramatic_text('You are in Art room!')
           roll = random.randint(1,20)
           draw_d20(roll)
           if roll == 6:
              print_dramatic_text('win!')
         if (room == '100'):
             print_dramatic_text('A ghost came to kiss you and have a crush on you! Leave the school with it!')
         else:
            skull = '\U0001F480'
            print_dramatic_text(skull +'YOU LOST')





    elif(room == '201'):
     print_dramatic_text('You enter the art room ...')
     roll = random.randint(1,6)
     draw_d6(roll)
     if roll <= 2:
      room = input('Room number: ')
      if (room == '302'):
               print_dramatic_text('You are in Art room!')
               roll = random.randint(1,4)
               draw_d4(roll)
               if roll == 4:
                 print_dramatic_text('WIN!!')
      if (room == '100'):
             print_dramatic_text('A ghost came to kiss you and you win!')
        
      if roll > 2:
         print_dramatic_text('You go to the dungeon! Answer this easy question to go back!')
         print_dramatic_text('What are the three basic clors in art? Red, blue and?')
         if player.role == 'artist':
            print_dramatic_text('HINT: y')
         else:
            print_dramatic_text('Do you want to get buffs?')
            print_dramatic_text('Yes or no?')
            choice = input('Choice: ')
            if choice == "yes" or "Yes":
              player.strength += 1
              player.print_character_sheet()
              print_dramatic_text('You sucessfully break the art color box! It is yellow!')
            else: 
               print_dramatic_text('LOST!')
         answer =input ('Answer: ')
         if answer == 'yellow' or 'Yellow':
            room = input('Room number: ')
            if (room == '302'):
               print_dramatic_text('You are in Art room!')
               roll = random.randint(1,4)
               draw_d4(roll)
               if roll == 4:
                 print_dramatic_text('WIN!!')
            if (room == '100'):
             print_dramatic_text('A ghost came to kiss you and have a crush on you! Leave the school with it!')
         else:
            skull = '\U0001F480'
            print_dramatic_text(skull +'YOU LOST')



      
           
    elif(room == '100'):
        print_dramatic_text('You enter the principal\'s office ...')
        roll = random.randint(1,4)
        draw_d4(roll)
        if roll <= 2:
         room = input('Room number: ')
        if roll > 2:
         print_dramatic_text('You go to the dungeon! Answer this easy question to go back!')
         print_dramatic_text('Ghost kiss you?')
         if player.role == 'staff member':
            print_dramatic_text('win, you gain the love from the office')
         else:
            print_dramatic_text('Do you want to get buffs?')
            print_dramatic_text('Yes or no?')
            choice = input('Choice: ')
            if choice == "yes" or "Yes":
              player.strength += 1
              player.print_character_sheet()
              print_dramatic_text('You sucessfully break the art color box! Ghost has a crush on you !')
            else: 
               print_dramatic_text('LOST!')
         

    else:
        print_dramatic_text('You did not enter a valid room number ... you go to the dungeon!')


    skull = '\U0001F480'
    print_dramatic_text(skull + ' you have no choice')
    


