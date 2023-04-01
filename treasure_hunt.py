import time

# Introduction to the games and rules
print('A small treasure hunt for you :P')
print('Instructions: You will always be facing IIM.')
print('         w (up)')
print(' a(Left) s (down) d(right)' )
print('\n I will change the position with the messages to make it more clear.\n')

print('---------------------------------------------------------------------------------')

# Defining lists for each road of the map.
# The positions 1,2,3,4 hold the positions for the roads it leads when we go forwards, left, right and back.
# For example, we are at road0 and we press 'W'. We check the 1st position which is None - this means going forward from road0 is not possible.
# Other example, we are at road0 and we press 'A'. We check the 2nd position which is 17 - this means going left (A) from road0 leads to road17.
# Similary for 'D' we reach road1 and for 'S' we go to road27.
# This is the way the map is designed. In my case I needed 34 roads to develop my map. 
# The 0th of list is the message about the location which is displayed whenever that specific location is reached.
# The other fields are used for the clues to go next location.
# Position 5 stores the clue number for that location. If reached correctly, position 6 has the message for next location.
# Road34 in my case is the final location which haves other fields to put on an addition test on the user. 

VNIT_list = {}
road0=['You are infront of Chemical Department watching the construction', None, 17, 1, 27, None, 0, None]
road1=['You are near canteen', 3,0,31,2,None,0,None]
road2=['You reached COP', 1,None,None,None,None,0,None]
road3=['You can see the matereials department at left and meta department to your right',4,None,28,1,None,0,None]
road4=['You reached canara bank', 7,5,19,3,None,0,None]
road5=['-*-The Auditorium-*-',6,30,4,None,None,0,None]
road6=['-*-Nescafe-*-', 10,12,7,5,None,0,None]
road7=['Seems like you are in some kind of a main square. Acad section is to your right.',9,6,8,4,None,0,None]
road8=['Your near Acad section and behind you is our spot <3',None,7,20,34,6,'A morning in the woods',None]
road9=['The Architecture department looks abandoned', None,10,None,7,None,0,None]
road10=['Electronics Dept', None,11,9,6,None,0,None]
road11=['Computer Science Department',None,None,10,12,None,0,None]
road12=['Your reached library',11,13,6,None,None,0,None]
road13=['You are near the tennis court junction',29,14,12,17,None,0,None]
road14=['Standing at the Y-Junction',None,15,13,None,None,0,None]
road15=['You are near the Ground',None,16,14,33,None,0,None]
road16=['Girls Hostel',32,None,15,None,None,0,None]
road17=['You are in HC road walking towards library',13,18,0,None,None,0,None]
road18=["You get into some desolated area filled with dried up trees",None,None,17,None,7,'"Sab se pyaari teri soorat, pyaar hai bas tera pyaaar heeee" with customary white dresses',None]
road19=['Taana na tana na na Dept',20,4,None,None,None,0,None]
road20=['You are behind the main building',25,8,21,19,None,0,None]
road21=['Inside the main building',None,20,22,None,None,0,None]
road22=['You are in front of the main building',23,21,26,None,8,'Goood Going. Next "Chain Cut ... Chain cut ":P :P :D',None]
road23=['ELECTRICAL DEPT B|',None,25,24,22,None,0,None]
road24=['The Parking seems totally empty',None,23,None,26,11,'You keep walking into the parking and as you go deep in, you see it all lightened up with candles decorated with balloons all over. \nAll of your friends are waiting for you and start shouting and singing the Happy birthday Song to you. \n Happy birthday to you Geeeettt :D :D \n Nikhila comes to you, hugs and wished you and vaguely says "Such weird nickname yet cute, insect Girl! "\n \n You cut the cake, talk , play , dance for so long. They all wish you again and disperse. \n You get all joyful, happy but something is missing.\n You did not see me yet',None]
road25=['CIVIL DEPT', None,None,23,20,None,0,None]
road26=['PLANE',24,22,None,None,None,0,None]
road27=['you are in chemical department',0,None,None,None,1,'You see Nikita and ask for your cycle keys\n Nikita:I gave your cycle to Sneha. \n Her class starts soon so go fast and get your keys.',None]
road28=['You are inside META Dept',None,3,None,None,2,'Sneha stands near the water cooler. You get the keys and leave to your hostel as mess would be closed in 5 mins',None]
road29=['You entered the tennis court',None,None,None,13,5,'All deserted you see nothing in the tennis court. \n Almost about to leave, you happen to see a water bottle. You pick it up and find a piece of paper in it. \n It reads "In this Motors are used to take water from one level to a higher one , clearing all obstacles so that water moves the turbine creating electricity." ',None]
road30=['The audi is all empty',None,None,5,None,10,'You sit for a while finding nothing\n \n Suddenly hundreds of ballons start flying beside you.\n The projector in the audi starts and the slide shows "How long? We all are waiting for you over here, Come fast"',None]
road31=['You entered the canteen',None,1,None,None,4,'After eating fried rice you see ghanta aproaching you.\n Seeming unusual he says "The first time you and molu ever met/hanged out or whatever you want to call it"',None]
road32=['You get into your hostel',None,None,None,16,3,'You were late to the mess and you are hungry like hell.Not eating is not an option',None]
road33=['The ground is all packed up',15,None,None,None,9,'4 Years\n4 nights\n2000 people dancing and shouting <3',None]
road34=['The canara bank is being loaded so no one is allowed to stay there',8,None,None,None,12,'The box is closed. Oh wait it seems like it has a passcode. What do you think it is?',None,'lizzy','\n You have opened the box.\n In it you see 23 roses amongst them 21 are red and 2 are yellow..(you must know the analogy :P) \n Also the pillow for your heart and a better earphone so that you would talk to me properly :P \n \n In the darkness you see a shadow coming... and there you go to hug him <3']

# Defining the whole map as a dictionary. 
VNIT_list =[ road0, road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11,
            road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22,
            road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33,
            road34]

done = False    # Used to check if the clip is completed or not.
current_room=0  # Starting point or road of the game.
next_room=1     
clue_flag=1     # You start with 1 and whenever clue is reached we can add it

# Constraints to the player playing regarding the map.
print('****Welcome back to VNIT***** !!')
print('The road backside of ECE and Tennis court is blocked due to construction ')
print('Girls are strictly not allowed anywhere close to boys hostel. The maximum you can go is to cop')
print('Type End whenever you want to exit')
print('-----------------------------------------------------------------------------------------------------')


while not done:
    print("\n")
        
    print(VNIT_list[current_room][0])    # Printing the message of the location of the room
    
    print(clue_flag)                     # The clue number is printed to see how further they are in the game.

    if (VNIT_list[current_room][5] == clue_flag):         # To check if they have reached the correct location to go further in the game.  
        print ('\n')
        print(VNIT_list[current_room][6])                 # If yes, then the clue for the next location is given here.
        if VNIT_list[current_room][5] == 12:              # Checking if they have reached the last clue location after completing previous 11 clues.
            done_a = False                                # Further check for the last clue.
            while not done_a:
                time.sleep(0.5)
                x = input("Type in the pass code! ")      # Final passcode is asked to complete the game.
                if ( x.lower() == VNIT_list[current_room][8].lower()):          # If passcode is entered successfully then, print the final message.
                    time.sleep(1)       
                    print(VNIT_list[current_room][9])
                    time.sleep(4)
                    print('------------------------------------------------------')

                    print('*** Congratulations madam*** \n You have completed the game :P \n A Happy Happy birthday Lizzy <3 :* :*')
                    print('A tiny attempt  to make you reminisce. This is not as great as I wanted it to be but my programming skills are way too deficient :P')
                    print('Anyway... Happy Happy birthday... I hope you enjoyed it a bit atleast xP')
                    print('Love you loads. \n Hugs and kisses :D :D')

                    done_a = True                         # Making it true to end the loop after completion.

        clue_flag += 1                                    # Adding the clue_flag after the current clue location is reached.
        
        if clue_flag == 13:                         # All the if clauses are used to change the messages of location after the clue location are reached. 
            done = True
        if clue_flag == 3 :
            road28[0] =  'You are inside META Dept and it is all engaged with extra classes.'
            VNIT_list[current_room][5] = 0
        if clue_flag == 2 :
            road27[0] = 'There is no one in your department.'
            VNIT_list[current_room][5] =0
        if clue_flag == 4 :
            road32[0] = "Empty Hostel. Everyone's busy roaming around in campus. Even you go roam around mistress"
            VNIT_list[current_room][5] =0
        if clue_flag == 5 :
            road31[0] = 'Canteen is closed.'
            VNIT_list[current_room][5] =0
        if clue_flag == 6 :
            road29[0] = 'You entered the tennis court and there is nothing to do in tennis court.'
            VNIT_list[current_room][5] =0
        if clue_flag == 10 :
            road33[0] = 'Ground is vacant. Sparta is sleeping near the gate. You would not want to disturb him.'
            VNIT_list[current_room][5] =0
        if clue_flag==12:
            VNIT_list[current_room][0] = "The feels are back, aren't they? \n It's all dark, breezy. Eyes looking for someone and then you see a box."  
        if current_room == 7 :
            road7[6] = '********************\n :D :D :D :D :D \n :P :P :P :P :P\n****************************'
            VNIT_list[current_room][5] = 11
    #	clue_flag += 1

    dir = input('Where do you want to go?')                    # Asking the user to give the input w, a, s, d.

    # Navigating the map.
    # Depending on the input, the next road is reached by the following if clauses.

    if dir.lower() == 'w':
        next_room = VNIT_list[current_room][1]
        if next_room == None:
            print('\n You cant go there.')
            time.sleep(0.5)
        else:
            current_room = next_room
    
    elif dir.lower() == 'a':
        # type code to go left
        next_room = VNIT_list[current_room][2]
        if next_room == None:
            print('\n You cant go there.')
            time.sleep(0.5)
        else:
           current_room = next_room
    
    elif dir.lower() == 'd':
        # type code to go right
        next_room = VNIT_list[current_room][3]
        if next_room == None:
            print('\nYou cant go there.')
            time.sleep(0.5)
        else:
            current_room = next_room
    
    elif  dir.lower() == 's':
        # type code to go south
        next_room = VNIT_list[current_room][4]
        if next_room == None:
            print('\nYou cant go there.')
            time.sleep(0.5)
        else:
           current_room = next_room
    
    elif dir.lower() == 'end':                          # Ending the game if user enters end
        print('HAPPY HAPPY HAPPY BIRTHDAY GEETU. Try until you complete the game :P ')
        done = True

    else:                                               # Message to print if any other input is provided.
        print('Sorry, Please choose from the given directions. Just like Joey says to Chandler "Choose!! You Jackass xP"')

print('-----------------------------------------------------------------------------------------------------------------------')
x = input("Press a key to quit")