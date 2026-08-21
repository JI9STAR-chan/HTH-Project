class Villain:
    def __init__(self, name, superpower, difficulty, health):
        self.name = name
        self.superpower = superpower
        self.difficulty = difficulty
        self.health = health

    def display_info(self):
        print("\n--- VILLAIN INFO ---")
        print("Name:", self.name)
        print("Superpower:", self.superpower)
        print("Difficulty:", self.difficulty)
        print("Health:", self.health)


# -------------------------
# EASY VILLAINS
# -------------------------

villain1 = Villain(
    name="Crocodile King",
    superpower="Chomp",
    difficulty="Easy",
    health=50
)

villain2 = Villain(
    name="Poopy Parker",
    superpower="Flush",
    difficulty="Easy",
    health=50
)

villain3 = Villain(
    name="Jittery James",
    superpower="Flip",
    difficulty="Easy",
    health=50
)
# -------------------------
# MEDIUM VILLAINS
# -------------------------

villain4 = Villain(
    name="Your English Teacher",
    superpower="Figuritive Language",
    difficulty="Medium",
    health=100
)

villain5 = Villain(
    name="Solar Pannel Salesmen",
    superpower="Monthly Payments with Free Installation",
    difficulty="Medium",
    health=100
)

villain6 = Villain(
    name="Kookoo Kathy",
    superpower="Coco pufff toss",
    difficulty="Medium",
    health=100
)

# -------------------------
# HARD VILLAINS
# -------------------------

villain7 = Villain(
    name="Your Crazy Ex Boyfriend",
    superpower="Love Bombing 3000",
    difficulty="Hard",
    health=150
)


villain8 = Villain(
    name="College Admissions Officer",
    superpower="Denial of Admission",
    difficulty="Hard",
    health=150
)

villain9 = Villain(
    name="Sydney",
    superpower="Infinite Computer Tabs",
    difficulty="Hard",
    health=150
)

# Store all villains in a list
easy_villains = [villain1, villain2, villain3]

medium_villains = [villain4, villain5, villain6]

hard_villains = [villain7, villain8, villain9]

# Let the player choose a villain
print("WELCOME TO THE VILLAIN SELECT SCREEN!")

print("\nChoose your difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty_choice = int(input("\nEnter your choice: "))


if difficulty_choice == 1:
    selected_list = easy_villains

elif difficulty_choice == 2:
    selected_list = medium_villains

elif difficulty_choice == 3:
    selected_list = hard_villains

else:
    print("Invalid choice!")
    selected_list = []


if selected_list:
    print("\nChoose your villain:")

    for number, villain in enumerate(selected_list, start=1):
        print(f"{number}. {villain.name}")

    choice = int(input("\nEnter the number of the villain you want to fight: "))

    selected_villain = selected_list[choice - 1]

    print("\nYou have selected:")
    selected_villain.display_info()