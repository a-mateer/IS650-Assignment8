# IS650-Assignment8
Git Development with AI

# My Virtual Pet
This program creates a virtual pet for the user. The user grants the pet a name, and then must select actions to keep their pet alive and thriving.

# Initial Version
In the initial version, users chose from four actions that influence the pet's hunger, happiness, and energy.

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep

# Current Actions
In the latest version, users choose from five actions to manage your pet's hunger, happiness, and energy:

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep
5. Take a walk

Enter `Q` to quit. Pet needs stay between 0 and 100, and the game ends when hunger reaches 100 or happiness or energy reaches 0.

# AI Tool Used
I used the built-in Chat option in Visual Studio Code:
> Copilot Fusion selected GPT-6 Luna

# AI Assistance
I gave the model the following prompt:
> Review the program in main.py, suggest improvements, and enhance the game experience for the user by suggesting at least one additional action.

# New or Modified Features
The model gave this summary response:
- Added takeWalk as a fifth action: it boosts happiness while using energy and increasing hunger.
- Added a quit option, feedback for invalid choices, and a default name if the user enters a blank one.
- Capped hunger, happiness, and energy at 0–100, and moved the game-over check so it appears immediately after a fatal action.
- Added a PetStats type and removed unused global stats. 
- Updated the action list in README.md.

# Evaluation of AI Output
I accepted the AI modifications because they made sense from a UI standpoint. Stopping the game when the game-ending decision is made makes a lot of sense for obvious reasons. The custom PetStats type was helpful - it opens the possibility in future versions for managing multiple pets. 

# How to Run the Program
The program may be run from the command line interface from the repository by entering: python main.py
