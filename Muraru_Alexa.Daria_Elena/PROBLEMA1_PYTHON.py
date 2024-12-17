class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in _init_)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgr_count=0

    def __init__(self, name, salary, departament):
        NUME_ECHIPA = "F23 "
        self.name = name
        self.salary = salary
        self.departament = NUME_ECHIPA + departament
        Manager.mgr_count += 1
    
    def display_employee(self):
        print(f"Departament: {self.departament}")

    def __del__(self):
        Manager.mgr_count -= 1

   


manager1 = Manager("Zorila", 2000, "HR")
manager2 = Manager("Stefana", 2500, "Tech")
manager3 = Manager("Maria", 1200, "IT")


manager1.display_employee()
manager2.display_employee()
manager3.display_employee()

print(f"Numarul de manageri este {Manager.mgr_count}")



employee1= Employee("Daria",5700)
employee2= Employee("Kitty",6580)
employee3= Employee("Stefania",4566)




employee1.display_employee()
employee2.display_employee()
employee3.display_employee()



print(f"Numarul de angajati este {Employee.empCount}")