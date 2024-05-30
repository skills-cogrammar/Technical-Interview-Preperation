def get_final_order(children: list, moves: int):
    last_wrapper_index = len(children) - (moves % len(children)) # 2 steps
    return children[last_wrapper_index:] + children[:last_wrapper_index] # 1 step 

# 2 + 1
# 3
# O(1)