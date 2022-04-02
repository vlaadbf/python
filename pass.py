import random
from random import choice
def gen():
    level=input("cate de lunga doresti sa fie parola?(easy,med,strong):")
    easylist=["ou","mic","lac"]
    medlist=["mancare","grupa","vesnicie"]
    if level=="easy":
        n=random.randint(1000,9999)
        s=(random.choice(easylist))
        print(s,n,sep="")
    else:
            if level=="med":
            
             n = random.randint(100000,999999)

             s = ((random.choice(medlist)))
             res = ''.join(choice((str.upper, str.lower))(char) for char in s)
            
             print (str(res) , n , sep='')

gen()



#a="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = 8
#p =  "".join(random.sample(a,passlen ))
#print(p)