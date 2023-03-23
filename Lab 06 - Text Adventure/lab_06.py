class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# not in class!
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Bedroom 2 - 0 - (description, north, east, south, west)
    room = Room("You are in the second bedroom, there is "
                "a door to the east.", 5, 1, None, None)
    room_list.append(room)
    south_hall = Room("You are in the south hall, there is door to the east"
                      " a door to the west and a hall to the north", 4, 2, None, 0)
    room_list.append(south_hall)
    kitchen = Room("You are now in the kitchen, there is a door to the north and"
                   " a door to the west.", 3, None, None, 1)
    room_list.append(kitchen)
    living_room = Room("You are the living room, there is a door to the north, west and"
                       " south.", 7, None, 2, 4)
    room_list.append(living_room)
    north_hall = Room("You are in the north hall there is hall to the south a door"
                      " to the west and a door to the east.", None, 3, 1, 5)
    room_list.append(north_hall)
    master_room = Room("You are in the Master bedroom you a door to the north, east "
                       "and a door to the south.", 6, 4, 0, None)
    room_list.append(master_room)
    garage = Room("You are in the garage there is a door to the south,"
                  , None, None, 5, None)
    room_list.append(garage)
    man_cave = Room("You are in the man cave and you have a door to the south"
                    ".", None, None, 3, None)
    room_list.append(man_cave)
    # add rest of rooms

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south

        # add other directions
        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        else:
            print("Please pick a valid direction.")
            continue

        # check for valid choice
        if next_room == None:
            print("You can't go that way!")
            continue

        # if all is well, set new room
        current_room = next_room

main()