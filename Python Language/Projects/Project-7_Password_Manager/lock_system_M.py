import Encryption_M
import Decryption_M
def lock_Protect(LOC_Key,LOC_Code):
    ur1=int(input("Passowrd Manager Authenticator\n1.Log IN\n2.Forget Password\n"))
    Dec=Decryption_M.Decryption(LOC_Key,LOC_Code)
    if ur1 == 1:
        ur2=(input("Enter Pin Code-"))
        if ur2==Dec:
            print("Correct Pin code")
        else:
            print("Incorrect Pin code")
            exit()
    elif ur1 ==2:
        print("Answer the security questions")
        ur3=input("What is youer Soul Name:")
        if ur3=="raiden":
            ur2=int(input("Enter NEW Pin Code-"))
            with open(LOC_Code, 'w') as file:
                file.write(str(ur2))
            Encryption_M.Encryption(LOC_Key,LOC_Code)
            print("Pin Code is Sucessfully Updated")
            exit()

        else:
            print("Wrong Answer")
            exit()


