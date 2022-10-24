def read_number():
    x=int(input("Enter a number <1,9>:"))
    return x

def generate_number():
    import random
    return random.randrange(1,9)
    