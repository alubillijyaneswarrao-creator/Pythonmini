def spin_row():
    pass
def print_row():
    pass
def get_wager():
    pass

def main():
    balance = 100
    print("-----------------------------")
    print("Welcome to the Slot Machine!")
    print("Symbols: A, B, C, D, E ")
    print("-----------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your wager amount (or 'q' to quit): ")
        if bet.isdigit():
            bet = int(bet)
            if bet > balance:
                print("Insufficient balance. Try again.")
                continue
            balance -= bet
        row = spin_row()
        print_row(row)
    
        
        
if __name__ == "__main__":
    main()