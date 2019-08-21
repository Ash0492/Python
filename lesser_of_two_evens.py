#My code from udemy tutorial exercises
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a>b:
            return a
        else:
            return b
    elif a%2 == 0 and b%2 != 0:
        if a>b:
            return a
        else:
            return b
        return b
    elif a%2 != 0 and b%2 == 0:
        if a>b:
            return a
        else:
            return b
        return a
    elif a%2 !=0 and b%2 != 0:
        if a>b:
            return a 
        else:
            return b
    