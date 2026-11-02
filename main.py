# My Virtual Pet

name: str = ""
money: int = 0
hunger: int = 0
happiness: int = 0
energy: int = 0

# Game title, primary input, dictionary creation
def gameStart() -> dict:
    print("MY VIRTUAL PET")
    print("---------------------")
    name = input("What is your pet's name?\n")

    stats: dict = {
        "name": name,
        "money": 0,
        "hunger": 50,
        "happiness": 50,
        "energy": 50,
    }

    printStats(stats)

    return stats

# Utility funtion to keep user informed of their pets condition
def printStats(stats):
    print(f"{stats["name"]}'s Stats:")
    print("Hunger:",stats["hunger"])
    print("Happiness:",stats["happiness"])
    print("Energy:", stats["energy"],"\n")

# Action 1
def feedPet(stats) -> dict:
    if stats["money"] >= 25:
        stats["money"] -= 25
        stats["hunger"] -= 15
        printStats(stats)
    else:
        print("Not enough money, go to work.")
    return stats

# Action 2
def playFetch(stats) -> dict:
    stats["happiness"] += 10
    stats["energy"] -= 10
    printStats(stats)
    return stats

# Action 3
def goToWork(stats) -> dict:
    stats["money"] += 50
    stats["hunger"] += 20
    stats["happiness"] -= 20
    printStats(stats)
    return stats

# Action 4
def goToSleep(stats) -> dict:
    stats["hunger"] += 10
    stats["happiness"] += 10
    stats["energy"] += 10
    printStats(stats)
    return stats


if __name__ == "__main__":

    stats = gameStart()

    # User must select action options to keep their pet fed, happy, and energetic.
    while True:
        print("1 = Feed pet")
        print("2 = Play fetch")
        print("3 = Go to work")
        print("4 = Go to sleep\n")
        uInput = input("Select an action:\n")

        if stats["hunger"] >= 100 or stats["happiness"] <= 0 or stats["energy"] <= 0:
            print("Game over. Your pet didn't make it.")
            break
        else:
            if uInput == "1":
                feedPet(stats)
            elif uInput == "2":
                playFetch(stats)
            elif uInput == "3":
                goToWork(stats)
            elif uInput == "4":
                goToSleep(stats)
            else:
                continue