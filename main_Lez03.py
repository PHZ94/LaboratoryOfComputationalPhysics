# even the heaven shall burn as we gather
# Lezione 03
# LaboratoryOfComputationalPhysics

# ---- I C E _ B R E A K I N G _ S M A L L T A L K -------------

print("Blyat")
import time


# --------------------------------------------------------------

print("Es 1\n\n")
# Es 1.1 -------------------------------------------------------

print("Es 1.1\n\n")
start = time.time()
ans = []
for i in range(3):
    for j in range(4):
        ans.append((i, j))
    #enddo
#enddo
finish = time.time()

print("For espliciti: \n", ans, "\nin ", finish-start, " s.")

start = time.time()
ans = [(i, j) for i in range(3) for j in range(4)]
finish = time.time()

print("List comprehension: \n", ans, "\nin ", finish-start, " s.")


# Es 1.2 -----------------------------
print("Es 1.2\n\n")

ans = map(lambda x: x*x , filter(lambda x: x % 2 == 0, range(5)))
print(list(ans))

ansia = []
for x in range(5):
    if x % 2 == 0:
        ansia.append(x**2)
    #endif
#enddo
print(ansia)

print("\n\nAncora un esperimento\n\n")

def Blyat(x):
    return x + 3
#enddef

trial = [i for i in range(20)]
print(trial)
ris = map(Blyat, trial)
print(list(ris))


# se volessimo metterci un filtro?
# quella della sigaretta che mi fumo oraaaa ==== ???


# qui torna molto molto comoda la lambda
ris = map(Blyat, filter(lambda n : n % 2 == 0 , trial))
print(list(ris))
'''
ris = map(Blyat, filter(lambda n : n % 2 == 0 , lambda x : x + 3 for x in trial))
print(list(ris))
nice try whatsoever
'''


# Es 2 ---------------------------------------------
print("Es 2\n\n")

x = 5
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1,2,3]
ans = f(alist)
print("Trial 1\n")
print (ans)
print (alist) 

adahList = [2,3,4]
def ff(alist):
    listToModify = []
    listToModify = alist
    for i in range(x):
        listToModify.append(i)
    #enddo
    return listToModify
#enddef

ansya = ff(adahList)
print("Trial 2\n")
print(ansya)
print(adahList)
