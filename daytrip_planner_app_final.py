import random

locations = ['SEATTLE', 'NEW YORK', 'LOS ANGELES', 'LAS VEGAS', 'MILWAUKEE']

eateries = ['Seattle Sticky Menu Diner', 'Seattle Mama Mia Italian Ristorante', 'Seattle Le Terible Vegan Restaurant', 'Seattle Meat Wagon', 'Seattle Shanghai Surprise', 'LA Hollywood Cafe', 'LA Taco Mal', 'LA Burger Bin', 'LA Vesuvio', 'LA Salads r Us', 'Vegas Strip Stakes', 'Vegas Vinnys', 'Vegas Lucky Dogs', 'Vegas Thai', 'Vegas Gyro', 'Milwuakee Wok', 'Milwaukee Beer and Some Food', 'Milwaukee Shake Shack', 'Milwaukee Fry Em Up', 'Milwaukee City Bar and Grill', 'New York Minute Fast Food', 'New York Seinfeld Deli', 'New York Capital Grille', 'New York Yan-Quiche', 'New York New York Pizza Pizza' ]

modes = ['The Batmobile (Seattle)', 'Tauntaun (Seattle)', 'The USS Enterprise (Seattle)', 'TARDIS (Seattle)', 'That Huge Flying Dog-Thing From The Neverending Story(Seattle)','The Batmobile(LA)', 'Tauntaun(LA)', 'The USS Enterprise(LA)', 'TARDIS(LA)', 'That Huge Flying Dog-Thing From The Neverending Story(LA)', 'The Batmobile(LV)', 'Tauntaun(LV)', 'The USS Enterprise(LV)', 'TARDIS(LV)', 'That Huge Flying Dog-Thing From The Neverending Story(LV)','The Batmobile(Milwaukee)', 'Tauntaun(Milwaukee)', 'The USS Enterprise(Milwaukee)', 'TARDIS(Milwaukee)', 'That Huge Flying Dog-Thing From The Neverending Story(Milwaukee)','The Batmobile(NY)', 'Tauntaun(NY)', 'The USS Enterprise(NY)', 'TARDIS(NY)', 'That Huge Flying Dog-Thing From The Neverending Story(NY)']

shows = ['Wyld Stallyns', 'Sonic Death Monkey', 'Scrantonicity', 'Uptown Girl: An 80s Joel Experience', 'Drive Shaft', 'Here Comes Treble', 'The Beets', 'This Is Spinal Tap', 'Timmy and the Lords of the Underworld', 'Dewey Cox', 'Scrantonicity II', 'Zack Attack', 'The Oneders', 'Vesuvius', 'Autobahn', 'The Commitments', 'Kathleen Turner Overdrive', 'The Rutles', 'Chris Gaines', 'Sparkle Nation', 'Limozeen', 'Dethklok', 'Scull Soup', 'Poverty Bomb', 'Blighted Daybreaker', 'Nerve Endings', 'Vespers']

def user_start (type):
    user_opt = str.upper(input(f'Please type (x) to randomly select {type} for your trip. '))
    while user_opt != 'X':
        print('Sorry, not a valid selection')
        user_opt = str.upper((input(f'Please type (x) to randomly select {type} for your trip. ')))
#I have a strange intuition that this return value is not necessary
    #return user_opt

def sel_rand (list):
   random_sel = random.randint (0, len(list)-1)
   return list [random_sel]

def sel_rand_by_city (list, range_min, range_max):
   random_sel = random.randint (range_min, range_max)
   return list [random_sel]   

def decide_init_first (list, selection, list_type, list_verb):
    decide_sel= str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect {list_type}, please type (r) '))
    while decide_sel != '':
        if decide_sel == 'R':
            selection = sel_rand(list)
            decide_sel = str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))
        else:
            print('Sorry, not a valid selection')
            decide_sel=str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))

    return selection

def decide_init (list, selection, list_type, list_verb):
    decide_sel= str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect {list_type}, please type (r) '))
    while decide_sel != '':
        if decide_sel == 'R':
            #selection = sel_rand_by_city(list)
            if loc_res == "SEATTLE":
                selection = sel_rand_by_city(list, 0, 4)
            elif loc_res == 'LOS ANGELES':
                selection = sel_rand_by_city (list, 5, 9)
            elif loc_res == "LAS VEGAS":
                selection = sel_rand_by_city(list, 10, 14)
            elif loc_res == "MILWAUKEE":
                selection = sel_rand_by_city(list, 15, 19)
            elif loc_res == "NEW YORK":
                selection = sel_rand_by_city(list, 20, 24)


            decide_sel = str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))
        else:
            print('Sorry, not a valid selection')
            decide_sel=str.upper(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please type (r) '))

    return selection

banner = ('***Powered by Radon Technologies (c) 2022  ****** WELCOME TO THE MARC CHERRIES TRIP PLANNER!****** Powered by Radon Technologies (c) 2022 ***')

print (banner)



#start of continuous loop to allow user to restart application
while True:
    user_opt = user_start ('a LOCATION')

    loc_res = sel_rand(locations)
    
    loc_res = decide_init_first(locations, loc_res, 'a LOCATION', 'travelling to')
    
    #first function starts new section
    #second function  selects a random option from list and stores it 
    #third function is a while loop prompting new choices until the user is satisfied
    
    user_opt = user_start ('an EATERY')

    if loc_res == "SEATTLE":
        eat_res = sel_rand_by_city(eateries, 0, 4)
    elif loc_res == 'LOS ANGELES':
        eat_res = sel_rand_by_city(eateries, 5, 9)
    elif loc_res == "LAS VEGAS":
        eat_res = sel_rand_by_city(eateries, 10, 14)
    elif loc_res == "MILWAUKEE":
        eat_res = sel_rand_by_city(eateries, 15, 19)
    elif loc_res == "NEW YORK":
        eat_res = sel_rand_by_city(eateries, 20, 24)

    eat_res = decide_init(eateries, eat_res, 'EATERY', 'dining at')


    
    
   

    
    
    user_opt = user_start ('a MODE OF TRANSPORTATION')
    
    if loc_res == "SEATTLE":
        mode_res = sel_rand_by_city(modes, 0, 4)
    elif loc_res == 'LOS ANGELES':
        mode_res = sel_rand_by_city(modes, 5, 9)
    elif loc_res == "LAS VEGAS":
        mode_res = sel_rand_by_city(modes, 10, 14)
    elif loc_res == "MILWAUKEE":
        mode_res = sel_rand_by_city(modes, 15, 19)
    elif loc_res == "NEW YORK":
        mode_res = sel_rand_by_city(modes, 20, 24)
   

    mode_res = decide_init(modes, mode_res, 'a MODE OF TRANSPORTATION', 'using')
   
    
    
    user_opt = user_start ('ENTERTAINMENT')

    if loc_res == "SEATTLE":
        show_res = sel_rand_by_city(shows, 0, 4)
    elif loc_res == 'LOS ANGELES':
        show_res = sel_rand_by_city(shows, 5, 9)
    elif loc_res == "LAS VEGAS":
        show_res = sel_rand_by_city(shows, 10, 14)
    elif loc_res == "MILWAUKEE":
        show_res = sel_rand_by_city(shows, 15, 19)
    elif loc_res == "NEW YORK":
        show_res = sel_rand_by_city(shows, 20, 24)

   

    show_res = decide_init(shows, show_res, 'ENTERTAINMENT', 'enjoying')

    
    
    input('Okay! Looks like you have made some nice selections today.  Let us recap, shall we? Please press ENTER to see a final readout of your selections.  Do not worry! You will have an opportunity to change your selections if needed.  ')
   
    print (f'LOCATION:                           {loc_res}')
    print (f'EATERY:                             {eat_res}') 
    print (f'MODE OF TRANSPORTATION:             {mode_res}') 
    print (f'ENTERTAINMENT:                      {show_res}') 
   
     #I tried but couldnt get a while loop to work here without it affecting the overall loop in a negative way and also had to comment out the else statement. I think it has something to do with the continue statement being in that block of code. If I define a function and call it will it somehow work better? I guess ill try
    restart = str.upper(input('Does everything look good to you?  If you are satisfied with these selections, please type (yes).  If you would like to START OVER, please type (restart)'))
    if restart != 'YES':  
        continue
    else:
        print (f'Congratulations! Your trip is all set. You will be travelling to {loc_res} by way of {mode_res} and chowing down on a fabulous meal at {eat_res}.  But the fun doesnt end there! You will cap the evening off with a private show preformed by none-other-than the legendary {show_res}! Have a great time!')
        break
    #else:
     #  print('not a valid selection, please try again')
      # restart = str.upper(input('Does everything look good to you?  If you are satisfied with these selections, please type (yes).  If you would like to START OVER, please type (restart) '))



 #the app works and does what it needs to do but there are several improvements I would make once I learn more

 #first I would make a seperate list for each city having its own restaurants and entertainment options.  This seems simple enough, though a few things I tried ran into problems

 #I would also make the option to restart only accept 'x' rather than any character, but this was stifled by my while loop issue on the restart block of code

 #I think there is still room to combine parts of code into one of the functions, or maybe even combine the rand_sel function and decide_init function into one

 #after testing it looks like if you restart the app it skips over the readout on the second go-around for some reason! need to work on this bug (update: bug fixed, had an epiphany while jogging.  I think a variable was being stored and on the second loop around it was forcing an if statement to evaluate incorrectly.  I simply removed the if statement and let the app continue on)
