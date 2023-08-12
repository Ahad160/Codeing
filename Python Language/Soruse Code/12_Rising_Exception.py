def increment(number):
    try:
        return int(number)+1

    except:
        raise ValueError("Check the value")
        

display=increment("das")
print(display)



   