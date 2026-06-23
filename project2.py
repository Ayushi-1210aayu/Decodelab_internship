"""Expense Tracker for Project 2.

Features:
- add expense amounts with optional notes
- view total spent and detailed list
- remove individual expenses
- clear all expenses
- view summary statistics
"""


def print_menu():
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spent")
    print("4. View summary")
    print("5. Remove an expense")
    print("6. Clear all expenses")
    print("7. Quit")


def get_total(expenses):
    return sum(item['amount'] for item in expenses)


def add_expense(expenses):
    amount_text = input("Enter expense amount: ").strip()
    if not amount_text:
        print("No amount entered. Try again.")
        return

    try:
        amount = float(amount_text)
        if amount < 0:
            print("Please enter a positive amount.")
            return
    except ValueError:
        print("Invalid amount. Enter a number like 50 or 100.")
        return

    note = input("Enter an optional note for this expense: ").strip()
    expenses.append({
        'amount': amount,
        'note': note
    })
    print(f"Added expense: {amount:.2f} {('- ' + note) if note else ''}")
    print(f"New total: {get_total(expenses):.2f}")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for index, item in enumerate(expenses, start=1):
        note_text = f" - {item['note']}" if item['note'] else ''
        print(f"{index}. {item['amount']:.2f}{note_text}")


def view_total(expenses):
    total = get_total(expenses)
    print(f"\nTotal spent: {total:.2f}")


def view_summary(expenses):
    if not expenses:
        print("No expenses recorded to summarize.")
        return

    total = get_total(expenses)
    count = len(expenses)
    average = total / count
    maximum = max(item['amount'] for item in expenses)
    minimum = min(item['amount'] for item in expenses)

    print("\nExpense Summary:")
    print(f"Count: {count}")
    print(f"Total spent: {total:.2f}")
    print(f"Average expense: {average:.2f}")
    print(f"Highest expense: {maximum:.2f}")
    print(f"Lowest expense: {minimum:.2f}")


def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return

    view_expenses(expenses)
    choice = input("Enter the number of the expense to remove: ").strip()
    if not choice.isdigit():
        print("Please enter a valid expense number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Removed expense: {removed['amount']:.2f}{(' - ' + removed['note']) if removed['note'] else ''}")
        print(f"New total: {get_total(expenses):.2f}")
    else:
        print("That expense number does not exist.")


def clear_expenses(expenses):
    if not expenses:
        print("No expenses to clear.")
        return

    confirm = input("Are you sure you want to clear all expenses? (yes/no): ").strip().lower()
    if confirm in ('yes', 'y'):
        expenses.clear()
        print("All expenses have been cleared.")
    else:
        print("Clear canceled.")


def main():
    expenses = []

    print("Welcome to the Expense Tracker!")
    print("Use the menu to manage your expenses and view totals.")

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_total(expenses)
        elif choice == '4':
            view_summary(expenses)
        elif choice == '5':
            remove_expense(expenses)
        elif choice == '6':
            clear_expenses(expenses)
        elif choice == '7':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == '__main__':
    main()
