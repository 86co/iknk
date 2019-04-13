operatorchar={
    0: '+',
    1: '*',
    2: '-',
    3: '-',
    4: '/',
    5: '/'
}

import re

def main():
    a, b, c, d = handle_input()
    maketen(a,b,c,d)
    
def handle_input():
    while True:
        numlist = re.findall(r'([\d])', input())
        numlist = [int(num) for num in numlist]
        if len(numlist)==4:
            return numlist

def maketen(a, b, c, d):
    numlist = [a,b,c,d]

    anslist=[]
    flag0list = []
    flag1list = []
    for i1 in range(3):
        for i2 in range(i1+1, 4):
            for i3 in [i for i in range(4) if i not in {i1, i2}]:
                i4 = 6 - i1 - i2 - i3
                n1, n2, n3, n4 = numlist[i1], numlist[i2], numlist[i3], numlist[i4]
                res1list = binary(n1, n2)
                for o1 in range(6):
                    res1 = res1list[o1]
                    if res1 == None or res1 < 0: continue
                    res2list = binary(res1, n3)
                    for o2 in range(6):
                        res2 = res2list[o2]
                        if res2 == None or res2 < 0: continue
                        res3list = binary(res2, n4)
                        for o3 in range(6):
                            res3 = res3list[o3]
                            if res3 == 10:
                                anslist.append(output1(n1, n2, n3, n4, o1, o2, o3))
            i3 = [i for i in range(4) if i not in {i1, i2}][0]
            i4 = 6 - i1 - i2 - i3
            n1, n2, n3, n4 = numlist[i1], numlist[i2], numlist[i3], numlist[i4]
            res1list = binary(n1, n2)
            for o1 in range(6):
                res1 = res1list[o1]
                if res1 == None or res1 < 0: continue
                res2list = binary(n3, n4)
                for o2 in range(6):
                    res2 = res2list[o2]
                    if res2 == None or res2 < 0: continue
                    res3list = binary(res1, res2)
                    for o3 in range(6):
                        res3 = res3list[o3]
                        if res3 == 10:
                            anslist.append(output2(n1, n2, n3, n4, o1, o2, o3))

    anslist = set(anslist)
    for ans in anslist:
        print(ans)

def binary(a,b):
    retlist = [a+b, a*b, a-b, b-a, a/b if b not in {0,1} else None, b/a if a not in {0,1} else None]
    return retlist

def output1(n1, n2, n3, n4, o1, o2, o3):
    if o1 in {0,1,2,4}:
        if (o1 in {0,2} and o2 in {1,3,4,5}) or (o1 == 4 and o2 == 5):
            str1= "({} {} {})".format(str(n1), operatorchar[o1], str(n2))
        else:
            str1= "{} {} {}".format(str(n1), operatorchar[o1], str(n2))
    else:
        if o1 == 3 and o2 in {1,3,4,5}:
            str1= "({} {} {})".format(str(n2), operatorchar[o1], str(n1))
        else:
            str1= "{} {} {}".format(str(n2), operatorchar[o1], str(n1))
    
    if o2 in {0,1,2,4}:
        if (o2 in {0,2} and o3 in {1,3,4,5}) or (o2 == 4 and o3 == 5):
            str2= "({} {} {})".format(str1, operatorchar[o2], str(n3))
        else:
            str2= "{} {} {}".format(str1, operatorchar[o2], str(n3))
    else:
        if o2 == 3 and o3 in {1,3,4,5}:
            str2= "({} {} {})".format(str(n3), operatorchar[o2], str1)
        else:
            str2= "{} {} {}".format(str(n3), operatorchar[o2], str1)
    
    if o3 in {0,1,2,4}:
        str3= "{} {} {}".format(str2, operatorchar[o3], str(n4))
    else:
        str3= "{} {} {}".format(str(n4), operatorchar[o3], str2)
        
    str4 = "{} = 10".format(str3)
    return str4

def output2(n1, n2, n3, n4, o1, o2, o3):
    if o1 in {0,1,2,4}:
        if (o1 in {0,2} and o3 in {1,3,4,5}) or (o1 == 4 and o3 == 5):
            str1= "({} {} {})".format(str(n1), operatorchar[o1], str(n2))
        else:
            str1= "{} {} {}".format(str(n1), operatorchar[o1], str(n2))
    else:
        if o1 == 3 and o3 in {1,3,4,5}:
            str1= "({} {} {})".format(str(n2), operatorchar[o1], str(n1))
        else:
            str1= "{} {} {}".format(str(n2), operatorchar[o1], str(n1))
    
    if o2 in {0,1,2,4}:
        if (o2 in {0,2} and o3 in {1,2,4,5}) or (o2 == 4 and o3 == 5):
            str2= "({} {} {})".format(str(n3), operatorchar[o2], str(n4))
        else:
            str2= "{} {} {}".format(str(n3), operatorchar[o2], str(n4))
    else:
        if o2 == 3 and o3 in {1,2,4,5}:
            str2= "({} {} {})".format(str(n4), operatorchar[o2], str(n3))
        else:
            str2= "{} {} {}".format(str(n4), operatorchar[o2], str(n3))
    
    if o3 in {0,1,2,4}:
        str3= "{} {} {}".format(str1, operatorchar[o3], str2)
    else:
        str3= "{} {} {}".format(str2, operatorchar[o3], str1)
        
    str4 = "{} = 10".format(str3)
    return str4
    
if __name__ == "__main__":
    main()