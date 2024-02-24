def main():
    games_played = 0
    player_choice = input("Choose Rock Paper or Scissors")
    computer_choice = generate_random()
    games_played += 1
    while games_played <= 0:
        match player_choice:
            case "Rock":
                if computer_choice("Rock"):
                    print("Draw")
                elif computer_choice("Paper"):
                    print("You lost")
                elif computer_choice("Scissors"):
                    print("You Won!")
                else:
                    print("Not Rock Paper or Scissors")
            case "Paper":
                if computer_choice("Rock"):
                    print("You won!")
                elif computer_choice("Paper"):
                    print("Draw")
                elif computer_choice("Scissors"):
                    print("You lost")
                else:
                    print("Not Paper Scissors or Rock")
            case "Scissors":
                if computer_choice("Rock"): 
                    print("You lost")
                elif computer_choice("Paper"):
                    print("You won!")
                elif computer_choice("Scissors"):
                    print("draw")
                else:
                    print("Not Paper Scissors or Rock")



def generate_random():

main()