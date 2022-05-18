import random
import time


def rgn_n():
    x = 1000000 * random.random()
    ts = time.time()
    ans = int(x * ts)
    return ans


at = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
bt = "A B C D E G F H I J K L M N O P Q R S T U V W X Y Z"
ct = "1 2 3 4 5 6 7 8 9 0"
dt = "# $"

a = at.split()
b = bt.split()
c = ct.split()
d = dt.split()

mix = []
mix.extend(a)
mix.extend(b)
mix.extend(c)
mix.extend(d)

ans = []

n = 8               #Enter the length of password

ans.append(a[rgn_n() % (len(a))])
ans.append(b[rgn_n() % (len(b))])
ans.append(c[rgn_n() % (len(c))])
ans.append(d[rgn_n() % (len(d))])

for i in range(n-4):
    ans.append(mix[rgn_n() % len(mix)])

random.shuffle(ans)

for x in ans:
    print(x, end='')


##These are changes made on 18-05-22



