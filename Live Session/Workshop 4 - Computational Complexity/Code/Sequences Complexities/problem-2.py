from array import array 

def get_final_order(children: array, moves: int):
    final_order = array('i', [0] * len(children))  # 0 Steps

    for seat, child in enumerate(children): # n 
        next_seat = (seat + moves) % len(children)  # 2(n)
        final_order[next_seat] = child # 0 steps

    return final_order

# n + 2(n)
# 3(n)
# O(n)