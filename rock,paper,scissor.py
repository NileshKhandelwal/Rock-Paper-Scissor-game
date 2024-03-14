import random
l=["rock","paper","scissor"]

while True:
    computercount=0
    yourchoicecount=0
    usercount=int(input('''
                 Game starts....
                 1 YES
                 2 NO  | EXIT
                 '''))
    if usercount==1:
        for a in range(1,6):
            userinput=int(input('''  
                          1 rock
                          2 scissor
                          3 paper      
                          '''))
            if userinput==1:
                yourchoice="rock"
            elif userinput==2:
                yourchoice="scissor"
            elif userinput==3:
                yourchoice="paper"
                
            computer=random.choice(l)
                        
            if computer==yourchoice:
                print("computer value",computer)
                print("user value",yourchoice)
                print("game draw")
                yourchoicecount=yourchoicecount+1
                computercount=computercount+1
            elif (computer=="rock" and yourchoice=="scissor")or(computer=="scissor" and yourchoice=="paper")or(computer=="paper" and yourchoice=="rock"):
                print("computer value",computer)
                print("user value",yourchoice)
                print("computer wins")
                computercount=computercount+1         
                                                        
            else:
                print("computer value",computer)
                print("user value",yourchoice)
                print("user wins")
                yourchoicecount=yourchoicecount+1
            
        if yourchoicecount==computercount:
            print("finally game draw")
            print("user score",yourchoicecount)
            print("computer score",computercount)
        elif yourchoicecount>computercount:
            print("finally user wins")
            print("user score",yourchoicecount)
            print("computer score",computercount)
        else:
            print("finally computer wins")
            print("user score",yourchoicecount)
            print("computer score",computercount)       
                        
    else:
        break
                   
        