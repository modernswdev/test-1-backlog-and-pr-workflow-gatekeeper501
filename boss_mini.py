# boss_mini.py

# --- Player and Boss Health Initialization ---
p_hp = 50
b_hp = 50


# BUG (Original Version):
# The attack() function originally did not subtract health from the boss.
# Without reducing b_hp, the game could never progress toward victory.
# FIX IMPLEMENTED:
# Added subtraction logic to reduce boss HP by 10 each time attack() is called.
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")


# BUG (Original Version):
# The heal() function originally lacked boundary validation.
# This allowed:
# - Healing beyond the maximum HP (50)
# - Healing when player HP was 0 (defeated state)
# FIX IMPLEMENTED:
# Added guardrails to prevent healing when defeated and cap HP at 50.
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > 50:
        p_hp = 50
    print(f"Healed! HP is now {p_hp}")


# BUG (Original Version):
# The game loop originally lacked a proper victory condition.
# The boss could reach 0 HP without triggering a win state.
# FIX IMPLEMENTED:
# Added a check to print "Victory!" and terminate the loop when b_hp <= 0.
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
