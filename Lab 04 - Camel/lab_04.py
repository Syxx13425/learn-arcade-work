import random


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
            drinks_in_canteen -= 1
            pass
        elif answer == 'B':
            miles_traveled += random.randint(5,12)
            camel_tiredness += random.randint(0,1)
            thirst += 1
            pass
        elif answer == 'C':
            miles_traveled += random.randint(10,20)
            thirst += 1
            natives_traveled += random.randint(7,14)
            camel_tiredness += random.randint(1,3)

        elif answer == 'E':
            pass
        elif answer == 'D':
            camel_tiredness = 0
            print("Your camel is happy!")
            natives_traveled += random.randint(7, 15)

        # choice independent tests
        # Print “Your camel is getting tired.” if the camel’s tiredness is above 5
        if camel_tiredness > 5:
            print("Your camel is getting tired.")
        if thirst > 4:
            print("You are thirsty!")
        if natives_traveled == 15 miles_traveled:
            print("The natives are close!")
    while done:
        if thirst > 6:
            print("You died of thirst!")
        if camel_tiredness > 8:
            print("Your camel is dead.")
        if natives_traveled == miles_traveled :
            print("The natives have caught up to you!")
        if miles_traveled == 200:
            print("You win!")










main()
