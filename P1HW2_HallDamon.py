# This program will allow you to calculate your trip allowance and budget.

# 09/28/2023

# CTI-110 P1HW2 - Travel Expense

# Damon Hall

#Program needs numeric inputs for all variables (excluding location) and put them together
#in order to not only add total expenses, but also give a remaining budget.

print("This program will help calculate your travel expenses. Simply input the specified \n amounts and it will calculate your total!")
#The following variables are established via input in order to make calculations simple
total_budget = int(input('Enter budget: '))
travel_location = input('Enter destination:')
gas_price = int(input('Estimate of total gas prices: '))
approximate_room = int(input('Approximate price of hotel: '))
food_cost = int(input('Estimated food cost: '))
#Below this comment essentially the trip summary, including location, budget, etc
print("--------Total Travel Expenses--------")
print("Location: " , travel_location)
print("Initial Budget: " , total_budget)
print("")
print("Fuel:" , gas_price)
print("Accomodation" , approximate_room)
print("Food:" , food_cost)
print("")
total_cost = (gas_price + approximate_room + food_cost)
print("Total cost for entire trip:" , total_cost)
print("Remaining balance:" , total_budget - total_cost)