from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue

        visited.add((j1, j2))
        current_path = path + [(j1, j2)]

        if (j1, j2) == target:
            return current_path

        moves = [
            (cap1, j2),  # Fill Jug 1
            (j1, cap2),  # Fill Jug 2
            (0, j2),     # Empty Jug 1
            (j1, 0),     # Empty Jug 2
        ]

        # Pour Jug 1 -> Jug 2
        amount = min(j1, cap2 - j2)
        moves.append((j1 - amount, j2 + amount))

        # Pour Jug 2 -> Jug 1
        amount = min(j2, cap1 - j1)
        moves.append((j1 + amount, j2 - amount))

        for move in moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))

    return None


cap1 = 5
cap2 = 3
target = (4, 0)

solution = water_jug(cap1, cap2, target)

if solution:
    print(f"Steps to reach target state {target}:")
    for step in solution:
        print(step)
else:
    print("No solution exists")