class student:
    def __init__(self):
        self.name=''
        self.student=[]
    def setinfo(self):
        for x in range(5):
            di={}
            self.marks=[]
            no=0
            self.name=input('please enter name')
            for y in range(3):
                no=int(input('eneter marks'))
                self.marks.append(no)
                di[self.name]=self.marks
                self.student.append(di)
    def getinfo(self):
        di={}
        for x in self.student:
            print(x.keys())
            print(x.values())        
ob=student()
ob.setinfo()
ob.getinfo()
