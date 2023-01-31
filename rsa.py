import math
### Switch case for menu ###
def menu(choice):
    match choice:
        case 1:
            rsaEncryption()
        case 2: 
            rsaDecryption()
        case 3:
            print("\nYou exited the program. Goodbye :)\n")
            SystemExit
        case _:
            print("\nInput is not recognized.\n")

### Function to check if a number is prime number or not
def checkIfPrimeNum(num):
    if num < 2:
        return -1
    for i in range(2, num):
        if num % i == 0:
            return -1
    return num

### Function to find the inverse of num2 in GF(num1) [result = e^-1 mod eu_n]
def findValue_d(num1, num2):
    A = [1,0,num1]
    B = [0,1,num2]
    while B[2] != 0 or B[2] != 1:
        if B[2] == 0:
            return -1
        elif B[2] == 1:
            return B[1]
        Q = A[2]//B[2]
        T = [A[0]-(Q*B[0]), A[1]-(Q*B[1]), A[2]-(Q*B[2])]
        for i in range(0,3):
            A[i] = B[i]
            B[i] = T[i]

### Function for encryption ###
def rsaEncryption ():
    # Get user input for message
    msg = int(input("\nEnter the hashed plain message(in integer): "))
    
    # Get inputs for p and q, then verify if prime number
    p = q = -1
    while (p==-1 and q==-1):
        print("\nEnter two prime number, p & q:-\n")
        p = input("p: ")
        q = input("q: ")
        p = checkIfPrimeNum(int(p))
        q = checkIfPrimeNum(int(q))
        if (p==-1 and q==-1):
            print("\nX-X Not prime number X-X")
    # After verification, calculate n and euler of n
    n = p*q
    eu_n = (p-1)*(q-1)
    print(f"\nFor p={p} and q={q}, it have been calculated n={n} and euler(n)={eu_n}\n")

    # Find possible e values and ask user to select
    listforE = []
    for i in range(2, eu_n-1):
        gcd = math.gcd(i,eu_n)
        if gcd == 1:
            listforE.append(i)
    print("All number below have gcd = 1 with euler(n):")
    for i in listforE:
        print(i)
    e = int(input("\nEnter your selected e: "))
    print(f"Your public key is key(n,e) = ({n},{e})")

    # Encrypt the message using public key
    cph = (msg**e)%n
    print(f"The encryption process is done!\nYour ciphered message is {cph}")
    print("\n")

### Function for decryption ###
def rsaDecryption():
    # Get user input for ciphered message
    cph = int(input("\nEnter the hashed cipher message(in integer): "))
    
    # Get inputs for p and q, then verify if prime number
    p = q = -1
    while (p==-1 and q==-1):
        print("\nEnter two prime number, p & q:-\n")
        p = input("p: ")
        q = input("q: ")
        p = checkIfPrimeNum(int(p))
        q = checkIfPrimeNum(int(q))
        if (p==-1 and q==-1):
            print("\nX-X Not prime number X-X")
    # After verification, calculate n and euler of n
    n = p*q
    eu_n = (p-1)*(q-1)
    print(f"\nFor p={p} and q={q}, it have been calculated n={n} and euler(n)={eu_n}\n")
    
    # Find possible e values and ask user to select
    listforE = []
    for i in range(2, eu_n-1):
        gcd = math.gcd(i,eu_n)
        if gcd == 1:
            listforE.append(i)
    print("All number below have gcd = 1 with euler(n):")
    for i in listforE:
        print(i)
    e = int(input("\nEnter your selected e: "))
    
    # Calculate value for d 
    d = findValue_d(eu_n, e)
    print(f"Your private key is key(n,d) = ({n},{d})")

    # Encrypt the message using private key
    msg = (cph**d)%n
    print(f"The decryption process is done!\nYour plain message is {msg}")
    print("\n")

### Main function ###
print("This is RSA algorithm in Python.")
exit = 0
while (exit!=3):
    print("Choose to what to do:\n1) Encrypt plain message.\n2) Decrypt cipher message.\n3) Exit.\n")
    exit = input("Enter the number to choose (1),(2) or (3): ")
    try:    
        exit = int(exit)
    except ValueError:
        exit = 0
    menu(exit)
