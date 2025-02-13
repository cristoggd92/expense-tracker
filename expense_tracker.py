import argparse
import json
import os
from datetime import datetime

EXPENSE_FILE = "expenses.json"

#Funcion cargar gastos
def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, "r") as file:
        return json.load(file)
    
#Funcion guardar gastos
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

#Funcion agregar gastos
def add_expense(description, amount):
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return
    
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    date = datetime.today().strftime("%Y-%m-%d")
    
    expenses.append({"id": expense_id, "date": date, "description": description, "amount": amount})
    save_expenses(expenses)
    
    print(f"Expense added successfully (ID: {expense_id})")
    
#Funcion listar gastos
def list_expenses():
    expenses = load_expenses()
    print("ID | Date       | Description           | Amount")
    for expense in expenses:
        print(f"{expense['id']} | {expense['date']} | {expense['description']} | {expense['amount']}")
        
#Funcion eliminar gastos
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [e for e in expenses if e["id"] != expense_id]
    save_expenses(expenses)
    print(f"Expense {expense_id} deleted successfully")
    
#Funcion mostrar resumen de gastos
def show_summary():
    expenses = load_expenses()
    total = 0
    if month:
        month = str(month).zfill(2)
        expenses = [e for e in expenses if e['date'][5:7] == month]
        print(f"Total expenses for {datetime.today().strftime('%B')}: $", end="")
    else:
        print("Total expenses: $", end="")
    total = sum(e["amount"] for e in expenses)
    print(total)
    
#Funcion principal
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    
    list_parser = subparsers.add_parser("list", help="List all expenses")
    
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID to delete")
    
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=int, help="Month (1-12) to filter expenses")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        show_summary(args.month)
    else:
        parser.print_help()

#Ejecutar funcion principal
if __name__ == "__main__":
    main()
