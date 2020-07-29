
class SE:
    total_count = int(input("Enter the total number of students in second year: "))
    c_count = int(input("Enter the number of students who play Cricket: "))
    b_count = int(input("Enter the number of students who play Badminton: "))
    f_count = int(input("Enter the number of students who play Football: "))
    c_list = []
    b_list = []
    f_list = []
    print("Give the names of the students,playing Cricket ")
    for i in range(0,c_count):
        elem = input("Enter the name of students who play Cricket: ")
        c_list.append(elem)
    print("Give the names of the students,playing Badminton ")
    for j in range(0,b_count):
        elem1 = input("Enter the name of students who play Badminton: ")
        b_list.append(elem1)
    print("Give the names of the students,playing Football ")
    for k in range(0,f_count):
        elem2 = input("Enter the name of students who play Football: ")
        f_list.append(elem2)
    def Both_Cricket_Badminton(self):
        c_and_b_list = []
        [c_and_b_list.append(i) for i in SE.c_list for j in SE.b_list if i==j]
        print("list of students who play both Cricket and Badminton: ",c_and_b_list)
    def Cricket_or_Badminton_NotBoth(self):
        c_or_b_notboth = []
        [c_or_b_notboth.append(i) for i in SE.c_list if i not in SE.b_list]
        [c_or_b_notboth.append(i) for i in SE.b_list if i not in SE.c_list]
        print("List of students who play either Cricket or Badminton but not both: ",c_or_b_notboth)
    def Only_Football(self):
        no_c_no_b=[]
        [no_c_no_b.append(i) for i in SE.f_list if i not in SE.c_list if i not in SE.b_list]
        print("Number of students who play neither Cricket nor Badminton: ",len(no_c_no_b))
    def Both_Cricket_Football_NO_Badminton(self):
        c_and_f_no_b = []
        [c_and_f_no_b.append(i) for i in SE.f_list if i in SE.c_list if i not in SE.b_list]
        print("Number of students who play Cricket and Football but not Badminton: ",len(c_and_f_no_b))

s = SE()
s.Both_Cricket_Badminton()
s.Cricket_or_Badminton_NotBoth()
s.Only_Football()
s.Both_Cricket_Football_NO_Badminton()















'''
class cls:
    grp_A = []
    grp_B = []
    grp_C = []
    AandB = []

    total_count = 0
    A_count = 0
    B_count = 0
    C_count = 0
    def __init__(self):
        self.fav_games = []
        cls.total_count +=1
        self.name = input("Enter the Name of student: ")
        self.n = int(input("Enter the number of games played by student: "))
        for i in range(0,self.n):
            elem = input("Enter the game(Cricket/Badminton/Football): ")
            self.fav_games.append(elem)
        self.create_list()
    def create_list(self):

        for i in self.fav_games:
            if i == 'Cricket':
                cls.grp_A.append(self.name)
                cls.A_count += 1
            elif i == 'Badminton':
                cls.grp_B.append(self.name)
                cls.B_count += 1
            else:
                cls.grp_C.append(self.name)
                cls.C_count += 1
        for i in cls.grp_A:
            if i in cls.grp_B:
                cls.AandB.append(i)
        AunionB = cls.grp_A + cls.grp_B
        AorBnotC = []
        [AorBnotC.append(x) for x in AunionB if x not in AorBnotC]
        onlyC=[]
        [onlyC.append(i) for i in cls.grp_C if i not in cls.grp_B if i not in cls.grp_A]
        '''