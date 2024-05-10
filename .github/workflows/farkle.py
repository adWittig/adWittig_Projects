import random

def score_check(group_kept):
    score = 0
    gk = sorted(group_kept)
    #
    if len(group_kept) == 1:
        if gk == [1]:
            score += 100
        elif gk == [5]:
            score += 50
    #3 of 1
    if len(group_kept) == 3:
        if sum(group_kept) == 18 and gk[0] == gk [2]:
            score += 600
        elif sum(group_kept) == 15 and gk[0] == gk [2]:
            score += 500
        elif sum(group_kept) == 12 and gk[0] == gk [2]:
            score += 400
        elif sum(group_kept) == 9 and gk[0] == gk [2] or sum(group_kept) == 3 and gk[0] == gk [2]:
            score += 300
        elif sum(group_kept) == 6 and gk[0] == gk [2]:
            score += 200
        elif sum(group_kept) == 3:
            score += 300
    #4 of 1
    if len(group_kept) == 4:
        if gk[0] == gk[1] == gk[2] == gk[3]:
            score += 1000
    #5 of 1
    if len(group_kept) == 5:
    #5 of 1
        if gk[0] == gk[1] == gk[2] == gk[3] == gk[4]:
            score += 2000
    
    if len(group_kept) == 6:
    #6 of 1
        if gk[0] == gk[1] == gk[2] == gk[3] == gk[4] == gk[5]:
            score += 3000
    #straight
        elif gk[0] < gk[1] < gk[2]< gk[3] < gk[4] < gk[5]:
            score += 1500
    #three pairs
        elif gk[0] == gk[1] and gk[2] == gk[3] and gk[4] == gk[5]:
            score += 1500
    #4 and 2
        elif gk[0] == gk[1] == gk[2] == gk[3] and gk[4] == gk[5] or gk[0] == gk[1] and gk[2] == gk[3] == gk[4] == gk[5]:
            score += 1500
     #2 sets of 3
        elif gk[0] == gk[1] == gk[2] and gk[3] == gk[4] == gk[5] and gk[0] != gk[4]:
            score += 2500
    return(score)

def roll_dice(roll_count, roll_list):
    for _ in range(roll_count):
        roll = random.randrange(1,6)
        roll_list.append(roll)

def table_text(names, scores):
    max_name_length = max(len(name) for name in names)
    total_width = 80
    print("\n")
    for name, score in zip(names, scores):
        # Format the name and score
        formatted_name = f"{name:{max_name_length}}"
        formatted_score = f"{score:5}"  # Adjust the width as needed
        
        # Combine the formatted name and score with appropriate spacing
        row = f"{formatted_name} {formatted_score}"
        
        # Print the row
        print(row)

def main():
    last_turn = 0
    turn = 0
    game = True
    p_scores = []
    p_names = []

    print("\n")
    p_count = int(input("How many players will there be? : "))


    for i in range(p_count):
        p_name = input(f"\nWhat's player {i+1}'s name? : ")
        p_names.append(p_name)
        p_scores.append(0)

    while game == True:
        table_text(p_names, p_scores)

        if turn >= p_count:
            turn = 0

        print(f"\n{p_names[turn]} is going!")
        dice_count = 6
        rolls = []
        temp_score = 0
        keep_turn = True

        while keep_turn == True:
            roll_dice(dice_count, rolls)
            print(f"\n{p_names[turn]} rolled : ")

            picking_die = True
            in_die = []

            while picking_die == True:
                print(sorted(rolls))
                keep_any = True

                while keep_any == True:
                    if len(rolls) > 0:
                        response = input("\nDo you want to keep any? y/n : ")
                    else:
                        response = "n"
                    if response in ["n","y"]:
                        keep_any = False
                    else:
                        print("That was not y or n")

                if response == "y" and dice_count > 0:
                    print("\nWhats the first set of dice are you keeping? Separate them by spaces")
                    in_die = list(map(int, input().split()))

                    if all(die in rolls for die in in_die):
                        dice_count -= len(in_die)
                        temp_score += score_check(in_die)
                        print(f"\nYou have {temp_score} points for this turn")

                        for die in in_die:
                            rolls.remove(die)
                        if len(in_die) == 0:
                            print("You lost your turn")
                            keep_turn, picking_die = False, False
                        
                        
                elif response == "n" and len(in_die) > 0:
                    lresponse = input("\nDo you want to roll again? y/n : ")
                    rolls = []
                    if lresponse == "y":
                        if dice_count <= 0:
                            dice_count = 6
                        picking_die = False

                    elif lresponse == "n":
                        if len(in_die) > 0:
                            p_scores[turn] += temp_score
                        keep_turn, picking_die = False, False
                        last_turn = turn
                        turn += 1
                else:
                    last_turn = turn
                    turn += 1
                    keep_turn, picking_die = False, False

        for p_score in p_scores:
            if p_score >= 10000:
                print(p_names[last_turn],"won!")
                game = False

if __name__ == "__main__":
    main()
