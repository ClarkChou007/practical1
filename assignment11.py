sing = "   *   "
lshng = list(sing)
x = int(len(lshng)/2)
for i in range(0,int(len(lshng)/2)+1):
    lshng[x-i]="*"
    lshng[x+i]="*"

    star = "".join(lshng)
    print(star)
for j in range(0,int(len(lshng)/2)+1):
    lshng[j] = ' '
    lshng[len(lshng)-1-j] = ' '
    star = "".join(lshng)
    print(star)

