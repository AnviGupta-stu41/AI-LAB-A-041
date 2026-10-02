import math

def alpha_beta(depth, nodeIndex, MaximizePlayer, values, alpha, beta, height):
    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if MaximizePlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta pruning
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha pruning
            if beta <= alpha:
                break
        return best

# Main program
values = list(map(int, input("Enter leaf node values (space-separated): ").split()))

# Validate power-of-2 input length and dynamically determine height
n = len(values)
if n == 0 or (n & (n - 1)) != 0:
    print("Error: The number of leaf node values must be a power of 2 (e.g., 2, 4, 8, 16).")
else:
    height = int(math.log2(n))
    result = alpha_beta(0, 0, True, values, -math.inf, math.inf, height)
    print("\nThe optimal value is:", result)