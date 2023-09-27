try:
 class Input:
    
    def __init__(self): 
      print("The Binary to Decimal converter")
      self.user=input("Enter The Binary Number--")
      
 class Calculation(Input):
    
      def __init__(self):
        super().__init__()
        list=[]
        for i in range(len(self.user)):
            Add=((len(self.user)-1)-i)
            list.insert(i, Add)

        self.list2=[]
        for j in range(len(self.user)):
            
            Cal=(int(self.user[j])*(2**int(list[j])))
            self.list2.insert(j,Cal)
    

 class Display(Calculation,Input):

    def __init__(self):
     super().__init__()
     print(f"\nBinary-{self.user}\nDecimal--{sum(self.list2)}")

  
 object=Display()

except Exception as error:
    print("\nInvalid Entrys")
    print("Pleace Try Again With Binary Number")