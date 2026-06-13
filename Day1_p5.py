class Employee:

    def __init__(self, name, age, salary, status):
        print("Initializing Employee object...")
        self.name = name
        self.age = age
        self.salary = salary
        self.status = status


name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
salary = float(input("Enter employee salary: "))
status = input("Enter employee status (Active/Inactive): ").lower() == "active"

emp1 = Employee(name, age, salary, status)

print("\nEmployee Details")
print("Name:", emp1.name)
print("Age:", emp1.age)
print("Salary:", emp1.salary)
print("Status:", "Active" if emp1.status else "Inactive")
print("Employee object created successfully!")