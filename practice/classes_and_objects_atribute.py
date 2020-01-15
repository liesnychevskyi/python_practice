class Emp:
    count = 0

    def get_name_age_salary(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.display_details()
        self.increase_count_for_emp()

    def increase_count_for_emp(self):
        Emp.count = Emp.count + 1
        return None

    def display_details(self):
        print(f'The name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
        return None


emp1 = Emp()
emp2 = Emp()

emp1.get_name_age_salary('Stas', 36, 50000)
#emp1.increase_count_for_emp()
emp2.get_name_age_salary('Tom', 30, 20000)
#emp2.increase_count_for_emp()
print(Emp.count)


print(emp1)
print(emp2)
print(dir(emp1))
print(dir(emp2))
#  print(emp1.display_details())
