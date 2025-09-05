employees = [{"id" : 101,"name" : "name"},{"id" : 103,"name" : "name1"},{"id" : 102,"name" : "name2"}]   #seed data
def create_employee(id, name):    
    emp = {
        'id':id, 
        'name': name
    }
    employees.append(emp)
def read_all():
    return employees

def read_by_id(id):
    for i in employees:
        if id == i['id']:
            return i
    return None

def update_by_id(id, name):
    emp = read_by_id(id)
    emp['name'] = name
    return None

def delete_by_id(id):
    employees.remove(read_by_id(id))



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