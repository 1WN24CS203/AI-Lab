import random

def minimax(s, p):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    w = next((1 if s[l[0]] == 'X' else -1 for l in lines if s[l[0]] == s[l[1]] == s[l[2]] != None), None)
    if w is not None: return w
    if None not in s: return 0
    
    scores = [minimax([p if i == a else x for i, x in enumerate(s)], 'O' if p == 'X' else 'X') for a in range(9) if s[a] is None]
    return max(scores) if p == 'X' else min(scores)

def print_board(s):
    r = [x if x is not None else ' ' for x in s]
    print(f" {r[0]} | {r[1]} | {r[2]} ")
    print("-----------")
    print(f" {r[3]} | {r[4]} | {r[5]} ")
    print("-----------")
    print(f" {r[6]} | {r[7]} | {r[8]} \n")

b = [None] * 9
lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# Randomly choose who goes first
current_player = random.choice(['X', 'O'])
print("Game Started! Positions are 0-8 (Top-Left to Bottom-Right)")
print(f"Random Choice: Player {current_player} goes first!\n")

# If human goes first, print an empty board as a reference
if current_player == 'O':
    print_board(b)

while None in b:
    if current_player == 'X':
        # AI (X) Move Selection
        moves = [(minimax([ 'X' if i == a else x for i, x in enumerate(b) ], 'O'), a) for a in range(9) if b[a] is None]
        m = max(moves)[1]
        b[m] = 'X'
        print(f"AI (X) played at position {m}:")
        print_board(b)
        
        if any(b[l[0]] == b[l[1]] == b[l[2]] != None for l in lines) or None not in b:
            break
        current_player = 'O' # Pass turn to human

    if current_player == 'O':
        # Human Player (O) Input
        u = int(input("Enter your move O (0-8): "))
        while u < 0 or u > 8 or b[u] is not None:
            u = int(input("Invalid move! Enter empty position O (0-8): "))
        b[u] = 'O'
        print("\nYou played:")
        print_board(b)
        
        if any(b[l[0]] == b[l[1]] == b[l[2]] != None for l in lines) or None not in b:
            break
        current_player = 'X' # Pass turn to AI

# Final Result Assessment
winner = next(('X' if b[l[0]] == 'X' else 'O' for l in lines if b[l[0]] == b[l[1]] == b[l[2]] != None), None)
if winner:
    print(f"Game Over! Player {winner} Wins!")
else:
    print("Game Over! It's a Draw!")
