# Slot Machine Simulation

## Overview
This project simulates a simple 3x3 slot machine with five distinct symbols, including a special Jackpot symbol. Users can define the number of spins, and the simulation calculates the total winnings and the Return to Player (RTP).

## Features
- **Symbols & Paylines**: 
  - The machine uses five symbols: Cherry, Lemon, Orange, Bell, and Jackpot.
  - The only payline is the middle row of the 3x3 grid.
  
- **Reel Mechanics**: 
  - Symbols are selected using random number generation (RNG) based on predefined frequency distributions.
  
- **Winning Conditions**: 
  - Wins occur when all three symbols in the middle row match.
  - Three matching Jackpot symbols trigger a grand payout.

- **Simulation**: 
  - Users can input the number of spins for the simulation.
  - Results are displayed after each spin, including the symbols and winnings.

- **RTP Calculation**: 
  - Calculates the Return to Player (RTP) based on total winnings and total spins.

## Getting Started

### Requirements
- Python 3.x

### How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
