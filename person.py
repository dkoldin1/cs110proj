class Person3:
    def __init__(self,name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20):
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
        self.q11=q11
        self.q12=q12
        self.q13=q13
        self.q14=q14
        self.q15=q15
        self.q16=q16
        self.q17=q17
        self.q18=q18
        self.q19=q19
        self.q20=q20

    def __str__(self):
    	return str(self.q1)+str(self.q2)+str(self.q3)+str(self.q4)+str(self.q5)+str(self.q6)+str(self.q7)+str(self.q8)+str(self.q9)+str(self.q10)+str(self.q11)+str(self.q12)+str(self.q13)+str(self.q14)+str(self.q15)+str(self.q16)+str(self.q17)+str(self.q18)+str(self.q19)+str(self.q20)

    @classmethod
    def from_input(cls):
        return cls(
        #name
            input('Name: '),
            #1
            input('Gender:'),
            #2
            input('State Abbreviation: '),
            #3
            int(input('Age: ')),
            #4
            input('Do you have any dietary restirctions be it from allergies or personal choice? (y or n) '),
            #5
            int(input('At about what hour do you go to sleep?')),
            #6
            int(input('At about what hour do you wake up?')),
            #7
            input('Do you smoke? (y or n)'),
            #8
            int(input('If you workout, about how many hours a week do you spend doing so?')),
            #9
            int(input('Which desribes you best:,(1) Complete mess,(2)Sometimes messy but relatively organized,(3) Pretty Tidy,(4)Neat Freak')),
            #10
            input('Do you consider yourself a light sleeper? (y or n)'),
            #11
            input('Do you have and/or want pets? (y or n)'),
            #12
            int(input('Which do you prefer?,(1) Quiet living space,(2) Noisy living space, (3) Some combination of the two')),
            #13
            input('Do you have a significant other? If no, do you plan on having over night guests of any kind? (y or n)'),
            #14
            input('Do you mind if your roommate has frequent over night guests? (y or n)'),
            #15
            input('Do you mind if your roommate has frequent day time guests if they leave at what you consider to be an approproate time? (y or n)'),
            #16
            int(input('Are you willing to split the grocery bill? If Yes, how much do you usually spend on groceries a month? If no write "0".')),
            #17
            int(input('Where would you like to live?,(1)Near a big city,(2)Suburbs,(3)Rural area')),
            #18
            input('Are you willing to split chores in shared living spaces? (y or n)'),
            #19
            input('Are you willing/expecting to share personal items such as clothes, cleaning supplies, etc? (y or n)'),
            #20
            int(input('How much are you looking to spend on rent, including utilities, per month?'))
            )

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
        if(self.q11==date.q11):
            num+=1
        if(self.q12==date.q12):
            num+=1
        elif(self.q12==3):
            num+=(1/2)
        elif(date.q12==3):
            num+=(1/2)
        else:
            num+=0
        if(self.q13==date.q13):
            num+=1
        if(self.q14==date.q14):
            num+=2
        else:
            num+= -1
        if(self.q15==date.q15):
            num+=1
        if(self.q16==date.q16):
            num+=2
        elif(self.q16>date.q16):
            num+=(date.q16/self.q16)
        elif(date.q16>self.q16):
            num+=(self.q16/date.q16)
        if(self.q17==date.q17):
            num+=1
        elif(self.q17>date.q17):
            num+=(self.q17 - date.q17)
        elif(date.q17>self.q17):
            num+=(date.q17 - self.q17)
        if(self.q18==date.q18):
            num+=1
        if(self.q19==date.q19):
            num+=2
        if(self.q20==date.q20):
            num+=5
        elif(self.q20>date.q20):
            num+=(date.q20/self.q20)
        elif(date.q20>self.q20):
            num+=(self.q20/date.q20)


        return str(((10000*(num/20))//1)/100)+"% Match"

def main():

        adam = Person3.from_input()
        barb = Person3.from_input()

        print(adam)
        print(adam.match(barb))

main()
