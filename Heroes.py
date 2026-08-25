class Heroes:
    def __init__(self, name, superpower, difficulty, health):
        self.name = name
        self.superpower = superpower
        self.difficulty = difficulty
        self.health = health

    def display_info(self):
        print("\n--- HEROES INFO ---")
        print("Name:", self.name)
        print("Superpower:", self.superpower)
        print("Difficulty:", self.difficulty)
        print("Health:", self.health)

# EASY HEROES

hero1 = Heroes(
    name="Teradactyl Thalia",
    superpower="Echo Location",
    difficulty="Easy",
    health=50
)

hero2 = Heroes(
    name="Kimchi Kenneth",
    superpower="Spicy Breath",
    difficulty="Easy",
    health=50
)

hero3 = Heroes(
    name="Angy Angy Abby",
    superpower="Rumbling Stomps",
    difficulty="Easy",
    health=50
)

# MEDIUM HEROES

hero4 = Heroes(
    name="Strawberry Shawty",
    superpower="Heart Kiss Nukes",
    difficulty="Medium",
    health=100
)

hero5 = Heroes(
    name="Friday Night Demon",
    superpower="Blinding Disco Lights",
    difficulty="Medium",
    health=100
)

hero6 = Heroes(
    name="Nutella Baby",
    superpower="Projectile Vomit",
    difficulty="Medium",
    health=100
)


# HARD HEROES

hero7 = Heroes(
    name="Your Loving Wife",
    superpower="Pancake Slapper Tornado",
    difficulty="Hard",
    health=150
)


hero8 = Heroes(
    name="Money Maker",
    superpower="Coin Toss of Doom and Dispair",
    difficulty="Hard",
    health=150
)

hero9 = Heroes(
    name="Chocolate Cake",
    superpower="Head chomper",
    difficulty="Hard",
    health=150
)

# Store all heroes in a list
easy_heroes = [hero1, hero2, hero3]

medium_heroes = [hero4, hero5, hero6]

hard_heroes = [hero7, hero8, hero9]

# Let the player choose a hero
print("WELCOME TO THE HERO SELECT SCREEN!")

print("\nChoose your difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty_choice = int(input("\nEnter your choice: "))


if difficulty_choice == 1:
    selected_list = easy_heroes

elif difficulty_choice == 2:
    selected_list = medium_heroes

elif difficulty_choice == 3:
    selected_list = hard_heroes

else:
    print("Invalid choice!")
    selected_list = []


if selected_list:
    print("\nChoose your hero:")

    for number, hero in enumerate(selected_list, start=1):
        print(f"{number}. {hero.name}")

    choice = int(input("\nEnter the number of the hero you want to play as: "))

    selected_hero = selected_list[choice - 1]

    print("\nYou have selected:")
    selected_hero.display_info()