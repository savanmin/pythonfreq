class students:
    id = False
    fname = False
    lname = False
    std = False
    mark = False
    school = False

    def __init__(self, id, fname, lname, std, mark, school):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.std = std
        self.mark = mark
        self.school = school
#
#     def details(self):
#         print(self.fname, self.lname, "\'s full details are as below:\n")
#
#         print("Id           :", self.id)
#         print("Standard     :", self.std)
#         print("Marks scored :", self.mark)
#         print("School       :", self.school)
#
#     def fullname(self):
#         print("Students\'s fullname is : ", (self.fname), (self.lname))
#
#
# st1 = students(100, "Savan", "Minsariya", 10, 50, "Saint thomas school")
# st2 = students(100, "Bitu", "vaishnav", 11, 98, "Saint thomas school")
# st3 = students(100, "Hardik", "goswami", 12, 99, "Saint thomas school")
#
# # st1.details()
# #
# # st2.fullname()
