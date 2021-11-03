import math
years = int(input('Enter the number of years: '))
rate = float(input('Enter the annual interest rate: '))/100
initial_balance = float(input('initial balance = '))

compound_rate_each_year = []
for year in range(years):
    compound_rate_each_year.append(rate*math.pow((1+rate), year))

#This list will represent the bottom line of the graph
interest_earned_each_year = []
for year in range(years):
    interest_earned_each_year.append(initial_balance*(compound_rate_each_year[year]))
print(interest_earned_each_year)

#Cumulative interest is the summing series of of the interest earned each year
cumulative_interest_each_year = []
sum = 0
for year in range(0, years):
    sum = sum + initial_balance*(compound_rate_each_year[year])
    cumulative_interest_each_year.append(sum)
print(cumulative_interest_each_year)

# This list is the balance earned each year: P*(1+r)^t
balance_each_year = []
balance = 0
for year in range(0, years):
    balance = initial_balance*(math.pow(1+rate, year))
    balance_each_year.append(balance)

print(balance_each_year)
