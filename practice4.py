class ATM:  
    def __init__(self):  
        self.balance = 1000  # Initial balance for demonstration  
        self.pin = "1234"    # Example PIN  

    def authenticate(self):  
        attempts = 0  
        while attempts < 3:  
            entered_pin = input("Enter your PIN: ")  
            if entered_pin == self.pin:
                print("Authentication successful.")  
                return True  
            else:  
                attempts += 1  
                print("Incorrect PIN. Please try again.")  
        print("Too many incorrect attempts. Please try again later.")  
        return False  

    def check_balance(self):  
        print(f"Your current balance is: ${self.balance}")  

def main():  
    atm = ATM()  
    if atm.authenticate():  
        atm.check_balance()  

if __name__ == "__main__":  
    main()