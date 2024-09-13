class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        elif amount <= 0:
            return "Invalid withdrawal amount"
        else:
            self.balance -= amount
            return f"Withdrawn ${amount}. New balance: ${self.balance}"

    def transfer(self, amount, recipient):
        if amount > self.balance:
            return "Insufficient funds for transfer"
        elif amount <= 0:
            return "Invalid transfer amount"
        else:
            self.balance -= amount
            recipient.balance += amount
            return f"Transferred ${amount} to {recipient.name}. Your new balance: ${self.balance}"

class Customer:
    def __init__(self, name):
        self.name = name
        self.account = None

    def open_account(self, initial_deposit):
        if initial_deposit >= 100:
            self.account = ATM(initial_deposit)
            return f"Account opened successfully with an initial deposit of ${initial_deposit}"
        else:
            return "Initial deposit must be at least $100"

def main():
    print("Welcome to Our Bank!")
    print("Let's Get Started.")

    customers = {}
    while True:
        print("\n1. Open Account\n2. Login\n3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            customer = Customer(name)
            result = customer.open_account(initial_deposit)
            print(result)
            customers[name] = customer

        elif choice == '2':
            name = input("Enter your name: ")
            if name in customers:
                customer = customers[name]
                atm = customer.account
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout")
                    choice = input("Enter choice (1/2/3/4/5): ")

                    if choice == '1':
                        print(atm.check_balance())
                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        print(atm.deposit(amount))
                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        print(atm.withdraw(amount))
                    elif choice == '4':
                        recipient_name = input("Enter recipient's name: ")
                        if recipient_name in customers:
                            recipient = customers[recipient_name].account
                            amount = float(input("Enter amount to transfer: "))
                            print(atm.transfer(amount, recipient))
                        else:
                            print("Recipient not found")
                    elif choice == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Customer not found")

        elif choice == '3':
            print("Exiting program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
