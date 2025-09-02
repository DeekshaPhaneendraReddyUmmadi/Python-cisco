from salary_manager_v2_crud import createSalary, readSalary, readBySalary, salaries, updateBySalary, deleteBySalary

def menu():
    message = '''
1 - Create Salary
2 - Read All Salaryies
3 - Read by Salary
4 - Update
5 - Delete
6 - Exit/ Logout
            '''
    choice = int(input(message))
    if choice == 1:
        salary = int(input('Salary : '))
        createSalary(salary)
    elif choice == 2:
        result_sal = readSalary()       
        print('Salaries')
        for i in result_sal:
            print(i)
    elif choice == 3:
        salary = int(input('Salary : '))
        index = readBySalary(salary)
        if salary == -1:
            print("Salary not found")
        else:
            print(f'Salary found at index {index}')
    elif choice == 4:
        oldSalary = int(input('Old salary : '))
        newSalary = int(input('New salary : '))
        updateBySalary(oldSalary, newSalary)
    elif choice == 5:
        salary = int(input('salary need to be deleted : '))
        deleteBySalary(salary)
    return choice

def menus():
    print('Salary Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using --Salary Management App--')

menus()