from random import shuffle
import os
class question:
    def __init__(self,id,desc,options,answer):
        self.id=id
        self.desc=desc
        self.options=options
        self.answer=answer
#預先處理成5行一組
separate=[]
with open('file.txt','r',encoding='utf-8') as f:
    tmp=[]
    arr=f.readlines().copy()
    for i in range(len(arr)):
        if i%5==0  and i !=0:
            separate.append(tmp.copy())
            tmp.clear()
        tmp.append(arr[i])
while True:
    shuffle(separate)
    #去除\n組成問題
    questions=[]
    id=1
    for s in separate:
        ans=""
        for i in range(1,5):
            if s[i][1]==s[0][0]:
                ans=s[i][3:-1]
        options=[s[1][3:-1],s[2][3:-1],s[3][3:-1],s[4][3:-1]]
        shuffle(options)
        questions.append(question(id,s[0][1:],options,ans))
        id+=1
    while True:
        print("總共有",len(questions),"題","要寫幾題")
        try:
            numbers=int(input())
            if 0<numbers<=len(questions):
                break
            else:
                print("沒這麼多題可以寫")
        except:
            pass
    questions=questions[0:numbers]

    incorrect=[]
    for i in questions:
        while True:
            print(i.id,end=".")
            print(i.desc,end="")
            qid=1
            for j in i.options:
                print(" ",str(qid)+"."+j)
                qid+=1
            user=input()
            if user in ["1",'2','3','4']:
                user=i.options[int(user)-1]
                break
        if user!=i.answer:
            i.user=user
            incorrect.append(i)
    print((len(questions)-len(incorrect))/len(questions)*100,"分")
    for i in incorrect:
        print("檢討時間")
        print(i.id,end=".")
        print(i.desc)
        print("你選了:",i.user,"但答案應該是:",i.answer)
        print()
    print("還要寫嗎?Y/N")
    if input()!="Y":
        break
