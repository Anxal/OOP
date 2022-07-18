class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def __str__(self):
            """Реализует определение средней оценки и возвращает характеристики экземпляра класса вида:
            print(some_student)
            Имя: Ruoy
            Фамилия: Eman
            Средняя оценка за домашние задания: 9.9
            Курсы в процессе изучения: Python, Git
            Завершенные курсы: Введение в программирование
            """

            grades_count = 0
            courses_in_progress_string = ', '.join(self.courses_in_progress)
            finished_courses_string = ', '.join(self.finished_courses)
            for k in self.grades:
                grades_count += len(self.grades[k])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count
            res = f'Имя: {self.name}\n' \
                  f'Фамилия: {self.surname}\n' \
                  f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
                  f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
                  f'Завершенные курсы: {finished_courses_string}'
            return res

        def __lt__(self, other):
            """Реализует сравнение через операторы '<,>' студентов между собой по средней оценке за домашние задания"""
            if not isinstance(other, Student):
                print('Такое сравнение некорректно')
                return
            return self.average_rating < other.average_rating

        def student_rating(student_list, course_name):
            """Функция для подсчета средней оценки за домашние задания
            по всем студентам в рамках конкретного курса
            в качестве аргументов принимает список студентов и название курса"""

            sum_all = 0
            count_all = 0
            for stud in student_list:
                if stud.courses_in_progress == [course_name]:
                    sum_all += stud.average_rating
                    count_all += 1
            average_for_all = sum_all / count_all
            return average_for_all
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


# Задача №1

class Lecturer(Mentor):

    def rate_hw(self, lecturer, course, grade):
        """Реализует возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента
        Принимает на вход переменные rate_hw(self, lecturer, course, grade)"""

    if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
        if course in lecturer.grades:
                lecturer.grades[course] += [grade]
        else:
                lecturer.grades[course] = [grade]
        else:
        return 'Ошибка'

    def __str__(self):
        """Возвращает характеристики экземпляра класса вида:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy
        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

        def __lt__(self, other):
            """Реализует сравнение через операторы '<,>' лекторов между собой по средней оценке за лекции"""
            if not isinstance(other, Lecturer):
                print('Такое сравнение некорректно')
                return
            return self.average_rating < other.average_rating

        def lecturer_rating(lecturer_list, course_name):
            """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
             в качестве аргумента принимает список лекторов и название курса"""

            sum_all = 0
            count_all = 0
            for lect in lecturer_list:
                if lect.courses_attached == [course_name]:
                    sum_all += lect.average_rating
                    count_all += 1
            average_for_all = sum_all / count_all
            return average_for_all

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Реализует возможность выставления оценки студенту за домашние задания,
        если этот проверяющий закреплен за этим студентом по данному курсу,
        или возвращает ошибку.
        Принимает на вход переменные rate_hw(self, student, course, grade)"""

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def __str__(self):
            """Реализует определение средней оценки и возвращает характеристики экземпляра класса вида:
            print(some_lecturer)
            Имя: Some
            Фамилия: Buddy
            Средняя оценка за лекции: 9.9
            """

            res = f'Имя: {self.name}\nФамилия: {self.surname}'
            return res


# Выставляем оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)