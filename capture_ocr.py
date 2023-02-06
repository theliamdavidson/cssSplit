from random import randint

def capture_decoder():
    names =[ "PI", "VF" ]
    will_loop = randint(0,1)
    return([names[will_loop],randint(1, 450)/4.5])
    