#Decortor SuperCharge a Funtion, can edit the function From outside
def Decorator(Function):
    def Output():
        print("🔴🔴🔴🔴🔴🔴🔴🔴🔴")
        Function()
        print("🔴🔴🔴🔴🔴🔴🔴🔴🔴")
        
    return Output    


@Decorator
def Name():
    print("My is Raiden")


Name()