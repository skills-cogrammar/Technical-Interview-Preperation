'''
Given a starting position, determine if it's possible to 
reach a certain goal.
'''

from timeit import timeit

map = {}

def find_path(start, goal):
    travelled = []
    possible_moves = [start]

    while len(possible_moves) > 0:
        current_position = possible_moves.pop(0)
        travelled.append(current_position)

        if (current_position == goal):
            return True

        for move in map[current_position]:
            if (move not in travelled):
                possible_moves.append(move)


def find_path_opt(start, goal):
    travelled = set()
    possible_moves = [start]

    while len(possible_moves) > 0:
        current_position = possible_moves.pop(0)
        travelled.add(current_position)

        if (current_position == goal):
            return True

        for move in map[current_position]:
            if (move not in travelled):
                possible_moves.append(move)

