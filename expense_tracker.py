
import csv
from datetime import date

while True:
    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), name, amount, category])

        print("Expense saved successfully!")

    elif choice == "2":
        print("Your Expenses:")

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                print("----------------------------")
                print("Date:", expense["Date"])
                print("Name:", expense["Name"])
                print("Amount: ₹", expense["Amount"])
                print("Category:", expense["Category"])

    elif choice == "3":
        total = 0

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                total = total + float(expense["Amount"])

        print("Total Expenses: ₹", total)

    elif choice == "4":
        expenses = []

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                expenses.append(expense)

        if len(expenses) == 0:
            print("No expenses found!")

        else:
            print("Your Expenses:")

            for i, expense in enumerate(expenses, start=1):
                print(
                    i,
                    expense["Date"],
                    expense["Name"],
                    "₹" + expense["Amount"],
                    expense["Category"]
                )

            number = int(input("Enter expense number to delete: "))

            if 1 <= number <= len(expenses):
                deleted_expense = expenses.pop(number - 1)

                with open("expenses.csv", "w", newline="") as file:
                    writer = csv.DictWriter(
                        file,
                        fieldnames=["Date", "Name", "Amount", "Category"]
                    )

                    writer.writeheader()
                    writer.writerows(expenses)

                print("Expense deleted successfully!")
                print("Deleted:", deleted_expense["Name"])

            else:
                print("Invalid expense number!")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
