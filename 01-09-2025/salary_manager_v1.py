'''
    salary manager using list
'''

salaries = []

salaries.append(1000)
salaries.append(4000)
salaries.append(5000)

print("All salaries", salaries)

searchEle = 5000
index = -1
i = 0

for salary in salaries:
    if salary == searchEle:
        index = i
        break
    i += 1 

print("Serach element found at index : " , index)
salaries.remove(searchEle)
print("After removing search element from salaries list : " , salaries)