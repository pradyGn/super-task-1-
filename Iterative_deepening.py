#!/usr/bin/env python
# coding: utf-8

# In[18]:


file_name = input("Enter file name: ")
G = open(file_name,'r')
with open(file_name) as G:
    lines = G.readlines()
G.close()


# In[19]:


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


# In[20]:


IN.sort()


# In[ ]:





# In[21]:


def getE_till_D(IN_ID, depth, start):
    
    if depth == 0:
        print("depth cannot be 0")
        return
    
    IN_D = []
    
    for E in IN_ID:
        spc = E.find(' ')
        if E[:spc] == start:
            IN_D.append(E)
            IN_ID[IN_ID.index(E)] = ' '
    
    
    for var in range(1, depth):
        temp_list = []
        for E_D in IN_D:                         #iterates over seld_IN
            spc1 = E_D.find(' ')
            for E_IN in IN_ID:                  #for each E_seld iterates over IN
                spc2 = E_IN.find(' ')
                if E_D[spc1+1:] == E_IN[:spc2]:    #appends end elements of an edge in temp_list
                    temp_list.append(E_IN)
                    IN_ID[IN_ID.index(E_IN)] = ' '    #removes these elements from IN and replaces with ' '
                        
        for mem in temp_list:
            IN_D.append(mem)
            
    return IN_D


# In[ ]:





# In[22]:


def DFS(IN, start, goal, depth):
    
    path = []
    
    d = 1
    
    if len(path) == 0:
        for E in IN:
            spc = E.find(' ')
            if E[:spc] == start:
                path.append(E)
                IN.remove(E)
                break
    
    while True:
#        print(len(IN))
        if len(IN) == 0:
            return "None"
        
        if len(path) == 0:
            for E in IN:
                spc = E.find(' ')
                if E[:spc] == start:
                    path.append(E)
                    d = d + 1
                    IN.remove(E)
                    break
        
        spc1 = path[-1].find(' ')
        
        if path[-1][spc1+1:] == goal:
            print("Goal reached!")
            return path
        
        check = 0
        for E in IN:
            spc2 = E.find(' ')
            if path[-1][spc1+1:] == E[:spc2]:
                path.append(E)
                d = d + 1
                IN.remove(E)
                check = check + 1
                break
        
        spc1 = path[-1].find(' ')
        
        if path[-1][spc1+1:] == goal:
            print("Goal reached!")
            return path
        
        if check == 0 or d == depth:
            spc1 = path[-1].find(' ')
            print("Depth reached at: " + path[-1][spc1+1:])
            path.remove(path[-1])
            d = d - 1
            


# In[ ]:





# In[23]:


def ID(IN):
    
    start = input("Enter starting point: " )
    goal = input("Enter goal point: " )
    
    depth = 1
    while True:
        IN_ID = IN.copy()
        new_IN_ID = getE_till_D(IN_ID, depth, start)
        print("At depth:" , depth)
#        print(depth)
#        print(new_IN_ID)
        path = DFS(new_IN_ID, start, goal, depth)
        depth = depth + 1
        
        spc = path[-1].find(' ')
        if path[-1][spc+1:] == goal:
            temp = start
            for E in path:
                spc = E.find(' ')
                temp = temp + '->' + E[spc+1:]
            return temp
    


# In[24]:


IN_copy = IN.copy()
path = ID(IN_copy)
print(path)


# In[ ]:





# In[ ]:





# In[ ]:




