total = 0

while True:
    expense = input("Enter expense (or 'quit'): ")

    if expense.lower() == "quit":
        break

    try:
        total += int(expense)
    except ValueError:
        print("Invalid Data")

print("Final Total:", total)