import logging 
import pickle
import os

logging.basicConfig(filename='app.log', 
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO)

employees = []

def read_all():
    if not os.path.exists('employee.dat'):
        return
    with open('employee.dat', 'rb') as reader:
        employees = pickle.load(reader)
    if employees == None:
        return []
    return employees

def create_employee(id, name, job_title, salary, join_date):    
    emp = {
        'id':id, 
        'name': name, 
        'job_title': job_title, 
        'salary': salary, 
        'join_date': join_date
    }
    employees = read_all()
    # employees.append(emp)
    with open('employee.dat', 'wb') as writer:
        pickle.dump(employees, writer)
    logging.info(f'{name} Employee Created.')
    





# employees = []
# def create_employee(id, name, job_title, salary, join_date):
#     emp = {
#         'id':id, 
#         'name': name, 
#         'job_title': job_title, 
#         'salary': salary, 
#         'join_date': join_date
#     }
#     employees.append(emp)
# def read_all():
#     return employees