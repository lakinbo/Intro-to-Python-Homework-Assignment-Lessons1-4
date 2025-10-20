# Create a budget calculator using a function that tracks income and expenses.
# 
# Requirements:
# 
# Create a function called calculate_budget() that:
    # Asks the user for their monthly income
    # Asks for 3 expenses: rent, food, and entertainment
    # Calculates total expenses and remaining money
    # Uses if/elif/else to give budget advice:
        # If remaining money < 0: "You're overspending! Cut back on expenses."
        # If remaining money < 100: "Your budget is tight. Be careful with spending."
        # If remaining money >= 100: "Great job! You have money left over."
    # Displays a formatted summary
# Call the function at the end of your program


def calculate_budget():
    monthly_income = float(input("Enter your monthly income: $"))
    rent_expense = float(input("Enter rent expense: $"))
    food_expense = float(input("Enter food expense: $"))
    entertainment_expense = float(input("Enter entertainment expense: $"))
    total_expenses = rent_expense + food_expense + entertainment_expense
    remaining_money = monthly_income - total_expenses

    # Budget advise:
    if remaining_money < 0:
        budget_advice = "You're overspending! Cut back on expenses!"
    elif remaining_money < 100:
        budget_advice = "Your budget is tight. Be careful with spending."
    else:
        budget_advice = "Great job! You have money left over."
    
    print("=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining_money:.2f}")
    print()
    print(f"Budget Advice: {budget_advice}")

calculate_budget()

    

