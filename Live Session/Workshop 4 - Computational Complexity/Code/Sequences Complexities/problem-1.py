def get_final_order(children: list, moves: int):
    standing = None # 0 Steps 
    
    for i in range(moves): # n steps
        for seat, child in enumerate(children): # nxm steps
            
            if standing: # 1 x (n x m)
                child = standing # 0 Steps
            
            if seat + 1 == len(children): # 1 x (n x m)
                children[0] = child # 0 Steps
                continue # 0 Steps

            standing = children[seat + 1] # 1 x (n x m) - 1
            children[seat + 1] = child # 1 x (n x m) - 1

    return children

# (nxm) + (nxm) + (nxm) + ((nxm) - 1) + ((nxm) - 1)
# 3(nxm) + 2(nxm - 2)
# 5(nxm) - 2
# O(mn)