def logical(s):
    sp = s.split("or")
    l=[]
    for i in sp:
        r =i.replace("(","")
        r =r.replace(")","")
        r =r.replace("and",",")
        l.append([r])
    print(l)
    
s="(A and B) or (C and D) or E or F"  #give input here

logical(s)
