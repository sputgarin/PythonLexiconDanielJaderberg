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
    Animals.Giraffe("Mr Tallneck", 5,50, 50),
    Animals.Lion("Mufasa! The Childhood trauma", 10,50, 50),
    Animals.Antilope("Antiprey", 12,50,50),
    Animals.Tiger("Shere Khan", 9,50,50)
    ]


def name_zoo(zoo_name):
    zoo_name = input("Please input a innovative name for your Zoo that will awe-strike your visitors.\n")
    return zoo_name

def start_game():
    print(f"Welcome to the first day of ZooSimulator!\n"
          f"Choosing animal care as your profession was \"obviously\" the right career path for you!\n")

def hunger_during_night(zoo):
    print("The animals get hungry during the night!")
    for animal in zoo:
        animal.hunger -= 30

def day_start(zoo):
    print(f"It's the start of day: {day}")
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
        print("Just stop giving them food already... Starvation is just a concept... Just say they died of multi related organ failures.")



def zoo_personnel_interaction():
    global game_over
    done = False
    while not done:
        player_choice = input(f"Please choose an interaction for your personnel: [F]eed, [P]lay,[R]elease, [D]one")
        if player_choice.lower() in ["f", "p", "d", "r"]:
            if player_choice == "f":
                for animal in zoo:
                    if animal.hunger >= 100:
                        print(f"The animal: {animal.name} is already full! Stop feeding it!")
                        animal_status()
                    else:
                        animal.hunger += 10
                        animal_status()
            if player_choice == "p":
                for animal in zoo:
                    if animal.happiness >= 100:
                        print(f"The animal: {animal.name} is already happy enough! Stop bothering it!")
                    else:
                        animal.happiness += 10
                        animal_status()
            if player_choice == "d":
                done = True

            if player_choice == "r":
                print(f"You release all the animals who ravage the park, killing all the guests and each other.\n"
                      f"You will probably spend the rest of your life in a dark hole for doing this!\n"
                      f"GAME OVER!")
                game_over=True
                exit(666)

        else:
            print("Incorrect input! Try again!")


def visitor_interaction(zoo, visitors):
    print(f"The visitors interacts with your animal:\n")
    # Make my visitors do one interaction each
    for visitor in visitors: # add a choice for each visitor
        alive_animals = [animal for animal in zoo if not animal.is_dead()]
        if not alive_animals:
            print("All animals are dead. The visitors just stare blankly at empty cages.")
            return

        visitor_choice = random.randint(0,3)
        animal = random.choice(zoo)
        if visitor_choice == 0:
            if animal.hunger < 100:
                visitor.happiness += 10
                animal.hunger += 10
                print(f"{visitor.feed_animal(animal.name)}")

            else:
                print(f"{visitor.feed_animal(animal.name)}, The animal: {animal.name} is not hungry.")
        elif visitor_choice == 1:
            visitor.happiness += 10
            print(f"{visitor.look_at_animal(animal.name)}")

        elif visitor_choice == 2:
            if animal.animal_type == "Tiger":
                print(f"The tiger {animal.name}just bit a visitor! You will never financially recover from this!")
                quit(666)
            if animal.happiness < 100:
                visitor.happiness += 10
                animal.happiness += 10
                print(f"{visitor.pet_animal(animal.name)}")

            else:
                print(f"{visitor.pet_animal(animal.name)}, The animal: {animal.name} is not interested.")


def animal_interaction(zoo):
    for animal in zoo:
        animal_choice = random.randint(0, 1)
        if animal_choice == 0:
            print(animal.make_sound())
        if animal_choice == 1:
            print(animal.sleep())
            animal.energy += 10
        if animal_choice == 2:
            print(animal.eat())
            animal.hunger += 10


def animal_status():
    for animal in zoo:
        print(
            f"Name: {animal.name}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")
        if animal.hunger <= 0:
            print(f"Animal: {animal.name} is dead, Great job zookeeper")

def check_if_all_animals_dead():
    global game_over
    dead_animals = [animal for animal in zoo if animal.hunger <= 0]
    if len(dead_animals) == len(zoo):
        print("All your animals are dead.. the zoo is eerily silent with visitor staring at your dead animals\n"
              "GAME OVER!")
        exit(666)


def end_turn(day):
    day +=1
    print(f"Day: {day} at {zoo_name} is over. Yet another pointless day in a never ending stretch of days\n")
    return day


def game_loop():
    global day
    global game_over
    while not game_over:
        day_start(zoo)
        zoo_personnel_interaction()
        visitor_interaction(zoo,visitors)
        animal_interaction(zoo)
        animal_status()
        hunger_during_night(zoo)
        animal_status()
        check_if_all_animals_dead()
        day = end_turn(day)
        if day >= 10:
            game_over = True
            print(f"I've had it with these motherf***ing animals in this motherf***ing zoo!\n"
                  f"The narrator presses the self destruct button, destroying your zoo,\n"
                  f"obliterating all of your lovely animals you so deeply cared for!\n"
                  f"GAME OVER!")

start_game()
zoo_name = name_zoo(zoo_name)
print(f"Your Zoo is named: {zoo_name}\nThis will stand forever! Or until you restart the game...")


print(f"Here are your starting animals:")
for animal in zoo:
    print(f"Name: {animal.name}, Age: {animal.age}, hunger: {animal.hunger}, Happiness: {animal.happiness}, Energy: {animal.energy}")

game_loop()



"""












"""