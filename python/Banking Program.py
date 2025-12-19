# Banking Program
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")
def deposit(balance, amount):
    balance += amount
    print(f"Deposited: ${amount:.2f}")
    return balance
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}")
    return balance 
def main():
    balance = 0.0
    while True:
        print("\nBanking Menu:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()