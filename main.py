import random

print("Bridge Crossing Game")
print("Choose which bridge to cross! Choose wisely...\n")

safe_count = 0

while safe_count < 3:
    # random safe side
    safe_side = random.choice(["left", "right"])
    choice = input("Choose a side to cross (left/right): ").lower()
    # invalid choice
    if choice not in ["left", "right"]:
        print("Invalid choice. Try again.")
        continue
    if choice == safe_side:
        safe_count += 1
        print("You picked the safe side! Moving through the bridge...")
    else:
        print("You picked the wrong side! The bridge collapsed! :(")
        print("Game over.")
        break

if safe_count == 3:
    print("You win! You made it across all 3 bridges!")
