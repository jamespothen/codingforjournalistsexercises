class Student:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.courses = []
        return;

    def numcourses(self):
        return len(self.courses)

### MAIN BODY ###

studentdict = {}
keepgoing = True
while keepgoing:
    nid = input("Enter student id: ")
    if nid not in studentdict.keys():
        print("Student NID not found.")
        ans = input("Would you like to add him/her/them? ")
        if ans.upper()[0] == "Y":
            newstudent = Student()
            inname = input("What is the student's name? ")
            inemail = input("What is the student's email? ")
            newstudent.name = inname
            newstudent.email = inemail
            studentdict[nid] = newstudent
    else:
        numcourses = studentdict[nid].numcourses()
        print(f"The student is taking {numcourses} courses.")
        ans = input("Would you like to add a course? ")
        if ans.upper()[0] == "Y":
            coursename = input("What course would you like to add? ")
            studentdict[nid].courses.append(coursename)
        print(f"Name: {studentdict[nid].name}")
        print(f"Email: {studentdict[nid].email}")
        print(f"Courses: {studentdict[nid].courses}")
    ans = input("Do you want to keep going? ")
    print()
    if ans.upper()[0] == "N":
        keepgoing = False
