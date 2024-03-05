play_again = "yes"
while play_again.lower() == "yes":
    # Welcome message and instructions for the Choose-Your-Own-Adventure application
    print(f"Greetings, traveler! Welcome to our tale of adventure and mystery. ")
    print(f"Before we embark on our quest, I must ask you a few questions to shape your journey. ")
    print(f"After each question, press Enter to continue...")
    input(f"\nPress the enter key to continue...")

    # Collecting user inputs
    character_name = input("\nWhat is the name of our brave explorer? ")
    while len(character_name) == 0:
        character_name = input("The name cannot be empty. Please enter the brave explorer's name: ")

    paths = ["whispering trail", "silent glade"]
    chosen_path = input("\nWhat is the name of the mysterious path our hero takes: The Whispering Trail or the Silent Glade? ").lower()
    while chosen_path not in paths:
        chosen_path = input("Invalid path! Please enter 'The Whispering Trail' or 'The Silent Glade': ").lower()

    artifacts = ["old compass", "cryptic scroll"]
    found_artifact = input("\nWhat ancient object does our adventurer discover: An old compass or a cryptic scroll? ").lower()
    while found_artifact not in artifacts:
        found_artifact = input("Invalid object! Please enter 'an old compass' or 'a cryptic scroll': ").lower()

    creatures = ["wise fox", "talking raven"]
    mystical_creature = input("\nWhich mystical creature does our character befriend: A wise fox or a talking raven? ").lower()
    while mystical_creature not in creatures:
        mystical_creature = input("Invalid creature! Please enter 'a wise fox' or 'a talking raven': ").lower()

    treasures = ["sunstone jewel", "book of elders"]
    sought_treasure = input("\nWhat is our explorer searching for in the heart of the forest: The Sunstone Jewel or the Book of Elders? ").lower()
    while sought_treasure not in treasures:
        sought_treasure = input("Invalid treasure! Please enter 'the Sunstone Jewel' or 'the Book of Elders': ").lower()

    print("\nThank you for your answers! Now, let's begin our adventure.")
    input("Press Enter to step into the world of the unknown...")

    # Start of the story
    print(f"\nOnce upon a time, in a land far, far away, there lived an explorer named {character_name}.")
    print(f"One day, {character_name} decided it was time to discover the secrets of the {chosen_path}.")
    print(f"Armed with nothing but a {found_artifact} and accompanied by a {mystical_creature},")
    print(f"{character_name} set out in search of the fabled {sought_treasure}.")

    # First decision point
    decision1 = input("\nA mysterious path lies ahead, shrouded in fog. Does our hero brave the path? (yes/no): ").lower()
    while decision1 not in ["yes", "no"]:
        decision1 = input("Please answer 'yes' or 'no': ").lower()

    if decision1 == "yes":
        print(f"\n{character_name} steels their nerves and steps into the fog. As it swirls around, the forest transforms.")
        print(f"Ancient trees whisper secrets, and {character_name} feels the weight of countless ages.")
        print(f"The path leads to an archaic stone circle where the air thrums with power. Here lies the heart of the forest's magic.")
        print(f"{character_name} senses that this place holds the key to finding the {sought_treasure}.")
        
    else:
        print(f"\n{character_name} opts for the safety of the known path. The sounds of the village fade, replaced by the forest's serene music.")
        print("Yet, a part of them yearns for the unknown as they pass by old carvings on the trees, hinting at lost lore.")
        print(f"Later, {character_name} comes across a quaint hermitage where an old sage offers tales of the forest's heart and its enigmas.")
        print(f"Though the journey is less mystical, {character_name} gains wisdom that may prove crucial later on.")
        

    # Second decision point
    decision2 = input("\nIn the depths of the forest, a shadowy figure offers two paths to the treasure. Does our hero trust the figure? (yes/no): ").lower()
    while decision2 not in ["yes", "no"]:
        decision2 = input("Please answer 'yes' or 'no': ").lower()

    if decision2 == "yes":
        print(f"\nTrusting the shadowy figure, {character_name} is led down a winding path that descends into a hidden valley.")
        print(f"In the valley, {character_name} finds not only the {sought_treasure} but also learns the truth about the forest's magic.")
        
    else:
        print(f"\n{character_name} decides not to trust the shadowy figure and instead relies on their own instincts to find the way.")
        print("This choice leads to a long and perilous journey, filled with trials, but also with personal growth and self-reliance.")
        

    # Determine the ending based on the user's decisions
    if decision1 == "yes" and decision2 == "yes":
        print(f"\n{character_name}, braving all the dangers, finally uncovers the {sought_treasure} and learns the secrets of the forest.")
        print("They return home, celebrated as a hero who has brought prosperity to their village.")
    elif decision1 == "no" and decision2 == "no":
        print(f"\n{character_name} returns from the forest with new knowledge and tales of wisdom.")
        print("They might not have found the treasure, but they have earned the respect of all through their wise choices.")
    elif (decision1 == "yes" and decision2 == "no") or (decision1 == "no" and decision2 == "yes"):
        print(f"\nThrough a balanced path of caution and courage, {character_name} finds a different kind of treasure.")
        print("Friendship and alliance with the creatures and spirits of the forest, ensuring the village's safety.")
    else:
        print("\nThe path of the adventure remains a mystery, as the choices made do not lead to a known ending.")

    print("\nYour adventure has come to an end. Will you embark on another journey, or is this where you bid farewell?")
    

    # Check if the user wants to play again
    play_again = input("\nWould you like to embark on another adventure? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid choice! Please answer 'yes' or 'no': ").lower()

print("Thank you for playing. Farewell, until our paths cross again!")