def game():
    return 5000

score = game()

file=open("game_high_score.txt","r")
read=file.read()

if read== "":
    file.close()
    file=open("game_high_score.txt","w")
    file.write(str(game()))

elif int(read)<int(score):
    file.close()
    file=open("game_high_score.txt","w")
    file.write(str(game()))
    
elif int(read)>int(score):
    file.close()