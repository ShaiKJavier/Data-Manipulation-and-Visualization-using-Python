#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd        #import os is that to operate the local path of the system
import numpy as np       #when we using pandas we need to import numpy as well 
os.getcwd()


# In[13]:


brics = pd.read_csv("C:/Users/lenovo/Downloads/brics.csv")  # We are trying to work on brics.csv dataset
                                                            # Dataset is now stored in a Pandas Dataframe
brics  


# In[15]:


brics.sort_values(by=['code'])                      # Ascending by default.


# In[18]:


brics.sort_values(by=['code'],ascending=True)    #ascending order


# In[19]:


brics.sort_values(by=['code'],ascending=False)  #descending order


# In[20]:


brics.country.sort_values(ascending=False)  # Sorting and printing just one column.//


# In[7]:


brics= pd.read_csv("C:/Users/lenovo/Downloads/brics.csv",index_col = 0)
brics                                                                     #indexing done by denoting column as 0


# In[54]:


brics          #calling the dataframe


# above dataframe one column is added through list ,here we can add any column to the dataframe by using list data type

# In[55]:


brics["on_earth"]=[True,True,True,True,True,False]       
brics                                                        #Adding a new column to the existing Data Frame
    


# In[57]:


brics1.drop(['area','on_earth','code'], axis=1)  #drop the cloumn we dont need


# In[58]:


brics1 = brics


# In[59]:


brics1 = brics

# Another way to drop columns
brics1.drop(columns=['area', 'density']) 


# In[60]:


brics1 = brics

# Drop rows by index

brics1.drop(['IN', 'CH'])


# In[61]:


# The shape function helps us to find the shape or size of an array or matrix. In Excel - A1:D10.  
# shape[0] means we are working along the first dimension of your array.
# If Y has n rows and m columns, then Y.shape is (n,m). So Y.shape[0] is n.

for index in range(brics.shape[0]):    
    countryName = brics.iloc[index,0]  # row - index, column - 0
    cityName = brics.iloc[index, 3]  # row - index, column - 3
    print('The Capital City of', countryName, 'is', cityName)


# In[62]:


for index, row in brics.iterrows():#ANOTHER SOLUTION
    print("The Capital City of",row['country'],"is", row['capital'])


# In[63]:


cars = pd.read_csv("C:/Users/lenovo/Downloads/cars.csv")
cars    


# In[66]:


# Print top 5 rows from the data, without any sorting or filter.
cars.head()


# In[68]:


cars.tail()# For bottom 5 rows in the dataframe


# In[75]:


print(cars)
df1=cars.rename(columns={'Unnamed:0':'code'},inplace = False)
cars.rename(columns={'Unnamed:0':'code'},inplace = True)
print(df1)
print(cars)                        
                        


# In[76]:


print(cars['cars_per_cap'])  # without column name at the top. Prints data and detail


# In[77]:


print(cars[['cars_per_cap']])  # print the actual data


# In[79]:


cars


# In[88]:


cars = pd.read_csv("C:/Users/lenovo/Downloads/cars.csv",index_col=0)
cars 


# In[5]:


marks= pd.read_csv("C:/Users/lenovo/Downloads/marks.csv")
marks 


# In[8]:


print(type(marks))
print(type(marks.English))  # Column's dtype is Series, the dtype of the values is Object.
print(type(5))
print(type(5.5))
print(type("Python"))
print(type(True))


# In[9]:


# Run these lines one by one and observe the difference in the three outputs.
print(marks)
 


# In[10]:


display(marks) #it is used display in dataframe mostly used


# In[11]:


# selecting marks for 'Ria'
display(marks.loc[(marks.Student_Name == 'Ria')])  # in case the index is not known for large datasets


# In[13]:


display(marks.loc[(marks.Student_Name == 'Lia')]) # "==" comparsion operator is used


# In[14]:


# Using OR operator to print details if the name is either 'Ria' OR 'David'
display(marks.loc[(marks.Student_Name == 'Ria') | (marks.Student_Name == 'David')])   


# In[22]:


display(marks.loc[(marks.Student_Name =='Tan') | (marks.Student_Name =='Ria')]) #display by using or


# In[25]:


print(marks.loc[(marks.Student_ID =='S05') | (marks.Student_ID =='S10')]) #print by using or  


# In[28]:


display(marks.loc[(marks.English > 70) & (marks.English>70)])  #fetching marks in English >70 by & opertor


# In[29]:


display(marks.loc[(marks.English > 70) | (marks.English>70)])  #fetching marks in English >70 by | opertor


# In[30]:


# Using NOT function 

# TO DO: Fetch all details for all students except for Ria or the all students who are not Ria.
display(marks.loc[(marks.Student_Name != "Ria")])


# In[3]:


# Index column can be changed by giving the name of the column - unique and case-sensitive

marks = pd.read_csv("C:/Users/lenovo/Downloads/marks.csv", index_col='Student_ID')# could have given the index no. of the columns (0,1..) as well.
display(marks)


# In[46]:


display(marks.iloc[0:10]) # IMPORTANT - Out of 11 indices, the last one will be excluded.

# Returns output of the indices without matching the value of incides entered and the value in the column.
# iloc will not work if the indices are not integers.


# In[55]:


display(marks.iloc[[0,4]])# Data of multiple and non-consecuitive indices
# Selecting details of the 1st and 5th row


# In[56]:


#Print the details from 0th, 5th and 8th rows, along with the details of indices 4th, 11th and 16th.


# In[68]:


display(marks.iloc[[0,4,7]])


# In[70]:


marks.iloc[4:11:16] 


# In[74]:


display(marks.loc['S01':'S05'])


# In[4]:


# Run these line one by one and observe the output to notice the difference and execution of the syntax

# display(marks.iloc[[2:5]])
# display(marks.iloc[[0:5]])
# display(marks.iloc[[:5]])
# display(marks.iloc[[15:20]])
# display(marks.iloc[[15:]])
# display(marks.iloc[[15:100]])
# display(marks.iloc[[:]])







display(marks.iloc[0:2])  # Prints all values from all columns for indices 1,2


# In[6]:


display(marks.iloc[2:5])  # Prints all values from all columns for indices  3 ,4,5.


# In[9]:


display(marks.iloc[:5])  # Prints all values from all columns for indices range of 1 to 5.


# In[10]:


display(marks.iloc[15:100])  # Prints all values from all columns for indices 16,17,18,19 and 20.


# #Data cleaning : Empty value treatment iin dataframes

# In[13]:


temps = pd.DataFrame({"sequence":[1,2,3,4,5],
          "measurement_type":['actual','actual','actual',None,'estimated'],  # With strings, it will become 'None'
          "temperature_f":[67.24,84.56,91.61,None,49.64]   #With numbers, it will become 'NaN'
         })
temps


# NaN belongs to the class float
# 
# None belongs to the class NoneType

# In[14]:


# To identify the null value. Return true if the value is null otherwise false
temps.isna()  


# observe that none(null) become ture rest of all become false

# In[15]:


# Return the count of missing value from each column     
temps.isna().sum() 


# In[16]:


# Total count of null from all columns
temps.isna().sum().sum() 


# In[17]:


# Drop/delete the row containing missing values

clean_temps = temps.dropna(how='any')  # how: {'any', 'all'}. Default 'any'
display (clean_temps)

# ‘any’ : If any NA values are present, drop that row or column.
# ‘all’ : If all values are NA, drop that row or column.


# Observe, in the output, index 3 is not there.


# In[18]:


# Drop the ROWS where at least one element is missing.
temps.dropna()


# In[19]:


# Drop COLUMNS where there are missing values.

# Drop the columns where at least one element is missing.
temps.dropna(axis = 'columns') # Without the 'axis' argument, rows will be dropped by default as you did in the previous code


# In[ ]:


Handling missing data by replacing values
Not every time we should delete the missing values, especially when the dataset is smaller or when missing values are very significant. 
In such as case, additional data-preparation is performed.

Depending on the dataset, it's structure and the research questions, we should decide which data preparation technique should be applied on what column or missing values.


# In[20]:


temps['temperature_f'].cumsum()   # Returns the commulative sum. 

# It will skip null values. skipna = TRUE by default

# CAN YOU THINK OF ANY PRACTICAL USE OF cumsum() ?


# In[23]:


temps['temperature_f'].cumsum(skipna=False)  


# In[24]:


# fill missing value with zero
temps.fillna(value=0, inplace = True)   # Do you remember the use of inplace? If not, please scroll up and check.
display(temps)


# In[25]:


# Print the dataframe

temps

# Why 0 in last column is 0.00 while only 0 in measurement_type? Please explain as a comment in this cell.


# In[26]:


# fill missing value with previous value
temps = pd.DataFrame({"sequence":[1,2,3,4,5],
          "measurement_type":['actual','actual','actual',None,'estimated'],
          "temperature_f":[67.24,84.56,91.61,None,49.64]
         })
temps.fillna(method='pad' , inplace=True)  # 'pad' means padding. Take value from previous row
temps


# In[27]:


# fill missing value with next value
temps1 = pd.DataFrame({"sequence":[1,2,3,4,5],
          "measurement_type":['actual','actual','actual',None,'estimated'],
          "temperature_f":[67.24,84.56,91.61,None,49.64]
         })
temps1.fillna(method='bfill' , inplace=True)  # bfill takes next value to replace
temps1


# In[28]:


# fill missing value with mean
temps = pd.DataFrame({"sequence":[1,2,3,4,5],
          "measurement_type":['actual','actual','actual',None,'estimated'],
          "temperature_f":[67.24,84.56,91.61,None,49.64]
         })
temps['temperature_f'].fillna(temps['temperature_f'].mean(), inplace=True)  # Mean will not work on strings
temps


# Lambda Function

# In[29]:


# lambda is used to define a temporary expression without any return statement. It always contains an expression
# that is returned. There is no need to assign a variable with lambda.


def cube(y):
    return y*y*y  # return is a keyword. Python stops when the code reaches to return statement. Print is a function.
    

# using the normally defined function
    print(cube(5))
 
# using the lambda function                 # Why this is red? How to resolve it?
lambda_cube = lambda y: y*y*y
print(lambda_cube(5))


# In[30]:


# Creating new dataframe to explore the use of Lambda and changing indices.

teams = pd.DataFrame({"Region":['North','West','East','South'],
          "Team":['One','Two','One','Two'],
          "Squad":['A','B','C','D'],
          "Revenue":[7500,5500,2750,6400],
            "Cost":[5200,5100,4400,5300]})

display (teams)


# In[31]:


# apply() to alter values along an axis in your dataframe or in a series/column 

# Categorise based on the revenue and cost
teams['Profit'] = teams.apply(lambda x: 'Profit' if x['Revenue']>x['Cost'] else 'Loss',axis=1)
teams


# In[34]:


# Use map() to substitute each value in a series
team_map = {"One":"Red","Two":"Blue"}      # new variable - dictionary (key-value pair)
teams['Team Color'] = teams['Team'].map(team_map) # A new column with mapped values
teams


# In[33]:


# applymap() method do elementwise operation on the entire dataframe.
# This method applies a function that accepts and returns a scalar to every element of a DataFrame.

teams.applymap(lambda x: len(str(x)))  # int(x) won't work because data has strings which can not be convereted to int.


# In[35]:


# Grouping on different categories. Needs the category as well as parameter
teams.groupby(['Profit']).max()


# In[37]:


# TO DO: Can you group the records on Cost with minimum values?
teams.groupby(['Cost']).min()


# In[38]:


# TO DO: Can you group the records on Revenue column with mean values?
teams.groupby(['Revenue']).mean()


# In[39]:


# Grouping on the basis of aggregates
teams.groupby(['Team']).agg({'Revenue':['mean','min','max']})


# In[40]:


teams


# In[41]:


# Setting two columns as index when a single column has not unique values.

teams_reindex = teams.set_index(['Region','Team'])  # 2 indices. useful when values are not unique
display(teams)

print()    # TO print blank/new line.


display(teams_reindex)


# In[42]:


# Restructuring the dataframe based the multiple indices
stacked = pd.DataFrame(teams_reindex.stack())
stacked


# Mergining dataframes

# In[43]:


# Defining two new dataframes
group1 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'number': [1, 2, 3, 4]})
group2 = pd.DataFrame({'name': ['Charlie', 'David', 'Edward', 'Ford'],
                    'number': [3, 4, 5, 6]})


# In[44]:


group1.merge(group2,how='left', on='number')   # Left - all from 1st table and only common from 2nd table.


# In[45]:


group1.merge(group2)   # Shows only the common records.


# In[46]:


group1.merge(group2,how='inner',left_on='number',right_on='number')  # Inner - Shows only the common records


# In[47]:


group1.merge(group2,how='right',left_on='number',right_on='number')  # Right - All from 2nd table, common from 1st table.


# In[1]:


import pandas as pd


# In[4]:


mt_cars = pd.read_csv("C:/Users/lenovo/Downloads/mtcars.csv")  #created the dataframe by dataset 
mt_cars


# In[7]:


type(mt_cars) #we can see which type it is 


# In[5]:


mt_cars = pd.read_csv("file:///C:/Users/lenovo/Downloads/mtcars.csv",index_col = "car_names")


# by using index_column I changed the index column 

# In[6]:


mt_cars


# In[8]:


# Import he required package 
import matplotlib.pyplot as plt


# In[38]:


plt.plot(mt_cars)
plt.xlabel("mpg")
plt.ylabel("hp")
plt.title("mpg vs hp")


# In[17]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ct = pd.crosstab(mt_cars.cyl, mt_cars.cyl)

ct.plot.bar(stacked=True)    # Try staked=False and then by removing stakced part
plt.legend(title='mark')   # Optional

plt.show()


# In[30]:


mt_cars.plot.hist(by="mpg", bins=10)


# In[ ]:




