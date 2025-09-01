from salary_manager_v2_crud import createSalary, readSalary, readBySalary, salaries, updateBySalary, deleteBySalary


# initializing the seed data with the help of createSalary function 
for i in range(1,10):
    createSalary(i * 1000)
    
# print all data in salaries list
resultSalaries = readSalary()
for i in resultSalaries:
    print(i)

# checking the salaries index by using linear search
print("Salary found at index : ", 10000, " : " , readBySalary(10000))
print("Salary found at index : ", 1000, " : " , readBySalary(1000))
print("Salary found at index : ", 3000, " : " , readBySalary(3000))

# printing the salary by findint the index and print the salary on the index
print(salaries[readBySalary(3000)])

# checking the update function
updateBySalary(3000, 12990)
print(readSalary())

# checking the delete function
deleteBySalary(12990)
print(readSalary())

'''
output: 
        1000
        2000
        3000
        4000
        5000
        6000
        7000
        8000
        9000
        Salary found at index :  10000  :  -1
        Salary found at index :  1000  :  0
        Salary found at index :  3000  :  2
        3000
        [1000, 2000, 12990, 4000, 5000, 6000, 7000, 8000, 9000]
        [1000, 2000, 4000, 5000, 6000, 7000, 8000, 9000]
'''