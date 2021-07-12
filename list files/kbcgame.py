question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling","Tourism", "Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)

correctans=[3,4,1]
amount=[5000,10000,50000]
ans=["seven","Delhi","Software Engineering"]
print("welcome in KBC")
i=0
count=0
while i<len(question_list):
    m=question_list[i]
    print(m)
    j=0
    k=i
    while j<len(options_list[i]):
        n=options_list[k][j]
        print(j+1,n)
        j=j+1
    userinput=input("do you wants to use 5050 laifeline").lower()
    if userinput=="yes":
        print("50-50")
        if count==0:
            print(1,options_list[i][i])
            print(2,ans[i])
            count=count+1
            userinput3=int(input("chosse the answer"))
            if userinput3==2:
                print("your answer is correct you won amount",amount[i])
    
            else:
                print("wrong you dropped out the game")
                break
        else:
            print("you can't use more life line")
            userinput2=int(input("choose the answer"))
            if userinput2==correctans[i]:
                print("your answer is correct you won",amount[i])
            else:
                print("your answer is wrong you dropped out the game ")
                break
    else: 
        userinput3=int(input("choose the answer"))
        if userinput3==correctans[i]:
            print("your answer is correct you won ",amount[i])
        else:
            print("your answer is wrong,you dropped out the game")
            break
    i=i+1