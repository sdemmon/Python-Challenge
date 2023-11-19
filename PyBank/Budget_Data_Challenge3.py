import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Initilize variables to store values
totalMonths = 0
totalProfit = 0
averageChange = []
maxIncrease =[]
maxDecrease =[]
dates = []

#Read the CSV file 
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)
    
    csvreader = list(csvreader)
    
    #loop through the rows in CSV file
    for i, row in enumerate(csvreader):
        date = row[0]
        ProfitLoss = int(row[1])

        #Calculate number of months
        totalMonths += 1
        
        #Calulate net profit/loss
        totalProfit += ProfitLoss
        
        #Calculate monthly change of profit/loss
        if i>0:
            change = ProfitLoss - int(csvreader[i-1][1])
            averageChange.append(change)
            dates.append(date)
            

# Find the corresponding dates for the greatest increase and decrease
maxIncrease = max(averageChange) 
max_increase_date = dates[averageChange.index(maxIncrease)] 
maxDecrease = min(averageChange)
max_decrease_date = dates[averageChange.index(maxDecrease)]

# Calculate the average change in profit/loss   
averageChange=(sum(averageChange)/len(averageChange))   

# # Print the analysis results
# print("Financial Analysis")
# print("---------------------------")
# print(f"Total Months: {totalMonths}")
# print(f"Total: ${totalProfit}")
# print(f"Average Change: ${averageChange:.2f}")
# print(f"Greatest Increase in Profits: {max_increase_date} (${maxIncrease})")
# print(f"Greatest Decrease in Profits: {max_decrease_date} (${maxDecrease})")
        
output = f"""        
Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average Change: ${averageChange:.2f}
Greatest Increase in Profits: {max_increase_date} (${maxIncrease})
Greatest Decrease in Profits: {max_decrease_date} (${maxDecrease})
""" 

print(output)

with open("analysis/pybank_analysis.txt", "w") as out_file:
    out_file.write(output)
        
        
        
        
        
        
        
        
        
        
