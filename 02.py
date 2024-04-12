import pandas as pd
# series=pd.Series([10,12,11,12.5,15],index=list('abcde'))
# print(series)
df=pd.DataFrame([('ravi',10),('Rakshit',40),('Kamal',22)],columns=['name','rollno'],index= (None))
# print(df)
movies=pd.read_csv(r'c:\Users\Admin\Pictures\Top 1000 Bollywood Movies and their boxoffice.csv')
# print(movies.head(2))
# Indexing
data=movies[['Movie','Verdict']]
print(data)
movies.loc[1,'Movie']
movies.loc[1:3,'Movie']
print(movies.loc[1,'Verdict'])
movies.loc[movies['Year']>2016,:]
# movies.loc[:,'Film','Year'] In this : select all the rows and only 2 column included
# In this when we use slice the it include the last element like[1:3] so it include 3 also
