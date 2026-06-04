name="dheeraj"
age=20
cgpa=9.22
is_student=True

print(f'''
      Types of ==> 
      name is {type(name)}
      age is {type(age)}
      cgpa is {type(cgpa)}
      is_student is {type(is_student)}
''')


print("type conversion")
print()
number = "18"
print(f"before type conversion  -- {type(number)}")
number = int(number)
print(f"after type conversion  -- {type(number)}")

print("String Methods")

fullName = "    dHeeRajpAnyAm   x"
print(fullName.upper())
print(fullName.lower())
print(fullName.strip())
