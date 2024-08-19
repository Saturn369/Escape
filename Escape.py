import random
import os
import time
import keyboard
import threading

# Global variables
player_pos = (0, 0)
visited = set()
level = 1
bomb_pos, exit_pos, heart_pos, mana_pos, monster_pos = None, None, None, None, None
first_move = True
health = 9
mana = 9
attack = 3
defense = 3
monster_attack = 0
monster_defense = 0
monster_hp = 0
player_turn = True
event = threading.Event()

def create_level():
    global heart_pos, mana_pos, monster_pos
    grid_size = 4
    bomb_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    exit_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    
    while exit_position == bomb_position or exit_position == player_pos:
        exit_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    while bomb_position == player_pos:
        bomb_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    if random.choice([True, False]):
        heart_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        while heart_position == bomb_position or heart_position == exit_position or heart_position == player_pos:
            heart_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        mana_position = None
    else:
        mana_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        while mana_position == bomb_position or mana_position == exit_position or mana_position == player_pos:
            mana_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        heart_position = None

    monster_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    while monster_position == bomb_position or monster_position == exit_position or monster_position == player_pos or monster_position == heart_position or monster_position == mana_position:
        monster_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    return bomb_position, exit_position, heart_position, mana_position, monster_position

def print_grid():
    grid_size = 4
    for r in range(grid_size):
        row = ''
        for c in range(grid_size):
            if (r, c) == player_pos:
                row += 'P '
            elif (r, c) == monster_pos:
                row += 'M '
            elif (r, c) in visited:
                row += 'X '
            else:
                row += '. '
        print(row)
    print()

def print_status():
    print(f"Level: {level}")
    print(f"Health: {'♥' * health} {'-' * (9 - health)}")
    print(f"Mana: {'♦' * mana} {'-' * (9 - mana)}")
    print(f"Attack: ⚔ {attack}")
    print(f"Defense: 🛡 {defense}")
    print()

def display_intro():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("Welcome to the Depths of the Unknown...")
    print("\nInstructions:")
    print("Use 'W' to move up")
    print("Use 'S' to move down")
    print("Use 'A' to move left")
    print("Use 'D' to move right")
    print("Avoid the bomb and find the exit to proceed to the next level.")
    print("Watch out for monsters that may attack you.")
    print("\nPrepare yourself to venture into the abyss where sanity frays.")
    print("In this forsaken realm, a labyrinthine grid awaits, tainted by eldritch horrors.")
    print("A malevolent force has ensnared the exit, concealed amongst innocuous tiles.")
    print("The bomb lurks in the shadows, a grim harbinger of oblivion.")
    print("Survive the madness, uncover the secrets, and escape the clutches of the unknown...")
    print("\nPress any key to begin...")
    keyboard.read_event()  # Wait for any key press

def encounter_fountain():
    phrases = [
        "In the midst of despair, a flicker of vitality rejuvenates the weary soul, restoring hope.",
        "A pulse of life, thudding rhythmically, infuses strength into your weary heart.",
        "From the abyssal void, an ancient essence bestows upon you a surge of primordial vigor."
    ]
    print(random.choice(phrases))
    print("You found a Fountain of Life! Your health has increased by 1.\n")

def encounter_bomb():
    phrases = [
        "In the ruins of destiny, one must tread carefully lest the powder keg beneath the veil ignites.",
        "A sudden explosion, as if the heart of darkness itself had erupted with malevolent force.",
        "The eldritch horrors beneath the surface have unleashed their wrath, tearing reality asunder."
    ]
    print(random.choice(phrases))
    print("You stepped on a bomb! Your health has decreased by 1.\n")

def encounter_exit():
    phrases = [
        "Through reason and enlightenment, a path to salvation has emerged from the labyrinth.",
        "Amidst the shadows, a beacon of hope beckons, leading you out of the stygian depths.",
        "Beyond the veil of madness, an otherworldly portal opens, offering a fleeting escape."
    ]
    print(random.choice(phrases))
    print("You found the exit! Proceeding to the next level...\n")

def encounter_mana():
    phrases = [
        "A forbidden tome whispers secrets, filling you with arcane power.",
        "An ancient relic pulses with energy, replenishing your mana.",
        "From the void, an eldritch presence bestows you with newfound magical strength."
    ]
    print(random.choice(phrases))
    print("You found a mana source! Your mana has increased by 1.\n")

def encounter_monster():
    global player_turn, monster_attack, monster_defense, monster_hp, health, attack, defense

    # Initialize monster stats
    monster_attack = random.randint(1, 5)
    monster_defense = random.randint(1, 5)
    monster_hp = random.randint(5, 10)

    print("A monstrous creature emerges from the shadows!")
    print(f"Monster stats - Attack: {monster_attack}, Defense: {monster_defense}, HP: {monster_hp}")

    while monster_hp > 0 and health > 0:
        if player_turn:
            # Randomize player's attack each turn
            current_player_attack = random.randint(0, attack)
            # Randomize monster's defense each turn
            current_monster_defense = random.randint(0, monster_defense)
            
            print("Your turn to attack!")
            time.sleep(.3)
            damage = max(0, current_player_attack - current_monster_defense)
            monster_hp -= damage
            print(f"You dealt {damage} damage. Monster HP: {monster_hp}")
            time.sleep(.3)
            player_turn = False
        else:
            # Randomize monster's attack each turn
            current_monster_attack = random.randint(0, monster_attack)
            # Randomize player's defense each turn
            current_player_defense = random.randint(0, defense)
            
            print("Monster's turn to attack!")
            time.sleep(.3)
            damage = max(0, current_monster_attack - current_player_defense)
            health -= damage
            print(f"Monster dealt {damage} damage. Your Health: {health}")
            time.sleep(.3)
            player_turn = True

    if monster_hp <= 0:
        print("You defeated the monster!")
    elif health <= 0:
        print("The monster has defeated you!")
        return False  # Player lost, game over

    return True  # Player won

def play_game():
    global player_pos, bomb_pos, exit_pos, heart_pos, mana_pos, monster_pos
    global level, health, mana, attack, defense, first_move, visited

    while True:
        if first_move:
            # Initialize the level
            bomb_pos, exit_pos, heart_pos, mana_pos, monster_pos = create_level()
            player_pos = (0, 0)
            visited = set()
            first_move = False

        # Print the current game status
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print_status()
        print_grid()

        # Move player
        while True:
            if keyboard.is_pressed('w') and player_pos[0] > 0:
                player_pos = (player_pos[0] - 1, player_pos[1])
                break
            elif keyboard.is_pressed('s') and player_pos[0] < 3:
                player_pos = (player_pos[0] + 1, player_pos[1])
                break
            elif keyboard.is_pressed('a') and player_pos[1] > 0:
                player_pos = (player_pos[0], player_pos[1] - 1)
                break
            elif keyboard.is_pressed('d') and player_pos[1] < 3:
                player_pos = (player_pos[0], player_pos[1] + 1)
                break

        # Update the grid
        visited.add(player_pos)

        if player_pos == bomb_pos:
            encounter_bomb()
            health = max(0, health - 1)  # Decrease health but ensure it doesn't go below 0
            if health <= 0:
                if not ask_to_play_again():
                    return  # Exit the game loop
                else:
                    # Reset game state
                    player_pos = (0, 0)
                    visited = set()
                    level = 1
                    health = 9
                    mana = 9
                    attack = 3
                    defense = 3
                    first_move = True
                    continue  # Restart the game

        elif player_pos == exit_pos:
            encounter_exit()
            level += 1
            # Reset level elements
            bomb_pos, exit_pos, heart_pos, mana_pos, monster_pos = None, None, None, None, None
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            print_status()
            print_grid()
            first_move = True
            continue  # Move to the next level

        elif player_pos == heart_pos:
            encounter_fountain()
            health = min(9, health + 1)  # Increase health but max it out at 9
            heart_pos = None  # Ensure heart does not appear again this level

        elif player_pos == mana_pos:
            encounter_mana()
            mana = min(9, mana + 1)  # Increase mana but max it out at 9
            mana_pos = None  # Ensure mana does not appear again this level

        elif player_pos == monster_pos:
            if not encounter_monster():
                if not ask_to_play_again():
                    return  # Exit the game loop
                else:
                    # Reset game state
                    player_pos = (0, 0)
                    visited = set()
                    level = 1
                    health = 9
                    mana = 9
                    attack = 3
                    defense = 3
                    first_move = True
                    continue  # Restart the game

        # Clear the screen and print the updated game state
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print_status()
        print_grid()
        first_move = False

        # Short delay to prevent high CPU usage
        time.sleep(0.1)

def ask_to_play_again():
    global level
    while True:
        response = input("Do you want to play again? (y/n): ").strip().lower()
        if response == 'y':
            level = 1  # Reset level for a new game
            return True
        elif response == 'n':
            print("Thank you for playing!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    display_intro()
    play_game()
