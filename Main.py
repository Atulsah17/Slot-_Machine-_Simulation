import random

# Define the symbols used in the slot machine and their corresponding frequencies
symbols = ["Cherry", "Lemon", "Orange", "Bell", "Jackpot"]

# Define frequencies to influence the likelihood of each symbol appearing
frequencies = {
    "Cherry": 45,   # Common symbol, appears frequently
    "Lemon": 35,    # Also common, but less than Cherry
    "Orange": 15,   # Uncommon symbol
    "Bell": 4,      # Rare symbol
    "Jackpot": 1    # Very rare, special symbol
}

# Define the payout structure for each symbol
payouts = {
    "Cherry": 5,    # Adjusted payout
    "Lemon": 10,    # Adjusted payout
    "Orange": 15,   # Adjusted payout
    "Bell": 30,     # Adjusted payout
    "Jackpot": 500  # Grand payout for hitting the Jackpot
}

def spin_reel():
    """Spin the reel and return a list of three randomly selected symbols."""
    return random.choices(symbols, weights=[frequencies[symbol] for symbol in symbols], k=3)

def calculate_winnings(reels):
    """Calculate the winnings based on the middle row of the reels."""
    middle_row = [reel[1] for reel in reels]

    # Check if all symbols in the middle row match
    if middle_row.count(middle_row[0]) == 3:
        return payouts[middle_row[0]]  # Return the payout for the matching symbol
    else:
        return 0  # No winnings if the symbols don't match

def simulate_slot_machine(spins):
    """Simulate a number of spins and calculate total winnings and RTP."""
    total_winnings = 0
    jackpot_wins = 0

    for spin_num in range(1, spins + 1):
        reels = [spin_reel(), spin_reel(), spin_reel()]  # Spin the reels
        winnings = calculate_winnings(reels)

        # Count Jackpot wins
        if winnings == payouts["Jackpot"]:
            jackpot_wins += 1

        total_winnings += winnings  # Keep track of total winnings

        # Print the result of the spin
        print(f"Spin {spin_num}: {[reel[1] for reel in reels]} - Winnings: {winnings}")

    # Calculate RTP, assuming a bet of 1 unit per spin
    rtp = (total_winnings / spins) * 100

    # Print out the simulation results
    print("\n--- Simulation Results ---")
    print(f"Total Spins: {spins}")
    print(f"Total Winnings: {total_winnings}")
    print(f"Number of Jackpot Wins: {jackpot_wins}")
    print(f"RTP: {rtp:.2f}%")

# Get the number of spins from the user
num_spins = int(input("Enter the number of spins: "))
simulate_slot_machine(num_spins)
