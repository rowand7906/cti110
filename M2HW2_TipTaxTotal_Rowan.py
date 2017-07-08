#Tip, Tax, And Total
#CTI-110 M2HW2 - Tip Tax Total
#Dante' Rowan
#June 9th, 2017
#Get the projected tip amount
total_amount = float(input('Enter the charge for your food: '))

#Calculate the amount as 18 percent tip and 7 percent sales tax.
profit = total_amount * 0.18 * 0.07

#Display each of these amounts and the total
print('The total amount is', format(profit, ',.2f'))
