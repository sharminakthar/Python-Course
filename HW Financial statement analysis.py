#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#profit for each month
profit = []

for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
profit

#tax for each profit
tax = [round (i*0.3,2) for i in profit]
tax

#profit after tax

profit_after_tax = []

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])
profit_after_tax

#profit margin

profit_margin = []

for i in range(0, len(profit)):
    profit_margin.append(profit_after_tax[i] / revenue[i])
profit_margin
#round to two decimal points and times by 100
profit_margin = [round(i * 100, 2) for i in profit_margin]
profit_margin

#mean profit after tax for 12 months
mean_profit_after_tax = sum(profit_after_tax) / len(profit_after_tax)
mean_profit_after_tax

#good months = months with above mean profit after tax 
good_months = []
for i in range (0, len(profit_after_tax)):
    good_months.append(profit_after_tax[i] > mean_profit_after_tax)
good_months

#bad months
bad_months = []
for i in range (0, len(profit_after_tax)):
    bad_months.append(not (good_months[i]))
bad_months

#best month : profit after tax = max
best_month = []
for i in range (0, len([profit_after_tax])):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
best_month

#worst month : profit after tax = min
worst_month = []
for i in range (0, len(profit_after_tax)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
worst_month

#convert all calculations to units of one thousand dollars
revenue_1000 = [round(i/1000, 2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 2) for i in profit_after_tax]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]

#print results
print ("Revenue :") 
print (revenue_1000)
print ("Expenses :") 
print (expenses_1000)
print ("Profit :")
print(profit_1000)
print ("Profit after tax :")
print (profit_after_tax_1000)
print ("Profit margin :")
print (profit_margin)
print ("Good months :")
print (good_months)
print ("Bad months :")
print (bad_months)
print ("Best month :")
print (best_month)
print ("Worst month :")
print (worst_month)