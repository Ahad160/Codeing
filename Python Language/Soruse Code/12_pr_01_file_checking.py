def Readfile(FileName):
    try:
        with open(FileName,'r') as file:
            print(file.read())
    
    except FileNotFoundError:
        print(f"{FileName} File Not Found")

Readfile("PF_game_high_score.txt")
Readfile("PF_highscore.txt")
Readfile("PF_file4.txtt")
