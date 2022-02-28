import random

locations = ['New York', 'Los Angeles', 'Las Vegas', 'Milwaukee', 'Seattle']

eateries = ['The Sticky Menu Diner', 'Mama Mia Italian Ristorante', 'Le Terible Vegan Restaurant', 'The Meat Wagon', 'Shanghai Surprise' ]

modes = ['The Batmobile', 'Tauntaun', 'The USS Enterprise', 'TARDIS', 'That Huge Flying Dog-Thing From The Neverending Story']

shows = ['Wyld Stallyns', 'Sonic Death Monkey', 'Scrantonicity', 'Uptown Girl: An 80s Joel Experience', 'Drive Shaft']

def user_start (type):
    user_opt = str.upper(input(f'Please type (x) to randomly select {type} for your trip. '))
    while user_opt != 'X':
        print('Sorry, not a valid selection')
        user_opt = str.upper((input(f'Please type (x) to randomly select {type} for your trip. ')))

def sel_rand (list):
   random_sel = random.randint (0, len(list)-1)
   return list [random_sel]

def decide_init (list, selection, list_type, list_verb):
    decide_sel= str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect {list_type}, please type (r) '))
    while decide_sel != '':
        if decide_sel == 'R':
            selection = sel_rand(list)
            decide_sel = str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))
        else:
            print('Sorry, not a valid selection')
            decide_sel=str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))

    return selection

banner = ('***Powered by Radon Technologies (c) 2022  ****** WELCOME TO THE MARC CHERRIES TRIP PLANNER!****** Powered by Radon Technologies (c) 2022 ***')

print (banner)

while True:
    user_opt = user_start ('a LOCATION')

    loc_res = sel_rand(locations)
    
    loc_res = decide_init(locations, loc_res, 'a LOCATION', 'travelling to')
    
    
    user_opt = user_start ('an EATERY')
    
    eat_res = sel_rand(eateries)

    eat_res = decide_init(eateries, eat_res, 'an EATERY', 'dining at')

    
    
    user_opt = user_start ('a MODE OF TRANSPORTATION')
    
    mode_res = sel_rand(modes)

    mode_res = decide_init(modes, mode_res, 'a MODE OF TRANSPORTATION', 'using')
   
    
    
    user_opt = user_start ('ENTERTAINMENT')

    show_res = sel_rand(shows)

    show_res = decide_init(shows, show_res, 'ENTERTAINMENT', 'enjoying')

    
    input('Okay! Looks like you have made some nice selections today.  Let us recap, shall we? Please press ENTER to see a final readout of your selections.  Do not worry! You will have an opportunity to change your selections if needed.  ')
   
    print (f'LOCATION:                           {loc_res}')
    print (f'EATERY:                             {eat_res}') 
    print (f'MODE OF TRANSPORTATION:             {mode_res}') 
    print (f'ENTERTAINMENT:                      {show_res}') 
   
    restart = str.upper(input('Does everything look good to you?  If you are satisfied with these selections, please type (yes).  If you would like to START OVER, please type (restart)'))
    if restart != 'YES':  
        continue
    else:
        print (f'Congratulations! Your trip is all set. You will be travelling to {loc_res} by way of {mode_res} and chowing down on a fabulous meal at {eat_res}.  But the fun doesnt end there! You will cap the evening off with a private show preformed by none-other-than the legendary {show_res}! Have a great time!')
        break
    







