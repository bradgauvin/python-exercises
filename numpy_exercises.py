#!/usr/bin/env python
# coding: utf-8

# # numpy_exercises

# ## Use the following code for the questions below:

# In[2]:


import numpy as np


# In[3]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?
# 2. How many positive numbers are there?
# 3. How many even positive numbers are there?
# 4. If you were to add 3 to each data point, how many positive numbers would there be?
# 5. If you squared each number, what would the new mean and standard deviation be?
# 

# In[6]:


#1 
print(len(a[a< 0]))


# In[7]:


#2
print(len(a[a>0]))


# In[8]:


#3
print(len(a[(a>0) & (a%2==0)]))


# In[11]:


#4
a +=3
print(len(a[(a>0) & (a%2==0)]))
a


# In[14]:


#5
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a.mean())
print(a.std())
a=a**2
print(a.mean())
print(a.std())


#  6. A common statistical operation on a dataset is centering. 
# - This means to adjust the data such that the mean of the data is 0. 
# - This is done by subtracting the mean from each data point. Center the data set. 
# - See this link for more on centering.
#  7. Calculate the z-score for each data point. Recall that the z-score is given by:
# - Z =(x−μ)/σ
#  8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[19]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

cent=a-a.mean()
print(cent)


# In[20]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a=cent/a.std()
print(a)


# ## import numpy as np
# # Life w/o numpy to life with numpy
# 
# ## Setup 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# ### Use python's built in functionality/operators to determine the following:
# ### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# 
# ### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# 
# ### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 
# ### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 
# ### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
# 
# ### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# 
# ### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# 
# ### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
# 
# ### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...

# In[21]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[26]:


sum_of_a = sum(a)
print(sum_of_a)


# In[28]:


min_of_a = min(a)
print(min_of_a)


# In[30]:


max_of_a = max(a)
print(max_of_a)


# In[33]:


import numpy as np


# In[34]:


mean_a = a.mean()
print(mean_a)


# In[35]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# In[36]:


mean_a = a.mean()
print (mean_a)


# In[37]:


import math
product_a = math.prod(a)
print(product_a)


# In[38]:


square_a = a**2
print(square_a)


# In[41]:


# attempt 1
odd_a = [n for n in a if n % 2 != 0]
print(odd_a)


# In[43]:


evens_a = [n for n in a if n%2==0]
print(evens_a)


# # Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# - b = [
# -   [3, 4, 5],
# -   [6, 7, 8]
# - ]
# 
# ### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
# 
# ### Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
# 
# ### Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
# 
# 
# ### Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
# 
# ### Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
# 
# # Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
# 
# 
# ### Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# 
# 
# ### Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
# 
# ### Exercise 9 - print out the shape of the array b.
# 
# ### Exercise 10 - transpose the array b.
# 
# ### Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
# 
# ### Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
# 

# In[71]:


#1
b = np.array ([
    [3, 4, 5],
    [6, 7, 8]
])


# In[48]:


#2
sum_b = b.sum()
print(sum_b)


# In[49]:


#n/a - got carried away
min_b = b.min()
print(min_b)


# In[50]:


#3
max_b = b.max()
print(max_b)


# In[51]:


#4
mean_b = b.mean()
print(mean_b)


# In[55]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
prod_b = np.prod(b)
print(prod_b)


# In[54]:


#6
square_b = np.square(b)
print(square_b)


# In[69]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
mask_even = b % 2 != 0
mask_even
b[mask_even]


# In[76]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
print(b)
mask_odd = b % 2 == 0
b[mask_odd]


# In[77]:


# 9 Exercise 9 - print out the shape of the array b.
b.shape


# In[79]:


# Exercise 10 - transpose the array b.
print(b.transpose())


# In[80]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(np.concatenate(b))


# In[88]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(np.transpose(np.concatenate(b))


# # Setup 3
# - c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 
# ## HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# ## Exercise 1 - Find the min, max, sum, and product of c.
# 
# ## Exercise 2 - Determine the standard deviation of c.
# 
# ## Exercise 3 - Determine the variance of c.
# 
# ## Exercise 4 - Print out the shape of the array c
# 
# ## Exercise 5 - Transpose c and print out transposed result.
# 
# ## Exercise 6 - Get the dot product of the array c with c. 
# 
# ## Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
# 
# ## Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
# 

# In[89]:


# Set up
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[91]:


# 1.
c=np.array(c)
print(c.min())
print(c.max())
print(c.sum())
print(np.prod(c))


# In[92]:


#2
print(c.std())


# In[93]:


#3
print(np.var(c))


# In[94]:


#4
print(c.shape)


# In[95]:


#5
print(c.transpose())


# In[96]:


#6
print(np.dot(c,c))


# In[97]:


#7
print((c*c.transpose()).sum())


# In[99]:


#8
print(np.prod(c*c.transpose()))


# # Setup 4
# ## d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]
# 
# ### Exercise 1 - Find the sine of all the numbers in d
# 
# ### Exercise 2 - Find the cosine of all the numbers in d
# 
# ### Exercise 3 - Find the tangent of all the numbers in d
# 
# ### Exercise 4 - Find all the negative numbers in d
# 
# ### Exercise 5 - Find all the positive numbers in d
# 
# ### Exercise 6 - Return an array of only the unique numbers in d.
# 
# ### Exercise 7 - Determine how many unique numbers there are in d.
# 
# ### Exercise 8 - Print out the shape of d.
# 
# ### Exercise 9 - Transpose and then print out the shape of d.
# 
# ### Exercise 10 - Reshape d into an array of 9 x 2

# In[109]:


#set up
d = [
[90, 30, 45, 0, 120, 180],
[45, -90, -30, 270, 90, 0],
[60, 45, -45, 90, -45, 180]
]

d=np.array(d)


# In[101]:


# 1
print(np.sin(d))


# In[102]:


#2
print(np.cos(d))


# In[103]:


#3
print(np.tan(d))


# In[110]:


#4
d[d < 0]


# In[111]:


#5
d[d > 0]


# In[112]:


#6
np.unique(d)


# In[114]:


#7
len(np.unique(d))


# In[115]:


#8
print(d.shape)


# In[116]:


#9
print(d.transpose().shape)


# In[117]:


#10
print(d.reshape(9,2))


# In[ ]:




