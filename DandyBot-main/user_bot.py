import random
def rideOnWall(check, x, y):
    if (check('gold', x, y) > 0):
        return "take"
    if (check('wall', x - 1, y) and check('wall', x, y + 1)):
        return "right"
    if (check("wall", x + 1, y) and check('wall', x, y + 1)):
        return "up"
    if (check('wall', x - 1, y) and check('wall', x, y - 1)):
        return "down"
    if (check('wall', x + 1, y) and check('wall', x, y - 1)):
        return "left"
    if check("wall", x, y + 1):
        return "right"
    if check("wall", x, y - 1):
        return "left"
    if check("wall", x + 1, y):
        return "up"
    if check("wall", x - 1, y):
        return "down"
    else:
        if (check("wall", x + 1, y + 1)):
            return "right"
        if (check("wall", x - 1, y + 1)):
            return "down"
        if (check("wall", x + 1, y - 1)):
            return "up"
        if (check("wall", x - 1, y - 1)):
            return "left"


def script(check, x, y):
    if(check("level") == 1):
        if(((18 <= x <= 23 and y == 4) or (4 <= y <= 8)) and check('gold', x, y) > 0):
            return 'take'
        elif(x == 23):
            return 'down'
        else:
            return 'right'
    elif(check("level") == 2):
        if (check('gold', x, y) > 0):
            return "take"

        elif (check('gold', x+2, y) > 0 or check('gold', x+1, y) > 0):
            return "right"
        elif (check('gold', x, y+1) > 0):
            return "down"
        elif (check('gold', x, y-1) > 0):
            return "up"
        elif (x == 0):
            return "right"
        elif (x == 1):
            return "up"


    elif(check("level") == 3):
        if (check('gold', x, y) > 0):
            return "take"
        if(check('wall', x-1, y) and check('wall', x, y+1)):
            return "right"
        if(check("wall", x+1, y) and check('wall', x, y+1)):
            return "up"
        if(check('wall', x-1, y) and check('wall', x, y-1)):
            return "down"
        if(check('wall', x+1, y) and check('wall', x, y-1)):
            return "left"
        if check("wall", x, y+1):
            return "right"
        if check("wall", x, y-1):
            return "left"
        if check("wall", x+1, y):
            return "up"
        if check("wall", x-1, y):
            return "down"
        else:
            if(check("wall", x+1, y+1)):
                return "right"
            if(check("wall", x-1, y+1)):
                return "down"
            if(check("wall", x+1, y-1)):
                return "up"
            if(check("wall", x-1, y-1)):
                return "left"

    elif(check("level") == 4):
        if(x == 19 and 2 <= y <= 6):
            return "down"
        if(x == 5 and 11 <= y <= 12):
            return "down"
        return rideOnWall(check, x, y)
    elif(check("level") == 5):
        if (check('gold', x, y) > 0):
            return "take"
        return random.choice(["left", "right", "up", "down"])

