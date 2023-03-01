#Ethan Martindale

#Global variables/dictionary for all functions to access with ease.
current_room = 'Great Hall'
Inventory = []
commands = ['go North', 'go South', 'go East', 'go West', 'get Item']
rooms = {
        'Great Hall' : {'North': 'Living Room', 'West': 'Master Bedroom', 'Item': 'None'},
        'Master Bedroom' : {'East': 'Great Hall', 'West': 'Bathroom', 'Item': 'Anti-Demon Sword'},
        'Bathroom' : {'East': 'Master Bedroom', 'Item': 'Cross'},
        'Living Room' : {'North': 'Garden', 'South': 'Great Hall', 'East': 'Hidden Library', 'West': 'Kitchen', 'Item': 'Lighter'},
        'Garden' : {'South': 'Living Room', 'Item': 'Sage'},
        'Kitchen' : {'East': 'Living Room', 'Item': 'Salt'},
        'Hidden Library' : {'South': 'Basement', 'West': 'Living Room', 'Item': 'Book of Banishment'},
        'Basement' : {'North': 'Hidden Library', 'Item': 'Demon'}#Villian awaits players arrival.
    }

#Introduction to game and win/lose conditions.
def instructions():
    print('-' * 100)
    print('Demon Mansion Madness, a Text Adventure Game')
    print('Collect 6 items to banish the demon and save your friend held captive in his manor!')
    return('')

#Rules state how to play and will appear again for player if they input invalid commands.
def rules():
    print('Move commands: go North, go South, go East, go West')
    print('Add to Inventory: get Item')
    return('')

#function called on to give room and possible item description to player before action is taken.
def gameplay():
    print('-' * 100)
    #Descriptions and possible directions are given to player based on the current room they are in.
    if current_room == 'Hidden Library':
        print('You wander through an illusion of a wall, stumbling in a room filled with floating candles and shelves of many books.')
        print('You sense a dark presence nearby...\n')
        #Gives extra description of item if not yet picked up by player.
        if rooms[current_room]['Item'] != 'None':
            print('You see a Book of Banishment\n')
    elif current_room == 'Living Room':
        print('You walk into a great room filled with fancy furniture to relax on.\n')
        if rooms[current_room]['Item'] != 'None':
            print('You see a lighter nugded between the cushions\n')
    elif current_room == 'Garden':
        print('A beautiful garden of many plants are sprouting here.')
        print('The way back in lies to the south.\n')
        if rooms[current_room]['Item'] != 'None':
            print('You see some Sage growing in the garden.\n')
    elif current_room == 'Kitchen':
        print('An unfinished chicken dinner sits coldly on the counter.\n')
        if rooms[current_room]['Item'] != 'None':
            print('Some salt lies next to the chicken\n')
    elif current_room == 'Master Bedroom':
        print('An impressively big room is left in complete disaster, everything a mess.\n')
        if rooms[current_room]['Item'] != 'None':
            print('A sharp looking sword lies on the bed.\n')
    elif current_room == 'Bathroom':
        print('An impossibly golden bathroom awaits your admiration.\n')
        if rooms[current_room]['Item'] != 'None':
            print('A cross hangs on the wall.\n')
    elif current_room == 'Great Hall':
        print('From the front door awaits a corrider with many unique paintings and statues aligned across the walls.\n')

    return('')

#Function for start point of game and input of actions by player.
def game():
    global rooms
    global current_room

    gameplay()
    print('You are in the', current_room)
    print('Inventory:', Inventory)
    action = input('What do you do?:\n>')
    #Checks commands list when player inputs action to determine if valid. If not valid, player is reminded of valid commands.
    if action not in commands:
        print('-' * 100)
        print('Invalid action! Your options are as follows:')
        print(rules())
    elif action in commands:
        #Splits input to drop go/get and find room/item in dictionary with the second word.
        split_action = action.split()[1]
        if split_action != 'Item':
            if split_action in rooms[current_room]:
                current_room = rooms[current_room][split_action]
            elif split_action not in rooms[current_room]:
                print('-' * 100)
                print('The path is blocked!\n')
        else:
            #Both if statements check if able to pick up item and tell player of results.
            if rooms[current_room]['Item'] != 'None':
                print('-' * 100)
                print('You picked up the {}'.format(rooms[current_room]['Item']))
                Inventory.append(rooms[current_room]['Item'])
                rooms[current_room]['Item'] = 'None'
            else:
                print('-' * 100)
                print('There is nothing to pick up!')

#Calls functions to introduce player to game and how to play before starting loop.
print(instructions())
print(rules())

#Infinite loop to start game until player reaches the Basement room with the boss.
while True:
    game()
    if current_room == 'Basement':
        #If all 6 items are in inventory, the game is won else it will be game over!

        if len(Inventory) == 6:
            print('-' * 100)
            print('Walking down into the darkness awaits a terrible demon. The creature springs into action towards you!')
            print('With the protection of the gathered items, you fight back to weaken the demon.')
            print('Before it can escape, you successfully banish the demon with your remaining items. The demon is no more!')
            print('You free your friend from a cage in the corner, they thank you before replying,')
            print('"That`s the last time I summon a demon to do my chores!".\n')
            print('You Win!')
            break
        else:
            print('-' * 100)
            print('Walking down into the darkness awaits a terrible demon. The creature springs into action towards you!')
            print('You fight back the best you can, but what you have is not enough to stop the demon...\n')
            print('Game Over!')
            break

print('Thank you for playing!')

#Keeps program running to not close game immediately when opened in command prompt.
input()