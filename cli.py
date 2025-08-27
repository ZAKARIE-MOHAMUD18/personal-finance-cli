from db import init_db, SessionLocal
from models import Account, Transaction, Category
from tabulate import tabulate
from datetime import datetime

def create_account(session):
    name = input("Account name: ")
    balance = float(input("Initial balance: "))
    acc = Account(name=name, balance=balance)
    session.add(acc)
    session.commit()
    print("✅ Account created.")

def list_accounts(session):
    accounts = session.query(Account).all()
    table = [(a.id, a.name, a.balance) for a in accounts]
    print(tabulate(table, headers=["ID", "Name", "Balance"]))

def add_category(session):
    name = input("Category name: ")
    cat = Category(name=name)
    session.add(cat)
    session.commit()
    print("✅ Category added.")

def list_categories(session):
    categories = session.query(Category).all()
    table = [(c.id, c.name) for c in categories]
    print(tabulate(table, headers=["ID", "Name"]))

def add_transaction(session):
    list_accounts(session)
    acc_id = int(input("Select account ID: "))
    list_categories(session)
    cat_id = int(input("Select category ID: "))

    desc = input("Description: ")
    amount = float(input("Amount (+income, -expense): "))

    tx = Transaction(description=desc, amount=amount,
                     account_id=acc_id, category_id=cat_id)
    session.add(tx)

    # update balance
    acc = session.query(Account).get(acc_id)
    acc.balance += amount

    session.commit()
    print("✅ Transaction added.")

def list_transactions(session):
    txs = session.query(Transaction).all()
    table = [(t.id, t.description, t.amount, t.account.name, t.category.name, t.timestamp.strftime("%Y-%m-%d"))
             for t in txs]
    print(tabulate(table, headers=["ID", "Description", "Amount", "Account", "Category", "Date"]))

def update_transaction(session):
    list_transactions(session)
    tx_id = int(input("Transaction ID to update: "))
    tx = session.query(Transaction).get(tx_id)
    if not tx:
        print("⚠ Transaction not found.")
        return
    tx.description = input(f"New description ({tx.description}): ") or tx.description
    tx.amount = float(input(f"New amount ({tx.amount}): ") or tx.amount)
    session.commit()
    print("✅ Transaction updated.")

def delete_transaction(session):
    list_transactions(session)
    tx_id = int(input("Transaction ID to delete: "))
    tx = session.query(Transaction).get(tx_id)
    if tx:
        session.delete(tx)
        session.commit()
        print("✅ Transaction deleted.")

def report_by_category(session):
    rows = session.query(Category.name, Account.name, Transaction.amount).join(Transaction).join(Account).all()
    table = {}
    for cat, acc, amt in rows:
        table.setdefault(cat, 0)
        table[cat] += amt
    print(tabulate(table.items(), headers=["Category", "Total"]))

def report_by_date(session):
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    txs = session.query(Transaction).all()
    filtered = [t for t in txs if t.timestamp.date() == date]
    table = [(t.id, t.description, t.amount, t.account.name, t.category.name) for t in filtered]
    print(tabulate(table, headers=["ID", "Description", "Amount", "Account", "Category"]))


def main():
    init_db()
    session = SessionLocal()
    commands = {
        "1": ("Create account", create_account),
        "2": ("List accounts", list_accounts),
        "3": ("Add category", add_category),
        "4": ("List categories", list_categories),
        "5": ("Add transaction", add_transaction),
        "6": ("List transactions", list_transactions),
        "7": ("Update transaction", update_transaction),
        "8": ("Delete transaction", delete_transaction),
        "9": ("Report by category", report_by_category),
        "10": ("Report by date", report_by_date),
        "0": ("Exit", None)
    }

    while True:
        print("\n--- Personal Finance Tracker ---")
        for k, (desc, _) in commands.items():
            print(f"{k}. {desc}")
        choice = input("Choose: ")
        if choice == "0":
            break
        action = commands.get(choice)
        if action:
            action[1](session)

if __name__ == "__main__":
    main()
