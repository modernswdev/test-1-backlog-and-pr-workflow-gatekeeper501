# boss_mini.py

# Security Audit: Hardcoded credentials present a massive security vulnerability.
# BONUS FIX: The SECRET_CODE variable and its cheat logic block were entirely removed.

p_hp = 50
b_hp = 50

# Attack Logic: The math to subtract 10 health from the Boss (b_hp) is missing.
# BONUS FIX: Added `b_hp -= 10` so the boss actually takes damage.
def attack():
    global b_hp
    b_hp -= 10
    print("You deal 10 damage!")

# Healing Guardrails: Missing boundary checks allow healing past 50 HP or when dead (0 HP).
# BONUS FIX: Added conditional checks to prevent zombie healing and over-healing.
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > 50:
        p_hp = 50
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    
    # ISSUE: Hardcoded SECRET_CODE and cheat path create a security backdoor.
    # RISK: Anyone who sees the code (or guesses the code) can bypass normal gameplay.
    # REQUIRED FIX (Bonus): Remove SECRET_CODE and all associated cheat logic from production code.
    # Security Audit: Removed the '[c]heat' option from the prompt
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    # Win Condition: The game loop does not trigger a win state when the boss dies.
    # BONUS FIX: Added check to see if b_hp reaches 0 to print "Victory!" and terminate the loop.
    if b_hp <= 0:
        print("Victory!")
        break
# ISSUE: Attack does not reduce the boss’s health. Missing subtraction like: b_hp -= 10
# EFFECT: Boss HP never decreases, so the game cannot progress to a win state.
# REQUIRED FIX (Bonus): Subtract 10 from boss HP each attack and ensure HP doesn't go below 0.
    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
