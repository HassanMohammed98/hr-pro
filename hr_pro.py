from datetime import date
	
todays_date = date.today()

class Employee:
   #Employee class here
    def __init__(self, name:str, age:int, salary:float, employment_year:int):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return todays_date.year - self.employment_year

    def get_employee(self):
        return {'name':self.name,'age':self.age, 'salary':self.salary,'Working Years':self.get_working_years()}

class Manager(Employee):
    #Manager class here
    def __init__(self, name:str, age:int, salary:float, employment_year:int , bonus_percentage:float):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def get_manager(self):
        return {'name':self.name,'age':self.age, 'salary':self.salary,'Working Years':self.get_working_years(),'Bonus':self.get_bonus()}
        
def main():
	# main code here
    Employees = []
    Managers = []
    print("Welcome to HR Pro {}".format(todays_date.year))

    while True:
        print('''Options:
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit\n''')
        try:
            action = int(input("What would you like to do? "))
        except:
            print("input is invalid. try again.")
        else:
            if (action == 1):
                print("-----------------\nEmployees")
                for employee in Employees:
                    print("Name: {}, Age: {}, Salary: {}, Working Years: {}".format(employee['name'], employee['age'],employee['salary'],employee['Working Years']))
                print("-----------------\n")
            elif (action == 2):
                print("-----------------\nManagers")
                for manager in Managers:
                    print("Name: {}, Age: {}, Salary: {}, Working Years: {}, Bonus: {}".format(manager['name'], manager['age'],manager['salary'],manager['Working Years'],manager['Bonus']))
                print("-----------------\n")
            elif (action == 3):
                print("-----------------")
                name = input("Name: ")
                age = int(input("Age: "))
                salary = float(input("Salary: "))
                employment_year = int(input("Employement year: "))
                temp = Employee(name,age,salary,employment_year)
                Employees.append(temp.get_employee())
                print("Employee added succesfully\n")
            elif (action == 4):
                name = input("Name: ")
                age = int(input("Age: "))
                salary = float(input("Salary: "))
                employment_year = int(input("Employement year: "))
                bonus_percentage = float(input("Bonus Percentage: "))
                temp = Manager(name,age,salary,employment_year,bonus_percentage)
                Managers.append(temp.get_manager())
                print("Manager added succesfully\n")
            elif (action == 5):
                break
            else:
                print("invalid choice. try again.")

if __name__ == '__main__':
	main()
