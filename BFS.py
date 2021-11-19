#!/usr/bin/env python
# coding: utf-8

# In[13]:


file_name = input("Enter file name with extension: ")
G = open(file_name,'r')
with open(file_name) as G:
    lines = G.readlines()
G.close()


# In[14]:


IN = []
i = 0

#print(lines)
for l in lines:
    i = i + 1
    if l[0] != '#' and l[0] != '\n':
        spc = l.find(' ')
        if not l[spc+1:spc+2].isdigit():  
            if i < len(lines):
                IN.append(l[:len(l)-1])
            else:
                IN.append(l)

#print(IN)


# In[15]:


IN.sort()
#print(IN)


# In[16]:


def BFS(IN, depth):

    Path = []
    
    Visited_list = []
    
    Start = input("Enter starting point: ")
    Goal = input("Enter ending point: ")
    
    l = len(Start)
    l1 = len(Goal)
    
    print("Expanding: " + Start)
    
    for E_main in IN:                                #iterating over each edge in input
        if E_main[:l] == Start:
            if E_main[:l] not in Visited_list:
                Visited_list.append(Start)           #appending start to visited list (VS)
            Path.append(E_main)                      #appending current edge to Path
            IN[IN.index(E_main)] = '*'               #erasing the added edge (to Path) from input
            
            spc = E_main.find(' ')
            if E_main[spc+1:] not in Visited_list:
                Visited_list.append(E_main[spc+1:])
                print("Expanding: " + E_main[spc+1:])
    
    temp_PathEx = []

    for d in range (depth):
        for E in Path:
            spc1 = []
            for y in range (len(E)):
                if E[y] == ' ':
                    spc1.append(y)
            
            if E[spc1[-1]+1:] == Goal:
                return E
    
        for i in range (len(Path)):
            
            spc2 = []
            for x in range (len(Path[i])):
                if Path[i][x] == ' ':
                    spc2.append(x)
            
            for j in range (len(IN)):
                if IN[j] != '*':
                    spc3 = IN[j].find(' ')
                    if Path[i][spc2[-1]+1:] == IN[j][:spc3] and IN[j][spc3+1:] not in Visited_list:
                        temp = Path[i] + ' ' + IN[j][spc3+1:]
                        Visited_list.append(IN[j][spc3+1:])
                        if IN[j][spc3+1:] != Goal:
                            print("Expanding: " + IN[j][spc3+1:])
                        temp_PathEx.append(temp)
                        IN[j] = '*'
        
        for newpaths in temp_PathEx:
            Path.append(newpaths)
        temp_PathEx = []


# In[17]:


depth = 4

path = BFS(IN, depth)

print(path)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




