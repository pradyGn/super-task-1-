#!/usr/bin/env python
# coding: utf-8

# In[2]:


file_name = input("Input file name: " )
G = open(file_name,'r')
with open(file_name) as G:
    lines = G.readlines()
G.close()


# In[3]:


IN = []
i = 0

#print(lines)
for l in lines:
    i = i + 1
    if l[0] != '#' and l[0] != '\n':
        if i < len(lines):
            IN.append(l[:len(l)-1])
        else:
            IN.append(l)

#print(IN)


# In[4]:


def INP(IN):
    
    info_IN1 = []
    info_IN2 = []
    temp_cord = []

    for mem in IN:
        spc1 = mem.find(' ')
        spc2 = mem[spc1+1:].find(' ') + spc1 + 1
        
        if spc1 == spc2:
            for del_mem in IN[:IN.index(mem)]:
                #info_IN1.append(del_mem[0])
                IN.remove(del_mem)
            return info_IN2, info_IN1
        
        info_IN1.append(mem[:spc1])
    
        temp1 = 0
        temp2 = 0
    
        if (spc2 - spc1) == 2:
            temp1 = int(mem[spc1+1:spc2])
        else:
            l = spc2 - spc1 - 1
            i = 1
            for ele in mem[spc1+1:spc2]:
                temp1 = temp1 + (int(ele)*(10**(l-i)))
                i = i + 1
        info_IN2.append(temp1)
    
        if (len(mem) - spc2) == 2:
            temp2 = int(mem[spc2+1:])
        else:
            l = len(mem) - spc2 - 1
            i = 1
            for ele in mem[spc2+1:]:
                temp2 = temp2 + (int(ele)*(10**(l-i)))
                i = i + 1
        info_IN2.append(temp2)
            
            
#    print(IN)
#    print(info_IN1)
#    print(info_IN2)


# In[5]:


[OP, points] = INP(IN)

#print(IN)

cords = []
#print(OP)
#print(OP1)

for i in range(int(len(OP)/2)):
    cords.append([OP[2*i], OP[2*i+1]])

#print(cords)
#print(points)



# In[6]:


point_info = {}

for i in range (len(points)):
    point_info[points[i]] = cords[i]

#print(point_info)


# In[7]:


import math

start = input("Input start: ")
goal = input("Input goal: ")

temp_path = []
temp_pathD = {}
Path = []

l = len(start)

for E in IN:
    if E[:l] == start:
        temp_path.append(E)
        
def getKey(value):
    for key, val in temp_pathD.items():
        if value == val:
            return key
        
        
def ED (A, B):
    X = A[0] - B[0]
    Y = A[1] - B[1]
    X = X**2
    Y = Y**2
    return math.sqrt(X+Y)

while True:
    for ETP in temp_path:
        Val = 0
        
        spc = []
        spc.append(-1)
        for s in range (len(ETP)):
            if ETP[s] == " ":
                spc.append(s)
        spc.append(len(ETP)-1)
        
        for i in range (len(spc)-2):
            if i != len(spc)-3:
                Val = Val + ED(point_info[ETP[spc[i]+1:spc[i+1]]], point_info[ETP[spc[i+1]+1:spc[i+2]]])
            else:
                Val = Val + ED(point_info[ETP[spc[i]+1:spc[i+1]]], point_info[ETP[spc[i+1]+1:spc[i+2]+1]])
        temp_pathD[ETP] = Val
        
    print(temp_pathD)
        
    """    
        for i in range (2,len(ETP),2):
            Val = Val + ED(point_info[ETP[i-2]], point_info[ETP[i]])
        temp_pathD[ETP] = Val
        
    if len(Path) == 0:
        Path.append(min(temp_pathD.values()))
    else:
        Path[0] == Path[0] + min(temp_pathD.values())[-1]
    """
    Path.clear()
    Path.append(getKey(min(temp_pathD.values())))
    print("Choosing " + Path[0])
    
#    print(Path)
#    print(temp_pathD)
    

    del temp_pathD[getKey(min(temp_pathD.values()))]
    temp_path.clear()
    
    for E in IN:
        spc_E = E.find(" ")
        
        spc_P = []
        for s1 in range (len(Path[0])):
            if Path[0][s1] == " ":
                spc_P.append(s1)
        
        
        if E[:spc_E] == Path[0][spc_P[-1]+1:]:
            temp_path.append(Path[0] + " " + E[spc_E+1:])
    
    l1 = len(goal)
    if Path[0][len(Path[0]) - l1:] == goal:
        break
                                 
        
print("Solution " + Path[0])                            
            
    
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




