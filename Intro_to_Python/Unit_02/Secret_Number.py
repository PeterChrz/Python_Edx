x = input("Enter a secret number from 1 - 100: ")
low = 1
high = 100
gnum = 0
guess = "Is your secret number " +  str(gnum)  + "?" 

while True:
    gnum = (low + high) // 2
    print(f"My guess is: {gnum}")

    if gnum == int(x):
        print("I guessed Correct!")
        break
    elif gnum < int(x):
        low = gnum + 1
    else:
        high = gnum - 1
   
    