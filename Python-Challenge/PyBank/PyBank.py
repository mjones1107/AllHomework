#!/usr/bin/env python
# coding: utf-8

# In[128]:


import csv
date = []
pnl = []
fields = []


# In[129]:


with open('budget_data.csv') as budgetData:
    budgetData = csv.reader(budgetData)
    totalmonths = 0
    maxnum = 0
    minnum = 0
    totalpnl = 0
    fields = next(budgetData)
    for row in budgetData:
        #get total months
        totalmonths = totalmonths + 1
        #convert string to int and total $
        totalpnl += int(row[1]) 
        #get maximum and minimum value information
        if int(row[1]) > maxnum:
            maxnum, maxdate = int(row[1]),row[0]
        if int(row[1]) < minnum:
            minnum, mindate = int(row[1]), row[0]
        date.append(row[0])
        pnl.append(row[1])
   


# In[130]:


#averagechange
avgamt = totalpnl/totalmonths


# In[131]:


print('Financial Analysis')
print('----------------------------')
print("Total Months: ",totalmonths)
print("Total: $",totalpnl)
print("Average Change: $",'{:06.2f}'.format(avgamt))
print("Greatest Increase in Profits: $",maxnum, "on ",maxdate)
print("Greatest Decrease in Profits: $",minnum, "on ", mindate)


# In[139]:


f = open("pybankresults", "w")
f.write('Financial Analysis'+'\n')
f.write('----------------------------'+'\n')
f.write("Total Months: "+str(totalmonths)+'\n')
f.write("Total: $"+str(totalpnl)+'\n')
f.write("Average Change: $"+'{:06.2f}'.format(avgamt) +'\n')
f.write("Greatest Increase in Profits: $"+ str(maxnum) + " on "+ str(maxdate) + '\n')
f.write("Greatest Decrease in Profits: $"+ str(minnum) + " on " + str(mindate) + '\n')

f.close()


# In[ ]:




