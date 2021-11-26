#13 zadatak 21oct2021
str = "testiramo sto sve mozemo napraviti sa stringovima"
rijec= "string"
gdje_je = str.find(rijec)

if gdje_je != -1:
    print(gdje_je)                                              #trazimo rijec
    print(str[gdje_je:gdje_je+len(rijec)])

import string
for x in string.ascii_letters:                          #trazimo zadnje slovo u rijeci
    if str.endswith(x):
        print(x)




#%%
l=[4,3,2,1]
for i in l:
    print(i)

for i in range(len(l)):
    print(i)
    for i in l:
        print(i)



#%%
matrix=[]
for i in range(5):
    l=[]
    for j in range(5):
        l.append(j)
    matrix.append(l)
print(matrix)



#%%
matrix = [[j for j in range(5)]for i in range(5)]
print(matrix)



# %%
matrix=[[1,2,3],[4,5],[6,7,8,9]]
flat_list=[]
for sublist in matrix:        #spajanje listi u jednu
    for item in sublist:
        flat_list.append(item)
print(flat_list)

flat_list=[item for sublist in matrix for item in sublist]
print(flat_list)






#%%
#23
l=[1,2,3,4]
print(l*5)
print([l]*3)






#%%
def pyramid(x):
    l=[]
    for i in range(1,x+1): 
        l.append([1]*i)
        print(l)
pyramid(4)





# %%
def my_sum(a:int,b:int):
    return a + b

print(my_sum("a","b"))

x = isinstance(5,int)
x = isinstance(5,str)





#%%
l=[1,2,3,4]    #iterable kao parametar
def my_sum(*args):
    rez = 0
    for x in args:
        rez +=x
    return rez
print(my_sum)





# %%
def concatenate(**kwargs):
    result=""
    for arg in kwargs.values():
        result += arg + " "
    return result, kwargs.keys()
print(concatenate(a="AI", b="Centar",c="Lipik"))

_,keys =concatenate(a="AI", b="Centar",c="Lipik")
print(keys)
# %%
