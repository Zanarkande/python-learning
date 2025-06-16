## 6.100A PSet 1: Part B
## Name: Zanarkande
## Time Spent: 5 minutes
## Collaborators: N/A

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
r = 0.05
amount_saved = 0
month = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < (cost_of_dream_home *  portion_down_payment):

    amount_saved = amount_saved * (1+(r/12))
    amount_saved += (yearly_salary * portion_saved)/12
    month += 1

    if (month % 6) == 0:
        yearly_salary *= 1 + semi_annual_raise


print(f"Number of months: {month}")