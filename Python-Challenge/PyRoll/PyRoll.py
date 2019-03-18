#!/usr/bin/env python
# coding: utf-8

# In[54]:


import csv
from collections import defaultdict
from collections import Counter
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote


# In[55]:


with open('election_data.csv') as electd:
    
    csvreader = csv.DictReader(electd)

    
    #extract each row
    for row in csvreader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
                
VoterIDs = data['Voter ID']
Counties = data['County']
Candidates = data['Candidate']

results = Counter(Candidates)
total_ballots = sum(results.values())
totalVotesKhan = results['Khan']
percentVotesKhan = totalVotesKhan/total_ballots
totalVotesCorrey = results['Correy']
percentVotesCorrey = totalVotesCorrey/total_ballots
totalVotesLi = results['Li']
percentVotesLi = totalVotesLi/total_ballots
totalVotesOTooley = results["O'Tooley"]
percentVotesOTooley = totalVotesOTooley/total_ballots
winner = max(results,key=results.get)
otic = "'"
newln = '\n'    
    


# In[57]:


print(f'Election Result')
print(f'----------------------------')
print(f'Total Votes:        {total_ballots}')
print(f'----------------------------')
print(f'Khan     : {(percentVotesKhan*100):6.4f}% ({totalVotesKhan})')
print(f'Correy   : {(percentVotesCorrey*100):6.4f}% ({totalVotesCorrey})')
print(f'Li       : {(percentVotesLi*100):6.4f}% ({totalVotesLi})')
print(f'O{otic}Tooley :  {(percentVotesOTooley*100):6.4f}% ({totalVotesOTooley})')
print(f'----------------------------')
print(f'Winner:        {winner}')
print(f'----------------------------')


# In[58]:


f = open("electionresults",'w')
f.write(f'Election Result{newln}')
f.write(f'----------------------------{newln}')
f.write(f'Total Votes:        {total_ballots}{newln}')
f.write(f'----------------------------{newln}')
f.write(f'Khan     : {(percentVotesKhan*100):6.4f}% ({totalVotesKhan}){newln}')
f.write(f'Correy   : {(percentVotesCorrey*100):6.4f}% ({totalVotesCorrey}){newln}')
f.write(f'Li       : {(percentVotesLi*100):6.4f}% ({totalVotesLi}){newln}')
f.write(f'O{otic}Tooley :  {(percentVotesOTooley*100):6.4f}% ({totalVotesOTooley}){newln}')
f.write(f'----------------------------{newln}')
f.write(f'Winner:        {winner}{newln}')
f.write(f'----------------------------{newln}')
f.close()

