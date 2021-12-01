# Sorting Lists 2
# The list method sorted() does two things differently from sort()
# 1. It comes before a list, instead of after as all built-in functions do.
# 2. It generates a new list rather than modifying the one that already exists.
# Seems to be handy for defining in its own variable.
# Example 
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games)
print(games_sorted)