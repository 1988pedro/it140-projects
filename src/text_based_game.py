# Anayo Pedro Okafor
# IT-140 Project Two: Text-Based Adventure Game

def show_instructions():
    """Displays the game instructions, rules, and available commands."""
    print("=" * 55)
    print("        WELCOME TO THE FANTASY ADVENTURE GAME!        ")
    print("=" * 55)
    print("Collect all 6 items to win the game, or face the villain.")
    print("Commands:")
    print("  go [direction]  (e.g., go north, go south, go east, go west)")
    print("  get [item name] (e.g., get Sword)")
    print("  exit            (Quit the game)")
    print("-" * 55)

def show_status(current_room, inventory, rooms):
    """Displays the player's current status, inventory, and visible items."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    
    # Check if there is an item in the current room
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        print(f"You see a {item}")
    print("-" * 35)

def main():
    # Define the dictionary linking rooms to other rooms and items
    rooms = {
        'Great Hall': {'south': 'Bedroom', 'north': 'Dungeon', 'east': 'Kitchen', 'west': 'Library'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar', 'item': 'Armor'},
        'Cellar': {'west': 'Bedroom', 'item': 'Helmet'},
        'Library': {'east': 'Great Hall', 'item': 'Spellbook'},
        'Kitchen': {'west': 'Great Hall', 'south': 'Dining Room', 'item': 'Key'},
        'Dungeon': {'south': 'Great Hall', 'east': 'Gallery', 'item': 'Sword'},
        'Gallery': {'west': 'Dungeon', 'item': 'Shield'},
        'Dining Room': {'north': 'Kitchen', 'item': 'Dragon'}  # Villain room
    }
    
    # Track the player's starting room and inventory
    current_room = 'Great Hall'
    inventory = []
    total_items_to_win = 6

    # Display instructions at the start of the game
    show_instructions()

    # Gameplay loop
    while True:
        # Show player status (room, inventory, room item)
        show_status(current_room, inventory, rooms)

        # Prompt the player for input
        player_input = input("Enter your move: ").strip()

        # Handle exit command
        if player_input.lower() == 'exit':
            print("Thank you for playing! Goodbye.")
            break

        # Split input into command and argument/direction
        command_parts = player_input.split(maxsplit=1)
        
        if not command_parts:
            print("Error: Please enter a command.")
            continue

        action = command_parts[0].lower()

        # Handle 'go' movement commands
        if action == 'go':
            if len(command_parts) < 2:
                print("Error: Specify a direction (e.g., go north).")
                continue
            
            direction = command_parts[1].capitalize()  # Capitalize direction to match dictionary keys if needed, or keep lowercase depending on setup
            # To be safe with lowercase direction entries:
            direction = command_parts[1].lower()
            # Map standard inputs to capitalized room keys if keys use capitalization, 
            # or check valid dictionary directions:
            
            # Let's check keys in rooms[current_room] directly
            # Note: directions in our dictionary are lowercase strings like 'south', 'north'
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                
                # Check if the player entered the villain's room
                if rooms[current_room].get('item') == 'Dragon':
                    print(f"\nYou are in the {current_room}")
                    print("NOM NOM... GAME OVER! The dragon got you!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break
            else:
                print("Error: You can't go that way! Invalid direction.")

        # Handle 'get' item commands
        elif action == 'get':
            if len(command_parts) < 2:
                print("Error: Specify an item to get (e.g., get Sword).")
                continue
            
            item_requested = command_parts[1]

            # Check if room has an item and if it matches the requested item (case-insensitive check)
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_requested.lower():
                item_to_add = rooms[current_room]['item']
                
                # Check if item is already in inventory to avoid duplicates
                if item_to_add not in inventory:
                    inventory.append(item_to_add)
                    print(f"You picked up the {item_to_add}!")
                    # Remove the item from the room so it can't be picked up twice
                    del rooms[current_room]['item']
                    
                    # Check win condition: 6 items collected
                    if len(inventory) == total_items_to_win:
                        print("\n" + "=" * 55)
                        print("Congratulations! You have collected all items and defeated the dragon!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        print("=" * 55)
                        break
                else:
                    print("You already have this item in your inventory.")
            else:
                print(f"Error: There is no {item_requested} in this room.")
        else:
            print("Error: Invalid command format. Use 'go [direction]' or 'get [item]'.")

if __name__ == "__main__":
    main()
