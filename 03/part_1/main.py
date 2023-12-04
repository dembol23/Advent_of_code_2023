f = open("input.txt", "r")
sum = 0
rows = []
for x in f:
    rows.append(x)
def hasspecial(Yindex,Xindex):
    specials = "*@#$+%/&=-"
    if Yindex==0:
        if rows[Yindex][Xindex-1] in specials or rows[Yindex][Xindex+1] in specials or rows[Yindex+1][Xindex-1] in specials or rows[Yindex+1][Xindex] in specials or rows[Yindex+1][Xindex+1] in specials:
            return True
    elif Yindex==len(rows)-1:
        if rows[Yindex][Xindex-1] in specials or rows[Yindex][Xindex+1] in specials or rows[Yindex-1][Xindex-1] in specials or rows[Yindex-1][Xindex] in specials or rows[Yindex-1][Xindex+1] in specials:
            return True
    else:
        if rows[Yindex-1][Xindex-1] in specials or rows[Yindex-1][Xindex] in specials or rows[Yindex-1][Xindex+1] in specials or rows[Yindex][Xindex-1] in specials or rows[Yindex][Xindex+1] in specials or rows[Yindex+1][Xindex-1] in specials or rows[Yindex+1][Xindex] in specials or rows[Yindex+1][Xindex+1] in specials:
            return True
number = ''
isPart = False
for Yindex,z in enumerate(rows):
    for Xindex,x in enumerate(z):
        if x.isdigit():
            number+=x
            if hasspecial(Yindex,Xindex):
                isPart=True
        else:
            if isPart:
                sum+=int(number)
                print(number)
                isPart = False
            number=''
print(sum)