import os

class Expense:
    def __init__(self,date,title,amount):
        self.date = date
        self.title = title
        self.amount = amount
    
    def __str__(self):
       return f"{self.date} - {self.title} - {self.amount}"

class ExpenseTracker:
    def __init__(self,filename="expenses.txt"):
        self.expense_list = []
        self.filename = filename
    

    
    def add(self, key,date, title, amount):
        new_expense = Expense(date, title, amount)
        self.expense_list.append(new_expense)
        self.save_to_file()

    def view(self):
        if not self.expense_list:
            print("No expenses recorded yet")
            return
        print("All expenses")
        for i, expense in enumerate(self.expense_list, start =1):
            print(f"{i}. {expense}")

    def save_to_file(self):
        with open (self.filename, "w") as f:
            for expense in self.expense_list:
                f.write(f"{expense.date} - {expense.title} {expense.amount}\n")
        
    def load_from_file(self):
        with open(self.filename, "r") as f:
            for line in f:
                date, title, amount = line.strip().split(",")
                self.expense_list.append(Expense(date,title, float(amount)))
    

exp = ExpenseTracker()
exp.add("Expense1", "17-OCT-2025", "Grocerries", 250)
exp.add("Expense2", "18-OCT-2025", "Fruits", 100)

exp.load_from_file()
exp.view()




    
