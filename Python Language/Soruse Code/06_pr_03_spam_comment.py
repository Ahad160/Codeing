text = input("Enter the text\n")

spam = False

if "make a lot of money" in text:
    spam = True 
elif "Buy Now" in text:
    spam = True
elif "Subcibe this" in text:
    spam = True
elif "click this" in text:
    spam = True

if spam == True :
    print("This text is spam")
else:
    print("This text is not spam")