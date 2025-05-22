import Animals
import Visitors
import random

day = 1
game_over = False
zoo_name = ""


visitors = [
    Visitors.Visitors("Pelle", 9, 50),
    Visitors.Visitors("Linda", 33,20)
]

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
    print("-----------------------------------------------------")
    print(f"Welcome to the first day of ZooSimulator!\n"
          f"Choosing animal care as your profession was \"obviously\" the right career path for you!")
    print("-----------------------------------------------------")

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


def daily_comment():
    if day == 2:
        print("So how is this life of monotonous animal care treating you? Are you bored yet?")
    if day == 3:
        print("All animals are equal but some pigs are more equal than others! Did i botch that?")
    if day == 4:
        print("Why are you doing this to yourself? This game obviously ends when all the animals are dead.")
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
        if player_choice.lower() in ["f", "p", "d", "r"]:
            if player_choice == "f":
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

            if player_choice == "p":
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

            if player_choice == "d":
                done = True

            if player_choice == "r":
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
    # Make my visitors do one interaction each
    for visitor in visitors: # add a choice for each visitor
        alive_animals = [animal for animal in zoo if not animal.is_dead()]
        if not alive_animals:
            print("All animals are dead. The visitors just stare blankly at empty cages.")
            return

        visitor_choice = random.randint(0,3)
        animal = random.choice(alive_animals)
        if visitor_choice == 0: # Feed animal.
            if animal.hunger < 100:
                visitor.happiness = max(0, min(100, visitor.happiness + 10))
                animal.hunger += 10
                animal.energy -= 10
                animal.clamp_stats()
                print(f"{visitor.feed_animal(animal.name)}")

            else:
                print(f"{visitor.feed_animal(animal.name)}, The animal: {animal.name} is not hungry.")
                visitor.happiness = max(0, min(100, visitor.happiness - 10))
        elif visitor_choice == 1: # Look at animal
            visitor.happiness = max(0, min(100, visitor.happiness + 10))
            animal.clamp_stats()
            print(f"{visitor.look_at_animal(animal.name)}")

        elif visitor_choice == 2:
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
                    visitor.happiness = max(0, min(100, visitor.happiness + 20))
                else:
                    visitor.happiness = max(0, min(100, visitor.happiness + 10))
                animal.happiness += 10
                animal.energy -= 10
                animal.clamp_stats()
                print(f"{visitor.pet_animal(animal.name)}")
            elif animal.energy <= 0:
                print(f"{visitor.pet_animal(animal.name)}, The animal: {animal.name} is not interested.")

            else:
                print(f"{visitor.pet_animal(animal.name)}, The animal: {animal.name} is not interested.")
        elif visitor_choice == 3: # Wander aimless
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
            f"Name: {animal.name},  Type: {animal.animal_type}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")


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
    day +=1
    print("-----------------------------------------------------")
    print(f"Day: {day} at {zoo_name} is over. Yet another pointless day in a never ending stretch of days")
    print("-----------------------------------------------------")
    input("Press the \"Any\" key to continue to the next day...\n")
    return day


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
        during_night(zoo)
        animal_status()
        check_if_all_animals_dead()
        if game_over:
            return
        end_turn()
        if day >= 10:
            game_over = True
            print("-----------------------------------------------------")
            print(f"I've had it with these motherf***ing animals in this motherf***ing zoo!\n"
                  f"The narrator presses the self destruct button, destroying your zoo,\n"
                  f"obliterating all of your lovely animals you so deeply cared for!\n"
                  f"--------------\n"
                  f"| GAME OVER! |\n"
                  "--------------")

start_game()
zoo_name = name_zoo()
print(f"Your Zoo is named: {zoo_name}\nThis will stand forever! Or until you restart the game...")

print("-----------------------------------------------------")
print(f"Here are your starting animals:")
print("-----------------------------------------------------")
for animal in zoo:
    print(f"Name: {animal.name}, Type: {animal.animal_type}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")

game_loop()

"""
Ideas:
1. Add random visitors from the list of visitors?
2. Do something with visitor happiness. like leave a bad review after they leave.
3. Rework the animal interaction system to work with the Visitor system. 
Move the animal interaction before the Visitor system
and if the animal is sleeping the other options of the visitor auto fail giving them negative happiness. 
Or do it the lazy way and just reuse my random chance generator to see if the animal is sleeping at that moment.
4. Create another animal that the player can "Buy" get for free.
5. Also check on the animals energy level, if it is low the visitors can't play or interact with them as a compliment to
the random sleep system if implemented. 
6. Add a random to the pet system that makes the visitor more happy when petting the animal. DONE


"""
