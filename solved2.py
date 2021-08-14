import random
choice = ['rock','paper','scissors']
def rock_paper_scissors():
    while True:
        comp_move = random.choice(choice)
        choose = input()
        if choose in choice:
            if choose == 'rock' and comp_move == 'scissors':
                continue
                return 'Rock Win'
            elif choose == 'rock' and comp_move == 'paper':
                continue
                return 'paper Win'
            elif choose == 'rock' and comp_move == 'rock':
                continue
                return 'Beraberdir'
            elif choose == 'paper'and comp_move == 'scissors':
                continue
                return 'Scissors Win'
            elif choose == 'paper' and comp_move == 'rock':
                continue
                return 'Paper Win'  
            elif choose == 'paper' and comp_move == 'paper':
                continue
                return 'BERABERDIR'  
            elif choose == 'scissors' and comp_move == 'rock':
                continue
                return 'Rock Win'
            elif choose == 'scissors' and comp_move == 'paper':
                continue
                return 'Scissors Win'
            elif choose == 'scissors' and comp_move == 'scissors':
                continue
                return 'beraberdir'
            elif choose == 'q':
                break
                        
print(rock_paper_scissors())                 

