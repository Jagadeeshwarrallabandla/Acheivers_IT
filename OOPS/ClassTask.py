class Student:
    # class is a keyword, It is a blueprint / template for creating new objects.
    # Student, it is the name of the class the starting letter must be capital.
    # class consists of properties and methods
    
    def __init__(self, name, qualification, yearofpassing, course, email):
        self.name = name
        self.qualification = qualification
        self.yearofpassing = yearofpassing
        self.course = course
        self.email = email
        
        # def is a keyword which is used to initialize the function.
        # __init__ is a keyword and method that is used to create a constructor.
        # The above line is a constructor which is used to initialize the properties and it is automatically called when an instance is created.
        # self is a keyword which points to the current class or method.
        # name, email, qualification, yearofpassing and course are the properties of the class.
        
    def Student_info(self):
        return f"Student Details:\n{self.name} completed his {self.qualification} in the year of {self.yearofpassing}. He is willing to learn {self.course} course and his email id is {self.email}."
    
    def Total_Marks(self):
        marks_obtained = [
            {"Subject": "Telugu", "Marks": 95},
            {"Subject": "Hindi", "Marks": 90},
            {"Subject": "English", "Marks": 85},
            {"Subject": "Maths", "Marks": 80},
            {"Subject": "Science", "Marks": 88},
            {"Subject": "Social", "Marks": 92}
        ]
        
        total_marks_obtained_in_all = 0
        for marks in marks_obtained:
            marks_in_every_subject = marks['Marks']
            total_marks_obtained_in_all += marks_in_every_subject
        print("Marks Obtained:", marks_obtained)
        print("Total Marks Obtained:", total_marks_obtained_in_all)
        
        return total_marks_obtained_in_all
        
    def Grade(self):
        grade_marks = self.Total_Marks()
        if grade_marks >= 500:
            print("Grade Obtained: A")
        elif grade_marks >= 400 and grade_marks <= 499:
            print("Grade Obtained: B")
        elif grade_marks >= 300 and grade_marks <= 399:
            print("Grade Obtained: C")
        else:
            print("You have failed.")
    
    def Course(self):
        technologies_included = ["HTML","CSS","JavaScript","React js","Python"]
        return f"Full stack Python including Frontend Languages {technologies_included[0]},{technologies_included[1]},{technologies_included[2]} and {technologies_included[3]} and backend language {technologies_included[4]}"
        
        
    #creating instance 
allinfo = Student("Jagadeesh", "Bachelor's of Technology", 2024, "Full Stack Python", "chintu.jagadeeshwar14@gmail.com")
#Printing all properties
print( "Student Name:", allinfo.name)
print("Qualification :", allinfo.qualification)
print("YOP:", allinfo.yearofpassing)
print("Enrolling Course :", allinfo.course)
print("Email ID :", allinfo.email)
#calling and 
print(allinfo.Student_info())
allinfo.Grade()
print(allinfo.Course())
