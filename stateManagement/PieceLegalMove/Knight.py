from Constants import MAX, MIN, enemy

def knightLegal(cx, cy, x, y):
    if (abs(x - cx) == 2 and abs(y - cy) == 1) or (abs(x - cx) == 1 and abs(y - cy) == 2):
        return True
    return False