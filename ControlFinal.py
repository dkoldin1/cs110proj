import tkinter
from tkinter import *


def callback():
    mylist=(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),E9.get(),E10.get())
    print(mylist)
    return mylist
top = Tk()
L1 = Label(top, text='Name: ')
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)

L2 = Label(top, text='Gender:')
L2.grid(row=1, column=0)
E2 = Entry(top, bd = 5)
E2.grid(row=1, column=1)

L3 = Label(top, text='State Abbreviation: ')
L3.grid(row=2, column=0)
E3 = Entry(top, bd = 5)
E3.grid(row=2, column=1)

L4 = Label(top, text='Age: ')
L4.grid(row=3, column=0)
E4 = Entry(top, bd = 5)
E4.grid(row=3, column=1)

L5 = Label(top, text='Do you have any dietary restirctions be it from allergies or personal choice? (y or n) ')
L5.grid(row=4, column=0)
E5 = Entry(top, bd = 5)
E5.grid(row=4, column=1)

L6 = Label(top, text='At about what hour do you go to sleep?')
L6.grid(row=5, column=0)
E6 = Entry(top, bd = 5)
E6.grid(row=5, column=1)

L7 = Label(top, text='At about what hour do you wake up?')
L7.grid(row=6, column=0)
E7 = Entry(top, bd = 5)
E7.grid(row=6, column=1)

L8 = Label(top, text='Do you smoke? (y or n)')
L8.grid(row=7, column=0)
E8 = Entry(top, bd = 5)
E8.grid(row=7, column=1)

L9 = Label(top, text='If you workout, about how many hours a week do you spend doing so?')
L9.grid(row=8, column=0)
E9 = Entry(top, bd = 5)
E9.grid(row=8, column=1)

L10 = Label(top, text='Which desribes you best:,(1) Complete mess,(2)Sometimes messy but relatively organized,(3) Pretty Tidy,(4)Neat Freak')
L10.grid(row=9, column=0)
E10 = Entry(top, bd = 5)
E10.grid(row=9, column=1)

MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=11, column=1)

mylist2=callback()

top.mainloop()

class person:
    def __init__(self,name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
        self.name=name
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5
        self.q6=q6
        self.q7=q7
        self.q8=q8
        self.q9=q9
        self.q10=q10

    def __str__(self):
    	return str(self.q1)+str(self.q2)+str(self.q3)+str(self.q4)+str(self.q5)+str(self.q6)+str(self.q7)+str(self.q8)+str(self.q9)+str(self.q10)

    @classmethod
    def from_input(cls):
        return cls(
        #name
            mylist2[0],
            #1
            mylist2[1],
            #2
            mylist2[2],
            #3
            int(mylist2[3]),
            #4
            mylist2[4],
            #5
            int(mylist2[5]),
            #6
            int(mylist2[6]),
            #7
            mylist2[7],
            #8
            int(mylist2[8],
            #9
            int(mylist2[9])))

    def match(self, date):
        num=0
        #if(self.q1a==date.q1a)
        #    print("name buddies")
        if(self.q1==date.q1):
            num+=1
        if(self.q2==date.q2):
            num+=1
        if(self.q3>date.q3):
            num+=(date.q3/self.q3)
        else:
            num+=(self.q3/date.q3)
        if(self.q4==date.q4):
            num+=1
        if(self.q5==date.q5):
            num+=1
        elif(self.q5>date.q5):
            num+=(date.q5/self.q5)
        elif(date.q5>self.q5):
            num+=(date.q5/self.q5)
        if(self.q6==date.q6):
            num+=1
        elif(self.q6>date.q6):
            num+=(date.q6/self.q6)
        elif(date.q6>self.q6):
            num+=(self.q6/date.q6)
        if(self.q7==date.q7):
            num+=2
        else:
            num+= -1
        if(self.q8>date.q8):
            num+=(date.q8/self.q8)
        elif(date.q8>self.q8):
            num+=(date.q8/self.q8)
        elif(self.q8==date.q8):
            num+=1
        if(self.q9<date.q9):
            num+=(date.q9/self.q9)
        elif(date.q9>self.q9):
            num+=(self.q9/date.q9)
        if(self.q10==date.q10):
            num+=1

        return str(((10000*(num/40))//1)/100)+"% Match"

def main():
        print(mylist2)
        adam = person.from_input()
        #barb = person.from_input()

        print(adam)
        #print(adam.match(barb))

main()
