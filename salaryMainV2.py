import salary_manager_v2_crud 

# initializing the seed data with the help of createSalary function 
for i in range(1,10):
    salary_manager_v2_crud.createSalary(i * 1000)
    
# print all data in salaries list
resultSalaries = salary_manager_v2_crud.readSalary()
for i in resultSalaries:
    print(i)

# checking the salaries index by using linear search
print("Salary found at index : ", 10000, " : " , salary_manager_v2_crud.readBySalary(10000))
print("Salary found at index : ", 1000, " : " , salary_manager_v2_crud.readBySalary(1000))
print("Salary found at index : ", 3000, " : " , salary_manager_v2_crud.readBySalary(3000))

# printing the salary by findint the index and print the salary on the index
print(salary_manager_v2_crud.salaries[salary_manager_v2_crud.readBySalary(3000)])

# checking the update function
salary_manager_v2_crud.updateBySalary(3000, 12990)
print(salary_manager_v2_crud.readSalary())

# checking the delete function
salary_manager_v2_crud.deleteBySalary(12990)
print(salary_manager_v2_crud.readSalary())

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