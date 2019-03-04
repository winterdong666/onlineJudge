# This is an sql problem so I don't put solutions.

'''
# Write your MySQL query statement below
SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
      TO_DAYS(wt1.RecordDate)-TO_DAYS(wt2.RecordDate)=1;
'''

pass
