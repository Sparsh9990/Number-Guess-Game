FILENAME = "expenses.txt"

expenses = []

# Load existing expenses (simple CSV: amount,category,note)
try:
    with open(FILENAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) >= 2:
                amount = float(parts[0])
                category = parts[1]
                note = parts[2] if len(parts) > 2 else ""
                expenses.append({
                    "amount": amount,
                    "category": category,
                    "note": note
                })
except FileNotFoundError:
    pass

def show_expenses(exp_list):
    if not exp_list:
        print("\nNo expenses yet.")
        return
    print("\nYour expenses:")
    for i, e in enumerate(exp_list, start=1):
        print(f"{i}. ${e['amount']} - {e['category']} - {e['note']}")

def total_amount(exp_list):
    return sum(e["amount"] for e in exp_list)

while True:
    print("\nChoose an option:")
    print("A - Add an expense")
    print("L - List expenses")
    print("T - Show total spent")
    print("Q - Quit")
    choice = input("Your choice: ").strip().lower()

    if choice == "a":
        amount_text = input("Amount: ").strip()
        category = input("Category: ").strip()
        note = input("Note (optional): ").strip()
        if amount_text:
            try:
                amount = float(amount_text)
                expenses.append({
                    "amount": amount,
                    "category": category,
                    "note": note
                })
                print("Expense added.")
            except ValueError:
                print("Please enter a valid number for amount.")
    elif choice == "l":
        show_expenses(expenses)
    elif choice == "t":
        print("\nTotal spent: $", total_amount(expenses))
    elif choice == "q":
        break
    else:
        print("Unknown option, try again.")

# Save expenses back to file
with open(FILENAME, "w") as f:
    for e in expenses:
        line = f"{e['amount']},{e['category']},{e['note']}\n"
        f.write(line)

print("\nExpenses saved to", FILENAME)
