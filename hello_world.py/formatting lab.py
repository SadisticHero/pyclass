import random
name = input ("enter your name: ")
salary = int(input(f""""Hello {name} what is your salary?"""))
raise_per = random.randint(0, 100)
Salary_increase = (salary*(raise_per/100))
new_salary = (salary + Salary_increase)
print(f"""Your new salary is {new_salary}""")