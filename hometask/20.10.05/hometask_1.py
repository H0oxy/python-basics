class student:
    def __init__(self):
        self.name = None
        self.surname = None
        self.patronymic = None
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None
        self.group_number = None

class teacher:
    def __init__(self):
        self.name = None
        self.surname = None
        self.patronymic = None
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None
        self.group_curator = None

class study_group:
    def __init__(self):
        self.group_nubmer = None
        self.group_curator = None
        self.curator_phone_number = None
        self.number_of_students = None

class college:
    def __init__(self):
        self.college_name = None
        self.college_address = None
        self.college_phonenumber = None

class exam:
    def __init__(self):
        self.subject_name = None
        self.exam_group_number = None
        self.examiner_name = None
        self.examiner_surname = None
        self.examiner_patronymic = None

class exam_of_student:
    def __init__(self):
        self.subject_name = None
        self.group_number = None
        self.student_name =  None
        self.student_surname = None
        self.student_patronymic = None
        self.student_mark = None

class car:
    def __init__(self):
        self.manufacturer = None
        self.model = None
        self.transmission = None
        self.date_of_issue = None
        self.color = None
        self.price = None