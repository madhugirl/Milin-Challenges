import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

#calculating the total number of loans in the list.
number_of_loans = len(loan_costs)
len(loan_costs)
print(number_of_loans)

#calculation the total loan amounts.
total_loan_amounts = sum(loan_costs)
sum(loan_costs)
print(total_loan_amounts)

#calculating the average loan amount.
average_loan_amount = sum(loan_costs) / len(loan_costs)
print(average_loan_amount)

#print statments of the number of loans, total loan amounts and average loan amounts
print(f"The total number of loans is {number_of_loans}")
print(f"The total amount of loans is {total_loan_amounts}")
print(f"The average loan amount is {average_loan_amount}")

    
#calucating the present value of loan 1.

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#calculating the future value and remaining months of loan 1
loan_price = 500
remaining_months = 9

future_value = loan.get("future_value")
print(f"the future value of this loan is {future_value}")

remaining_months = loan.get("remaining_months")
print(f"the remaining months of this loan is {remaining_months}")

#calculate fair present value of loan 1
time = remaining_months
present_value = future_value / (1 + .20) ** time
print(present_value)

#caluculing if client should purchase new loan
if present_value >= loan_price:
    print("the loan is worth at least the cost to buy it")

elif present_value < loan_price:
    print("the loan is too expensive and not worth the price")


#calculating new loan with annual discount rate
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


def present_value(future_value, remaining_months, annual_discount_rate):
    return(future_value * annual_discount_rate / remaining_months)


annual_discount_rate = 0.20
calculate_present_value = present_value(
new_loan["future_value"],
new_loan["remaining_months"],
annual_discount_rate)

print(f"The present value of the loan is: {calculate_present_value}")


#calculating inexpensive loans for client to purchase in orde to make a profit.  Add to new list inexpensive_loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


inexpensive_loans = []


for list_loan_price in loans:
    if list_loan_price["loan_price"] <= 500:
        inexpensive_loans.append(list_loan_price)


print(inexpensive_loans)


#create a csv file with new list: inexpensive_loans
header = ["loan_price", "remaining_months", "repayment_interval" ,"future_value"]

path = Path("inexpensive_loans.csv")
with open (path, "w") as csvfile:
 csv_writer = csv.writer(csvfile, delimiter = ",")
 csv_writer.writerow(header)
 for x in inexpensive_loans:
  csv_writer.writerow(loan.values())