# Game introduction
print("Welcome to the adventure!")
print("You are on a path leading up a mountain.")

# Player choice 1
choice1 = input("Do you want to go up the mountain or back down? Type 'up' or 'down'")

if choice1 == "up":
    # Continue story up the mountain
    print("You continue up the mountain path. It starts to get very cold.")

    # Next choice
    choice2 = input("Do you want to continue up the mountain or go back 'down'?")

    if choice2 == "up":
        # Finish story
        print("You reach the top of the mountain! You made it to the summit!")
    elif choice2 == "down":
        print("You decide to go back down the mountain to stay warm.")
    else:
        print("Invalid choice. Game over.")

elif choice1 == "down":
    print("You go back down the mountain to the base.")

else:
    print("Invalid choice. Game over.")


# Game classes

class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.stamina = 100
        self.inventory = []

    def change_health(self, amount):
        self.health += amount

    def change_stamina(self, amount):
        self.stamina += amount


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.characters = []
        self.items = []

    def add_character(self, character):
        self.characters.append(character)

    def get_details(self):
        print(self.name)
        print(self.description)
        print("Characters:")
        for c in self.characters:
            print(c.name)
        print("Items:")
        for i in self.items:
            print(i.name)


class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        print(self.name + ": " + self.description)

    def talk(self):
        if self.conversation is not None:
            print(self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(self.name + ": " + self.description)


# Game initialization
player = Player()
player.name = input("Enter your name: ")

location = Location("Mountain Base", "You are at the foot of a large mountain")
npc = Character("Wise Sage", "An old sage sitting in meditation")
location.add_character(npc)

# Main game loop
while True:

    print("\n")
    location.get_details()

    action = input("What do you want to do? ")
    if action == "talk":
        npc.talk()
    elif action == "climb":
        print("You start climbing the mountain...")

# And so on with more game logic and story...

# Additional locations

mountain_path = Location("Mountain Path", "A winding path up the mountain")
mountain_top = Location("Mountain Top", "The peak of the mountain with sweeping views")
old_ruins = Location("Ancient Ruins", "Crumbled ruins of an old temple")

# Connect locations
location.linked_locations = [mountain_path]
mountain_path.linked_locations = [location, mountain_top, old_ruins]

# Add items
sword = Item("Rusty Sword", "An old sword with some combat ability")
mountain_path.items.append(sword)

# Modify main loop
while True:

    # Existing logic to print location details

    action = input("What do you want to do? ").lower()

    if action == "talk":
        npc.talk()

    elif action == "climb":
        # Check if there's a linked location to climb to
        if location.linked_locations != []:
            location = location.linked_locations[0]
            print("You climb to the next area...")
        else:
            print("There is nowhere to climb!")

    elif action == "get" or action == "take":
        if location.items:
            item = location.items[0]
            print(f"You take the {item.name}")
            player.inventory.append(item)
            location.items.remove(item)
        else:
            print("There is nothing here you can take")

    elif action == "fight":
        if "sword" in player.inventory:
            print("You fight with your trusty sword!")
        else:
            print("You have no weapon to fight with!")

    elif action == "jump":
        print("You leap from the mountain top!")
        break  # Exit game loop

    else:
        print("I don't understand that command")

print("\nGAME OVER")
