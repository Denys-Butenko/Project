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

class ExtendedDenys(Denys):
    def __init__(self, name=None, surname=None, birth_year=None,
                 faculty=None, specialty=None, student_id=None):
        super().__init__(name, surname, birth_year)
        self.faculty = faculty
        self.specialty = specialty
        self.__student_id = student_id  # приватний атрибут

    def get_full_info(self):
        return {
            "Ім'я": self.name,
            "Прізвище": self.surname,
            "Рік народження": self.birth_year,
            "Факультет": self.faculty,
            "Спеціальність": self.specialty,
            "ID Студента": self.__student_id
        }

    def is_graduating(self):
        course = self.calculate_course()
        return course == 4 if course else False

    def _generate_email(self):  # protected метод
        if self.name and self.surname and self.__student_id:
            return f"{self.name.lower()}.{self.surname.lower()}.{self.__student_id}@university.edu"
        return None