import json
"""
Converting lists to json
"""
#https://stackoverflow.com/questions/26033239/list-of-objects-to-json-with-python
class Student:
    def __init__(self,id_no,name):
        self.id = id_no
        self.name = name
        #self.items = items
    def __str__(self):
        return f"Student's name is {self.name} and id is {self.id}"

class School:
    def __init__(self,name):
        self.name = name
        self.students = []
    def __str__(self):
        return f"Students present in school are {self.students[0]} and {self.students[1]}"
        #return f"{str(temp) for temp in self.students}"
    def __repr__(self):
        return self.__str__()
    def add_student(self,student):
        self.students.append(student)
    def get_json(self):
        json_string = json.dumps([ob.__dict__ for ob in self.students])
        return json_string


if __name__ == "__main__":
    s1 = Student(1,"Sourabh")
    s2 = Student(2,"Vaibhav")
    
    print(s1.__dict__)
    # sch1 = School("My School")
    # sch1.add_student(s1)
    # sch1.add_student(s2)
    # #data = json.dumps(sch1)
    # data = sch1.get_json()

    # print(type(data))