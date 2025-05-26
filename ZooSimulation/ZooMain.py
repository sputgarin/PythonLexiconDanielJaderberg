# By Daniel Jäderberg
import Animals
from Visitors import Visitors
import random
from enum import Enum

class VisitorAction(Enum):
    FEED = 0
    LOOK = 1
    PET = 2
    WANDER = 3

class PlayerAction(Enum):
    FEED = "f"
    PLAY = "p"
    RELEASE = "r"
    DONE = "d"

day = 1
game_over = False
zoo_name = ""



visitor_pool = [
    Visitors("Pelle", 9, 50),
    Visitors("Linda", 33,20),
    Visitors("Olle", 55,60),
    Visitors("CyklonCrawX", 999,0),
    Visitors("Rutger", 12,70),
    Visitors("Märta", 75,35),
    Visitors("Rut", 66,100),
    Visitors("Kurt", 44,25),
    Visitors("Mizuki", 29,44)
]

def select_daily_visitors():
    return random.sample(visitor_pool, random.randint(2,4))


visitors = select_daily_visitors()

zoo = [
    Animals.Giraffe("Mr Tallneck", 5,10, 50),
    Animals.Lion("Mufasa! The Childhood trauma", 10,50, 50),
    Animals.Antilope("Antiprey", 12,50,50),
    Animals.Tiger("Shere Khan", 9,50,50)
    ]

def percentage_chance(chance):
    return random.randint(1,100) <= chance

def name_zoo():
    while True:
        zoo_name = input("Please input a innovative name for your Zoo that will awe-strike your visitors.\n").strip()
        if zoo_name:
            return zoo_name
        else:
            print("-----------------------------------------------------")
            print("That's not a valid name. Try something that contains actual characters or numbers.")
            print("-----------------------------------------------------")
def start_game():
    global zoo_name
    print("-----------------------------------------------------")
    print(f"Welcome to the first day of ZooSimulator!\n"
          f"Choosing animal care as your profession was \"obviously\" the right career path for you!")
    print("-----------------------------------------------------")
    zoo_name = name_zoo()
    print(f"Your Zoo is named: {zoo_name}\nThis will stand forever! Or until you restart the game...")

    print("-----------------------------------------------------")
    print(f"Here are your starting animals:")
    print("-----------------------------------------------------")
    for animal in zoo:
        print(
            f"Name: {animal.name}, Type: {animal.animal_type}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")


def during_night(zoo):
    print("-----------------------------------------------------")
    print("The animals get hungry during the night!")
    for animal in zoo:
        if animal.is_dead():
            continue
        animal.hunger -= 30
        animal.energy += 30
        animal.clamp_stats()

def day_start(zoo):
    print("-----------------------------------------------------")
    print(f"It's the start of day: {day}")
    daily_comment()
    visitor_status(visitors)

def daily_comment():
    global zoo
    if day == 2:
        print("So how is this life of monotonous animal care treating you? Are you bored yet?")
    if day == 3:
        print("All animals are equal but some pigs are more equal than others! Did i botch that?")
    if day == 4:
        print("Why are you doing this to yourself? This game obviously ends when all the animals are dead.")
        zoo.append(Animals.Penguin("Pinguh", 6, 50,50))
        last_animal = zoo[-1]
        print("-----------------------------------------------------")
        print(f"You have received a new animal! How fun...\n"
              f"A wild {last_animal.animal_type} appear, with the name: {last_animal.name} "
              f"Hunger: {last_animal.hunger} Happiness: {last_animal.happiness}.")

    if day == 5:
        print("Just release the carnivorous already! You know you want it!")
    if day == 6:
        print("Breaking the 4th wall am I? My goal is obviously to break down the walls of your zoo.")
    if day == 7:
        print("They are not animals... Just lines of text on your screen... Why do you care?")
    if day == 8:
        print("Reality is merely an illusion, albeit a very persistent one. Like the animals in your zoo!")
    if day == 9:
        print(
            "Just stop giving them food already... Starvation is just a concept... Just say they died of multiple organ failure.")


def zoo_personnel_interaction():

    global game_over
    done = False
    while not done:
        print("-----------------------------------------------------")
        player_choice = input(f"Please choose an interaction for your personnel: [F]eed, [P]lay,[R]elease, [D]one\n")
        if player_choice.lower() in [action.value for action in PlayerAction]:
            if player_choice == PlayerAction.FEED.value:
                for animal in zoo:
                    if animal.is_dead():
                        print(f"The animal {animal.name} is dead you can't feed a dead animal.")
                    elif animal.hunger >= 100:
                        print(f"The animal: {animal.name} is already full! Stop feeding it!")

                    else:
                        animal.hunger = min(100, animal.hunger + 10)
                        animal.energy -= 10
                        animal.clamp_stats()
                animal_status()

            if player_choice == PlayerAction.PLAY.value:
                for animal in zoo:
                    if animal.is_dead():
                        print(f"The animal {animal.name} is dead. You can't play a dead animal.")
                    elif animal.happiness >= 100:
                        print(f"The animal: {animal.name} is already happy enough! Stop bothering it!")
                    elif animal.energy <= 0:
                        print(f"The animal: {animal.name} is too tired to play! Stop bothering it!")
                    else:
                        animal.happiness += 10
                        animal.energy -= 10
                        animal.clamp_stats()
                animal_status()

            if player_choice == PlayerAction.DONE.value:
                done = True

            if player_choice == PlayerAction.RELEASE.value:
                print(f"You release all the animals who ravage the park, killing all the guests and each other.\n"
                      f"You will probably spend the rest of your life in a dark hole for doing this!\n"
                      f"GAME OVER!")
                game_over=True
                return

        else:
            print("Incorrect input! Try again!")


def visitor_interaction(zoo, visitors):
    global game_over
    print("-----------------------------------------------------")
    print(f"The visitors interacts with your animals:")
    print("-----------------------------------------------------")

    alive_animals = [animal for animal in zoo if not animal.is_dead()]
    if not alive_animals:
        print("All animals are dead. The visitors just stare blankly at empty cages.")
        return

    for visitor in visitors:
        animal = random.choice(alive_animals)
        visitor_choice = VisitorAction(random.randint(0,3))
        if visitor_choice == VisitorAction.FEED:
            if animal.energy <= 10:
                print(f"{animal.name} is to tired to be fed by {visitor.name}")
                visitor.adjust_happiness(10)
                continue

            elif animal.hunger < 100:
                visitor.adjust_happiness(10)
                animal.hunger += 10
                animal.energy -= 10
                animal.clamp_stats()
                print(f"{visitor.feed_animal(animal.name)}")

            else:
                print(f"{visitor.feed_animal(animal.name)}, The animal: {animal.name} is not hungry.")
                visitor.adjust_happiness(-10)
        elif visitor_choice == VisitorAction.LOOK:
            visitor.adjust_happiness(10)
            animal.clamp_stats()
            print(f"{visitor.look_at_animal(animal.name)}")

        elif visitor_choice == VisitorAction.PET:
            if animal.animal_type == "Tiger" and percentage_chance(30):
                print(f"{visitor.pet_animal(animal.name)}")
                my_multi_line_str = r"""
  ,\/~~~\_                            _/~~~~\
  |  ---, `\_    ___,-------~~\__  /~' ,,''  |
  | `~`, ',,\`-~~--_____    ---  - /, ,--/ '/'
   `\_|\ _\`    ______,---~~~\  ,_   '\_/' /'
     \,_|   , '~,/'~   /~\ ,_  `\_\ \_  \_\'
     ,/   /' ,/' _,-'~~  `\  ~~\_ ,_  `\  `\
   /@@ _/  /' ./',-                 \       `@,
   @@ '   |  ___/  /'  /  \  \ '\__ _`~|, `, @@
 /@@ /  | | ',___  |  |    `  | ,,---,  |  | `@@,
 @@@ \  | | \ \O_`\ |        / / O_/' | \  \  @@@
 @@@ |  | `| '   ~ / ,          ~     /  |    @@@
 `@@ |   \ `\     ` |         | |  _/'  /'  | @@'
  @@ |    ~\ /--'~  |       , |  \__   |    | |@@
  @@, \     | ,,|   |       ,,|   | `\     /',@@
  `@@, ~\   \ '     |       / /    `' '   / ,@@
   @@@,    \    ~~\ `\/~---'~/' _ /'~~~~~~~~--,_
    `@@@_,---::::::=  `-,| ,~  _=:::::''''''    `
    ,/~~_---'_,-___     _-__  ' -~~~\_```---
      ~`   ~~_/'// _,--~\_/ '~--, |\_
           /' /'| `@@@@@,,,,,@@@@  | \
                `     `@@@@@@'
"""
                print(my_multi_line_str)

                print(f"The tiger {animal.name} just bit the hand off visitor: {visitor.name}\n"
                      f"You will never financially recover from this!")
                print("--------------\n"
                      "| GAME OVER! |\n"
                      "--------------")

                game_over = True
                return
            if animal.happiness < 100:
                if percentage_chance(20):
                    visitor.adjust_happiness(20)
                else:
                    visitor.adjust_happiness(10)
                animal.happiness += 10
                animal.energy -= 10
                animal.clamp_stats()
                print(f"{visitor.pet_animal(animal.name)}")
            elif animal.energy <= 0:
                print(f"{visitor.pet_animal(animal.name)}, The animal: {animal.name} is not interested.")

            else:
                print(f"{visitor.pet_animal(animal.name)}, The animal: {animal.name} is not interested.")
        elif visitor_choice == VisitorAction.WANDER:
            print("The visitor aimlessly walks around contemplating life.")

def animal_interaction(zoo):
    print("-----------------------------------------------------")
    print(f"The Animals go about their business")
    print("-----------------------------------------------------")
    for animal in zoo:
        if animal.is_dead():
            continue
        animal_choice = random.randint(0, 2)
        if animal_choice == 0:
            print(animal.make_sound())
        if animal_choice == 1:
            print(animal.sleep())
            animal.energy += 10
            animal.clamp_stats()
        if animal_choice == 2:
            print(animal.eat())
            animal.hunger += 10
            animal.clamp_stats()


def animal_status():
    print("-----------------------------------------------------")
    for animal in zoo:
        if animal.is_dead():
            print(f"Animal: {animal.name} is dead, Great job zookeeper")
        else:
            print(
            f"Name: {animal.name}, Type: {animal.animal_type}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")


def check_if_all_animals_dead():
    global game_over
    dead_animals = [animal for animal in zoo if animal.is_dead()]
    if len(dead_animals) == len(zoo):
        print("All your animals are dead.. the zoo is eerily silent with visitor staring at your dead animals\n"
              "--------------\n"
              "| GAME OVER! |\n"
              "--------------")
        game_over = True
        return


def end_turn():
    global day
    print("-----------------------------------------------------")
    print(f"Day: {day} at {zoo_name} is over. Yet another pointless day in a never ending stretch of days")
    print("-----------------------------------------------------")
    input("Press the \"Any\" key to continue to the next day...\n")
    day += 1
    return day

def visitor_status(visitors):
    print("-----------------------------------------------------")
    print(f"Today's visitors:")
    print("-----------------------------------------------------")
    for visitor in visitors:
        print(f"Name: {visitor.name}, Age: {visitor.age}, Happiness: {visitor.happiness}")


def end_of_day_visitor_status(visitors):
    print("-----------------------------------------------------")
    print("End of the day visitor mood summary:")
    for visitor in visitors:
        print(f"Name: {visitor.name}, Age: {visitor.age}, Happiness: {visitor.happiness}")
        if visitor.happiness <= 0:
            print(f"{visitor.name} did not enjoy the zoo and left a bad review on the internet...\n"
                  f"Oh no! Someone on the internet does not like your zoo!")


def game_loop():
    global day
    global game_over
    while not game_over:
        day_start(zoo)
        zoo_personnel_interaction()
        if game_over:
            return
        visitor_interaction(zoo,visitors)
        if game_over:
            return
        animal_interaction(zoo)
        animal_status()
        end_of_day_visitor_status(visitors)
        during_night(zoo)
        animal_status()
        check_if_all_animals_dead()
        if game_over:
            return
        end_turn()
        if day >= 10:
            game_over = True
            print("-----------------------------------------------------")
            print(f"It's the start of day: {day}")
            print("-----------------------------------------------------")
            print(f"I've had it with these motherf***ing animals in this motherf***ing zoo!\n"
                  f"The narrator presses the self destruct button, destroying your zoo,\n"
                  f"obliterating all of your lovely animals you so deeply cared for!\n"
                  f"--------------\n"
                  f"| GAME OVER! |\n"
                  "--------------")

start_game()
game_loop()

