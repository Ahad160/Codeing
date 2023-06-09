# C:\Windows\Temp    
# C:\Users\PROGAD~1\AppData\Local\Temp
# C:\Windows\Prefetch

import os

try:

    folder_path = 'C:/Windows/Temp'

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Temp-Files📂 Are Successfully Deleted✔️")
        except Exception as e:
            print("Temp-Files📂 Are Not⚠️ Successfuly Deleted❌")



    folder_path2 = 'C:/Users/PROGAD~1/AppData/Local/Temp'

    for filename in os.listdir(folder_path2):
        file_path = os.path.join(folder_path2,filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("%temp%-Files📂 Are Successfully Deleted✔️")
        except Exception as e:
            print("%Temp%-Files📂 Are Not⚠️ Successfuly Deleted❌")




    folder_path3 = 'C:/Windows/Prefetch'
    os.chmod(folder_path3, 0o700) #Folder Access Permission Given

    for filename in os.listdir(folder_path3):
        file_path = os.path.join(folder_path3,filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Prefetch-Files📂 Are Successfully Deleted✔️")
        except Exception as e:
            print("Prefetch-Files📂 Are Not⚠️ Successfuly Deleted❌")

except PermissionError as error:
    print("Try Again As Administator")

