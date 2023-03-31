import random
def game():
    # num=random.randint(1, 4000)
    return 500


score=game()


file=open("game_high_score.txt","r")
history=file.read()

if history =='':
    file.close()
    file=open("game_high_score.txt","w")
    file.write(str(score))

if str(score) >= str(history):
    file.close()
    file=open("game_high_score.txt","w")
    file.write(str(score))
    
elif str(score) <= str(history):
    file.close()    



