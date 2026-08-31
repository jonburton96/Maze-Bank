#just4grins
#bank

def main():
    #intialize
    STARTING_BALANCE = float(1000.0)
    transCode = str("")
    transType = str("")
    transAmnt = float(0.0)
    currentBalance = float(0.0)
    Withdraw = float(0.0)
    Deposit = float(0.0)
    

    #input
    transType = str(input("Enter W for Withdrawal or D for deposit:"))
    transAmnt = float(input("Amount for transaction:"))

    #process
    if transType == "W":
        currentBalance = STARTING_BALANCE - transAmnt
        if transAmnt > STARTING_BALANCE:
            print(f"Starting Balance:{STARTING_BALANCE}")
            print(f"Transaction Code:{'I'}")
            print(f"Transaction Type:{'Insufficent Funds'}")
            print(f"Transaction Error:{"Broke ahh, ninja!!"}")
            print()
            print(f"Current Balance:{STARTING_BALANCE}")
            print("Thank you for banking with Maze")
        else:
            print(f"Starting Balance:{STARTING_BALANCE}")
            print(f"Transaction Code:{'W'}")
            print(f"Transaction Type:{'Withdraw'}")
            print(f"Transaction Amount:{transAmnt}")
            print(f"Current Balance:{currentBalance}")
            print("Thank you for banking with Maze")

    elif transType == "D":
        currentBalance = STARTING_BALANCE + transAmnt
        print(f"Starting Balance:{STARTING_BALANCE}")
        print(f"Transaction Code:{'D'}")
        print(f"Transaction Type:{'Deposit'}")
        print(f"Transaction Amount:{transAmnt}")
        print(f"Current Balance:{currentBalance}")
        print("Thank you for banking with Maze")

    else:
        print(f"Starting Balance:{STARTING_BALANCE}")
        print(f"Transaction Code:{"E"}")
        print(f"Transaction Type:{"Unknown Entry"}")
        print(f"Transaction Error::{'Entry must be W or D. Try Again'}")
        print(f"Current Balance:{STARTING_BALANCE}")
        print("Thank you for banking with Maze")
         
        
    
        
        
main()
