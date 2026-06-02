import json
import os
import sys

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")

def initialize_storage():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

def load_expenses():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    print("\n" + "-"*45)
    print(f"{'🆕 RECORD NEW EXPENSE ENTRY':^45}")
    print("-"*45 + "\n")
    
    w = 38 
    
    title = input(f" {f'Enter Expense Title/Item Name':<{w}} : ").strip().title()
    if not title:
        print("\n ❌ Error: Expense title cannot be blank.")
        return  
    
    category = input(f" {f'Enter Expense Category (e.g. Food)':<{w}} : ").strip().title()
    
    try:
        amount_raw = input(f" {f'Enter Paid Amount (Rs)':<{w}} : ")
        amount = float(amount_raw)
        if amount <= 0:
            print("\n ❌ Error: Amount must be greater than zero.")
            return
    except ValueError:
        print("\n ❌ Error: Invalid numeric digits typed.")
        return

    expenses = load_expenses()
    expense_id = len(expenses) + 1 if expenses else 1
    
    new_item = {
        "id": expense_id,
        "title": title,
        "category": category if category == "General" else category,
        "amount": amount
    }
    
    expenses.append(new_item)
    save_expenses(expenses)
    print(f"\n Success: '{title}' (Rs {amount:.2f}) added successfully! ✅")


def view_expenses():
    expenses = load_expenses()
    print("\n" + "="*55)
    print(f"{'📊 CURRENT EXPENSE MONITORING REGISTER':^55}\n")
    
    if not expenses:
        print(f"{'\nNO RUNNING EXPENSES STORED IN SYSTEM':^55}\n")
        return

    print(f"{'ID':<5} | {'TITLE / ITEM':<18} | {'CATEGORY':<12} | {'AMOUNT (Rs)':<20}")
    print("-" * 55 + "\n")
    for item in expenses:
        print(f"{item['id']:<5} | {item['title']:<18} | {item['category']:<12} | {item['amount']:>.2f}\n")

def delete_expense():
    print("\n" + "-"*45)
    print(f"{'🗑️ PURGE EXPENSE LOG ENTRY':^45}")
    
    view_expenses()
    expenses = load_expenses()
    if not expenses:
        return

    try:
        target_id = int(input("\nEnter target log Entry ID to remove: "))
    except ValueError:
        print("\n❌ Error: Please type an integer key sequence.")
        return

    updated_expenses = [item for item in expenses if item['id'] != target_id]
    
    if len(updated_expenses) == len(expenses):
        print("\n❌ Error: Specified Entry ID not found.")
        return

    for index, item in enumerate(updated_expenses, start=1):
        item['id'] = index

    save_expenses(updated_expenses)
    print(f"\nSuccess: Expense log entry #{target_id} completely removed! 🗑️")

def display_total_spending():
    expenses = load_expenses()
    print("\n" + "-"*45) 
    print(f"{'📈 FINANCIAL VALUATION RUNTIME RADAR':^45}")
    
    total_cost = sum(item['amount'] for item in expenses)
    print(f" \nCumulative Total Items Logged : {len(expenses)} Entries")
    print(f"Total Aggregated Spending     : Rs {total_cost:,.2f}")
    
    if expenses:
        print("-" * 45 + "\n")
        print(f" {'CATEGORY':<25} | {'TOTAL SPENT':<15}")
        print("-" * 45 + "\n")
        cat_summary = {}
        for item in expenses:
            cat_summary[item['category']] = cat_summary.get(item['category'], 0.0) + item['amount']
        for cat, sum_val in sorted(cat_summary.items()):
            print(f"  {cat:<25} : Rs {sum_val:>11.2f}")


def main_runtime_loop():
    initialize_storage()
    while True:
        print("\n" + "="*50 )
        print(f"{'💼 PERSONAL EXPENSE TRACKER CLI':^50}\n")
        print("  1. Add New Expense Entry\n  2. View Total Ledger Records\n  3. Delete Target Expense Entry\n  " \
    "4. Calculate Cumulative Total Spending\n  5. Shutdown Terminal Console Application")
        
        choice = input("\nSelect operation command option (1-5): ").strip()
        if choice == '1': add_expense()
        elif choice == '2': view_expenses()
        elif choice == '3': delete_expense()
        elif choice == '4': display_total_spending()
        elif choice == '5':
            print("\nShutting down tracking systems interface safely... Goodbye! 🔌\n")
            sys.exit()
        else:
            print("\n❌ System Error: Option out of limits. Try again.")

if __name__ == "__main__":
    main_runtime_loop()