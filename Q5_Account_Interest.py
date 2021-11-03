import math
import matplotlib.pyplot as plt

years = int(input('Enter the number of years: '))
rate = float(input('Enter the annual interest rate(%) : '))/100
initial_balance = float(input('Enter initial balance($) : '))

compound_rate_each_year = []
for year in range(years):
    compound_rate_each_year.append(rate*math.pow((1+rate), year))

#This list will represent the bottom line of the graph
interest_earned_each_year = []
for year in range(years):
    interest_earned_each_year.append(initial_balance*(compound_rate_each_year[year]))

#Cumulative interest is the summing series of of the interest earned each year, middle line of graph
cumulative_interest_each_year = []
sum = 0
for year in range(0, years):
    sum = sum + initial_balance*(compound_rate_each_year[year])
    cumulative_interest_each_year.append(sum)

# This list is the balance earned each year: P*(1+r)^t, top line of graph
balance_each_year = []
balance = 0
for year in range(0, years):
    balance = initial_balance*(math.pow(1+rate, year))
    balance_each_year.append(balance)

# your 3 data sets to plot: balance_each_year, cumulative_interest_each_year, interest_earned_each_year
# bo- means blue with dots and a solid line
# g means green line
# r-- means red dashed line
plt.plot(balance_each_year, 'bo-', label="Balance")
plt.plot(interest_earned_each_year,'g', label = "Interest")
plt.plot(cumulative_interest_each_year, 'r--', label="Cumulative Interest")

plt.xlabel = "Years"
plt.ylabel = "Money ($)"
plt.legend()
plt.show()