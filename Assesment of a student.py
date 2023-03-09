from Code import Student
import random

Nikita = Student("Nikita", 16, 8.5, "Handsome", True, False, True, True)
Timur = Student("Timur", 16, 8.3, "Very good", True, True, True, True)
Dima = Student("Dima", 16, 7.3, "Ok", True, True, False, True)
Mark = Student("Mark", 16, 8.2, "Very good", True, True, True, True)

Information = [Nikita, Timur, Dima, Mark]
random.shuffle(Information)







def assesment(Information):

    List1 = []
    Student_Mark = 0
    for i in range(len(Information)):
        for Student in Information:
                if Student.av_mark > 8:
                    Student_Mark += 2
                if Student.appearance == "Handsome":
                    Student_Mark += 3
                elif Student.appearance == "Very good":
                    Student_Mark += 2
                elif Student.appearance == "Ok":
                    Student_Mark += 1
                if Student.doing_sport is True:
                    Student_Mark += 1
                if Student.is_kind is True:
                     Student_Mark += 1
                if Student.intelligent is True:
                    Student_Mark += 2
                if Student.nice_clothes is True:
                    Student_Mark += 1
                    List1.append([Student.name, Student_Mark])
                    Information.remove(Student)
                    Student_Mark = Student_Mark - Student_Mark

                if len(List1) == 4:
                    print(List1)









assesment(Information)

