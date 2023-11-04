rooms = {
        "Harvelle's Roadhouse": {'South': 'The Chapel','East':"Bobby's House"},
        'The Chapel': {'North':"Harvelle's Roadhouse", 'East': "God's Bar", 'West':'Hotel Room','South':'The Parking Garage'},
        "Bobby's House": {'West': "Harvell's Roadhouse"},
        'Hotel Room':{"East":"The Chapel"},
        'The Bunker':{"South": "Gods Bar"},
        "God's Bar":{"West":"The Chapel", "North":"The Bunker"},
        'The Parking Garage':{"North":"The Chapel", "East": "Hell"}, 
        'Hell':{"West":"The Parking Garage"}
        
    }
  
inventory=[]
item=["salt", "holy oil", "the amulet", "sawed off shot gun", "the book of the damned", "the colt", "the demon blade"]
   
def allinv():
    if inventory==item:
        print("You have found all the items. Please go to hell. While there, take care of Aboddon")


def Start():
    print("Welcome to Supernatural: Stuck in a Text Based Game. Help Sam and Dean defeat Abaddon! They have been trapped in a text based game! Go through all the rooms and collect all the objects to help beat Abaddon and meet Sam and Dean in hell!!! Hurry there isn't much time! To start the game, type start. To exit at any time type Exit.")
    direction=['Start']
    player_input=input('Please choose Start or Exit')
    if player_input == 'Start':
        harvelle()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def harvelle():
    print('Your current room is the famous Harvelles Roadhouseouse owned and operated by Ellen Harvelle and her daughter Jo Harvelle!')
    direction=['South','East','Exit']
    player_input=input("Here you can obtain salt! obtain salt? yes/no?") 
    if player_input=="yes":
        newitem="salt"
        inventory.append(newitem)
        print(f"Your current inventory consists of {inventory}.")
    else:
        print("You do not obtain the salt")
    allinv()
    player_dirinput=input( "To the East lies Bobby's House, and to the South lies The Chapel. Please choose East or South")
    if player_input == "East":
        bobby()
    elif player_input == "South":
        chapel() 
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def chapel():
    print('You find yourself in a beautiful chapel with big stain glass windows and long dark wooden pues.')
    direction=['South','East','Exit','North','West']
    player_input=input("Here you can obtain holy oil! To the South lies The Parking Garage, to the East is where God's Bar is, to the North you can find Harvell's Roadhouse and to the West you can go to The Hotel Room. Please choose North, South, East or West")
    if player_input == "South":
        parking()
    elif player_input == "North":
        harvelle()
    elif player_input == "East":
        god()
    elif player_input == "West":
        hotel()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def bobby():
    print("You find yourself in Bobby's old house located in a scrap yard that Bobby owns")
    direction=['West', 'Exit']
    player_input=input("Here you can obtain 'The Book of the Damned' To the West is Harvelle's Roadhouse. Please choose West.")
    if player_input == "West":
        harvelle()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def hotel():
    print("You find yourself in Sam and Deans hotel room. There are two beds and an old tv against the wall")
    direction=['East', 'Exit']
    player_input=input("Here you can obtain Dean's amulet! To the East is The Chapel. Please choose East.")
    if player_input == "East":
        chapel()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def bunker():
    print("You find yourself in The Men of Letter's secret hide out; The Bunker")
    direction=['South', 'Exit']
    player_input=input("Here you can obtain 'The Colt'! To the South is Gods Bar. Please choose South.")
    if player_input == "South":
        god()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def god():
    print("You find yourself in God's hide out,  God's Bar, It's small and dark with a small stage")
    direction=['West', 'North', 'Exit']
    player_input=input("Here you can obtain The Demon Blade! To the West is The Chapel and to the North is the Bunker. Please choose West or North.")
    if player_input == "West":
        chapel()
    elif player_input == "North":
        bunker()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def parking():
    print("You find yourself in an empty parking garage where you see Dean's 1967 Chevy Impala")
    direction=['East', 'North', 'Exit']
    player_input=input("Here you can obtain Dean's sawed off shotgun! To the East is Hell and to the North is The Chapel. Please choose East or North.")
    if player_input == "East":
        hell()
    elif player_input == "North":
        chapel()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def hell():
    print("You've Made it to Hell.")
    direction=['East', 'Exit']
    player_input=input("You've made it to hell, Think you can defeat Aboddon? East is The Parking Garage. Please choose East.")
    if player_input == "East":
        parking()
    elif player_input == 'Exit':
        exit()
    else:
        print('Invalid choice. Please try again')
def exit():
    print('Thank you for playing')
    quit()
if __name__ == "__main__":
    while True:
        Start()






