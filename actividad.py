#Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
#Crear un constructor que inicialice los atributos
#Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.
#Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


students_info = [{"name": "Juan", "age": 20, "grades": [95, 85, 75]}, {"name": "María", "age": 22, "grades": [90, 88, 92]},{"name": "Carlos", "age": 21, "grades": [78, 85, 70]}]


students = [Student(info["name"], info["age"], info["grades"]) for info in students_info]


threshold = 80


passed_students = [student for student in students if student.average_grade() >= threshold]


high_grade_students_dict = {student.name: student for student in students if student.average_grade() > threshold}


print("Lista de estudiantes:")
for student in students:
    print(f"{student.name}: {student.average_grade()}")

print("\nEstudiantes que pasaron:")
for student in passed_students:
    print(f"{student.name}: {student.average_grade()}")

print("\nDiccionario de estudiantes con notas altas:")
for name, student in high_grade_students_dict.items():
    print(f"{name}: {student.average_grade()}")