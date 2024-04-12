import pandas as pd
data=["Rakshit","Kamal","Vivek","Shailesh"]
data1=pd.Series(data,[40,22,62,47])
print(data1)
# Syntax for dataframe Visualisation;
# pandas.DataFrame(data,index,columns,dtype,copy) 
# Example:
data =[['Alex',10],['Bob',12],['Clarke',13]]
df =pd.DataFrame(data,columns=['Name','Age'])
print(df)
# Example2:
data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)
