class Denys:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self, current_year=2025):

# Враховує курс студента відповідно до року народження

        if self.birth_year is None:
            return None
        age = current_year - self.birth_year
        course = max(1, min((age - 17), 4)) if age >= 17 else None
        return course

    def create_name_list(self):

# Створює список з імені та прізвища

        return [self.name, self.surname]

# Приклад використання

student = Denys("Денис", "Бутенко", 2008)
print(student.calculate_course())  # Виведе курс студента
print(student.create_name_list())  # Виведе список ["Денис", "Бутенко"]