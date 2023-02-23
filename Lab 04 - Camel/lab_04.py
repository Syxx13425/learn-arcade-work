def hello():
    print("Welcome to camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your"+
          "desert trek and out run the natives.")

def main():
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drinks_in_canteen = 3

    hello()
    done = False
    while not done:
        print("A. Drink from your canteen")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        answer = input("what is your choice? Q ").upper()
        if answer == 'Q':
            done = True
        elif answer == 'A':
            pass
        elif answer == 'B':
            pass
        elif answer == 'C':
            pass
        elif answer == 'D':
            camel_tiredness: 0
            natives_traveled: -6
            print("The camel is happy!")
            pass
        elif answer == 'E':
            miles_traveled: 0
            drinks_in_canteen: 3
            natives_traveled: -20
            pass
        elif





main()
