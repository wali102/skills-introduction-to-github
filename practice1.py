# ATM Simulation in Python  
def atm():  

    # Initialize user's balance  
    # You can set this to any starting balance
    balance = 1000    
    
    # Start an infinite loop to keep the ATM running  
    # that infinite loop will run untill to option "4.exit".
    while True:  
        print("\nWelcome to the ATM!")  
        print("Please select an option:")  
        print("1. Check Balance")  
        print("2. Deposit Money")  
        print("3. Withdraw Money")  
        print("4. Exit")  

        # Get user choice  
        choice = input("Enter your choice (1-4): ")  
        
        # Check user's choice  
        if choice == '1':  

            # Option to check balance  
            print(f"Your current balance is: ${balance}")  
        
        # if option is 2. depositing money
        elif choice == '2':

            # input method to deposit money  
            deposit_amount = float(input("Enter the amount to deposit: "))  
            
            # Ensure the deposit amount is valid, more than zero
            if deposit_amount > 0:    

                # method to deposit money to balance
                balance += deposit_amount 

                # print section shows deposted amount as new balance   
                print(f"${deposit_amount} deposited. New balance: ${balance}")

            # if user enter an invalid entry      
            else:  
                print("Please enter a valid amount to deposit.")

         # option for 3 choice of withdraw         
        elif choice == '3':  

            # input user method to withdraw money  
            withdraw_amount = float(input("Enter the amount to withdraw: "))  

            # Check if the withdrawal is valid
            if 0 < withdraw_amount <= balance:

                # withdraw method to withdraw from balance    
                balance -= withdraw_amount 

                # that print section shows new balance aftr withdraw  
                print(f"${withdraw_amount} withdrawn. New balance: ${balance}")

            # else shows if invalid amount for withdraw      
            else:  
                print("Invalid withdrawal amount. Ensure it's greater than 0 and less than or equal to your balance.")  
        
        # Exit the ATM
        elif choice == '4':

            # Exit the ATM  
            print("Thank you for using the ATM. Goodbye!")  
            
            # Exit the while loop and terminate the program  
            break  

        # Invalid choice handling          
        else:        
            print("Invalid choice. Please select a valid option (1-4).")  

# Run the ATM function  
atm()