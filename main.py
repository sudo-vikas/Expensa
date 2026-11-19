import pandas as pd

df = pd.read_csv("expense_data_1.csv")
print(df.head())

# Cleaninng data
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head(),"\n")

#Adding multiple expenses
def add_expense(date, category, note, amount, exp_type = "Expense"):
    global data
    new_entry = {
        "Date": date,
        "Category": category,
        "Note":note,
        "Amount":amount,
        "Income/Expense":exp_type
    }
    new_entry = pd.DataFrame([new_entry])
    data = pd.concat([data, new_entry], ignore_index=True)
    print(f" Added: {note}-{amount}({category})")

add_expense("2025-08-22 19:30", "Food", "Shawara", 2500, "Expense")
add_expense("2025-08-22  8:00", "Subscriptions", "Netflix Mothly Plan", 4500, "Expense")
add_expense("2025-08-22 14:00", "Entertainment", "Outdoor games with friends", 7000, "Expense")

#View recent Expenses
def view_expenses(n=5):
    return data.tail(n)
print(view_expenses(5))    

#Summarize spending
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)
print(summarize_expenses())