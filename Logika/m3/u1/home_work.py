import time
start_time = time.time()
class Student():
   def __init__(self,surname,name,grade) -> None:
      self.surname = surname
      self.name = name
      self.grade = grade


marks = []
students = []
with open('students_large.txt', 'r', encoding='utf-8') as file:
   for line in file:
      data = line.split(' ')
      obj = Student(data[0],data[1],int(data[2]))
      students.append(obj)
for s in students:
   if s.grade == 5:
      print(s.surname)
   marks.append(s.grade)
avereage_rate = sum(marks)/len(marks)
print('Середня оцінка',avereage_rate)

new_time = time.time() - start_time
print('Робота програми:',new_time)