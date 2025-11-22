import sys

try:
    if len(sys.argv) != 3:
        print("Usage: python bbj.py <initial> <deposit>")
        sys.exit(1)
    
    initial = float(args[0])
    deposit = float(args[1])

    updated= initial + deposit

    print("Initial Balance:", initial)
    print("Deposit Amount:", deposit)
    print("Updated Balance:", updated)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
