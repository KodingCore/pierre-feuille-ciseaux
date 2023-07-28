import keyboard

pointsJ1 = 0
pointsJ2 = 0
turn = True
newGame = True

print("Jeux du Pierre Feuille Ciseaux")
while newGame:
    print("Le joueur 1 commence")

    while pointsJ1 < 2 and pointsJ2 < 2:
        if turn:
            print("1 > Pierre, 2 > Feuille, 3 > Ciseaux")
            print("Choix du joueur 1:")
            # Attendre jusqu'à ce qu'une touche soit enfoncée
            event = keyboard.read_event(suppress=True)
            while event.event_type != keyboard.KEY_DOWN:
                event = keyboard.read_event(suppress=True)

            choiceJ1 = event.name
        else:
            print("Choix du joueur 2:")
            # Attendre jusqu'à ce qu'une touche soit enfoncée
            event = keyboard.read_event(suppress=True)
            while event.event_type != keyboard.KEY_DOWN:
                event = keyboard.read_event(suppress=True)

            choiceJ2 = event.name
            if choiceJ1 == "1" and choiceJ2 == "2":
                print("Joueur 1 à choisi Pierre")
                print("Joueur 2 à choisi Feuille")
                print("Joueur 2 remporte cette manche")
                pointsJ2 += 1

            elif choiceJ1 == "1" and choiceJ2 == "3":
                print("Joueur 1 à choisi Pierre")
                print("Joueur 2 à choisi Ciseaux")
                print("Joueur 1 remporte cette manche")

                pointsJ1 += 1
            elif choiceJ1 == "2" and choiceJ2 == "1":
                print("Joueur 1 à choisi Feuille")
                print("Joueur 2 à choisi Pierre")
                print("Joueur 1 remporte cette manche")

                pointsJ1 += 1
            elif choiceJ1 == "2" and choiceJ2 == "3":
                print("Joueur 1 à choisi Feuille")
                print("Joueur 2 à choisi Ciseaux")
                print("Joueur 2 remporte cette manche")

                pointsJ2 += 1
            elif choiceJ1 == "3" and choiceJ2 == "1":
                print("Joueur 1 à choisi Ciseaux")
                print("Joueur 2 à choisi Pierre")
                print("Joueur 2 remporte cette manche")

                pointsJ2 += 1
            elif choiceJ1 == "3" and choiceJ2 == "2":
                print("Joueur 1 à choisi Ciseaux")
                print("Joueur 2 à choisi Feuille")
                print("Joueur 1 remporte cette manche")

                pointsJ1 += 1

            print("J1: " + str(pointsJ1) + " J2: " + str(pointsJ2))
        turn = not turn

    if pointsJ1 == 2:
        print("Le joueur 1 a gagné !")
    else:
        print("Le joueur 2 a gagné !")
    
    playAgain = input("Voulez-vous refaire une partie? y/n")
    if playAgain == "y":
        pointsJ1 = 0
        pointsJ2 = 0
        newGame = True
    else:
        newGame = False

