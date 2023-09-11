def initial_state():
    return (8, 0, 0)

def is_goal(s):
    if s[0] == 4 and s[1] == 4:
        return True
    else:
        return False

def successors(s):
    x, y, z = s
    space8 = 8 - x #if 0, bottle 8 is full
    space5 = 5 - y #if 0, bottle 5 is full
    space3 = 3 - z #if 0, bottle 3 is full
    #Action1: Pour from bottle 8
    if x > 0:
        #to bottle 5
        if space5 > 0: 
            if x > space5:
                yield(x - space5, 5, z)
            else:
                yield(0, x + y, z)
        #to bottle 3
        elif space3 > 0: 
            if x > space3:
                yield(x - space3, y, 3)
            else:
                yield(0, y, x+z)
    #Action2: Pour from bottle 5
    if y > 0:
        #to bottle 8
        if space8 > 0: 
            if y > space8: ###The system should never go into this condition anyway, since there is only 8 litre of water in the system.
                yield(8, y - space8, z)  
            else:
                yield(x + y, 0, z)
        #to bottle 3
        elif space3 > 0: 
            if y > space3:
                yield(x, y - space3, 3)
            else:
                yield(x, 0, y+z)
    #Action3: Pour from bottle 3
    if z > 0:
        #to bottle 8
        if space8 > 0: 
            if z > space8: ###The system should never go into this condition anyway, since there is only 8 litre of water in the system.
                yield(8, y, z - space8)  
            else:
                yield(x + z, y, 0)
        #to bottle 5
        elif space5 > 0: 
            if z > space5:
                yield(x, 5, z - space5)
            else:
                yield(x, y + z, 0)

