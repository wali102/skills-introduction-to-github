# Class Definition: The ATM class encapsulates all functionalities related to the ATM,including balance management, deposits, and withdrawals.
class ATM:  

    # Constructor (__init__ method): Initializes the ATM with a balance of $0.00 and sets a flag to indicate that the ATM is running.
    def __init__(self):  
        self.balance = 100.00 # Initial balance set to 0.0  
        self.is_running = True  # to set the Flag to keep the ATM running  
    
    # function to display balance
    def check_balance(self):  
        # Display the current balance formatted to two decimal places  
        print(f"Your current balance is: ${self.balance:.2f}")  

    def deposit(self, amount):  
        # Check if the deposit amount is greater than 0  
        if amount > 0:  
            self.balance += amount  # Add the deposit amount to the balance  
            # Confirm successful deposit with a message  
            print(f"${amount:.2f} deposited successfully.")  
        else:  
            # Inform the user if the deposit amount is invalid  
            print("Please enter a valid amount to deposit.")  

    def withdraw(self, amount):  
        # Check if the withdrawal amount is valid (greater than 0 and less than or equal to the balance)  
        if amount > 0 and amount <= self.balance:  
            self.balance -= amount  # Deduct the withdrawal amount from the balance  
            # Confirm successful withdrawal with a message  
            print(f"${amount:.2f} withdrawn successfully.")  

         # Inform the user if there are insufficient funds
        elif amount > self.balance:  
            print("Insufficient funds.")  

        # Inform the user if the withdrawal amount is invalid 
        else:             
            print("Please enter a valid amount to withdraw.")  

    # run opration do all oprations to chek balance to depost or to withdraw amount
    def run(self):  

        # Start a loop that runs while the ATM is active  
        while self.is_running:  

            # Display the ATM menu options  
            print("\nWelcome to the ATM!")  
            print("1. Check Balance")  
            print("2. Deposit Money")  
            print("3. Withdraw Money")  
            print("4. Exit")  

            # Prompt the user to select an option  
            choice = input("Please select an option (1-4): ")  

            # Handle the user's choice  
            if choice == '1':  
                self.check_balance()  # Call the method to check balance  
            elif choice == '2':  
                # Ask for the deposit amount and call the deposit method  
                amount = float(input("Enter amount to deposit: "))  
                self.deposit(amount)  
            elif choice == '3':  
                # Ask for the withdrawal amount and call the withdraw method  
                amount = float(input("Enter amount to withdraw: "))  
                self.withdraw(amount)  
            elif choice == '4':  
                self.is_running = False  # Set the flag to False to exit the loop  
                print("Thank you for using the ATM. Goodbye!")  
            else:  
                # Inform the user if the selected option is invalid  
                print("Invalid option. Please try again.")  

# This block ensures that the ATM runs only if the script is executed directly  
if __name__ == "__main__":  
    atm = ATM()  # Create an instance of the ATM class  
    atm.run()  # Call the run method to start the ATM simulation