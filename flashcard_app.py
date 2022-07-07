import random

# flashcars app

key_signature =[('key of G', '''
------#
-------
-------
-------
-------'''),
('key of A', '''
    #
#
  #
'''),]

full_deck = [("a","b"),("c","d"), (key_signature[0]), (key_signature[1])]


# display_front = input()
other_side =  ''

old_pile =  [] # done memorizing  these cards for the session
current_pile = [] # the pile you are working on memorizing
current_card = ()

# press key to show other side

# menu: press <> to show other side.   press <> to move item to old pile . press <> to add new card
# if key is pressed put into archive pile

def get_new_card(full_deck):
    new_card = random.choice(full_deck)
    while new_card in current_pile:
        new_card = random.choice(full_deck)
    current_pile.append(new_card)
    return new_card

def get_next_card(current_pile):
    next_card = random.choice(current_pile)
    return next_card

def menu():
    global current_card
    if len(current_pile) == 0:
        print("\n No cards in the pile")

    choice = input("""
    Press the space bar to show other side.  
    Press 'o' to move card to the old pile. 
    Press 'n' to add a new card to the current pile. 
    Press 'x' to view the next current card.  
    Press 'q' to quit. """)
    if choice == ' ': # show other side
        global other_side
        if other_side == current_card[0]:
            other_side = current_card[1]
        else:
            other_side == current_card[1]
            other_side = current_card[0]
        print("\n This is the other side: ", other_side, "\n")
        menu()
    elif choice == 'x':
        if len(current_pile) == 0:
            print("\n No cards in the pile")
            menu()
        else:
            current_card = get_next_card(current_pile)
            other_side = current_card[0]
            print("\n This is the current card: ", current_card[0], "\n")
            menu()

    elif choice == 'o': # move to old pile
        old_pile.append(current_card)
        current_pile.remove(current_card)
        menu()
    elif choice == 'n': # add new card
        if len(current_pile) == len(full_deck):
            print("\n All cards in the deck have been added to the current pile")
        else:
            new_card = get_new_card(full_deck)

            current_pile.append(new_card)
            print("\n This is the new card: ", new_card[0], "\n")
            current_card = new_card
            other_side = current_card[0]  # set other side to front of card
        menu()
    elif choice == 'q':
        quit()
    else:
        print("invalid input")
        menu()
menu()

#TODO:  find out why the not all cards getting added to the current pile
