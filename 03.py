import pandas as pd
df2=pd.DataFrame([('ravi',10),('saket',40),('Rakshit',50)],columns=['name','marks'])
# If we use curly bracket then data will give in reverse order
df2.index=['a','b','c']
# df2[['name','marks']]
# df2[["marks"]]
df2.loc['a']
# print(df2.loc['a':'b','name'])
# print('a','name')
# print(df2.loc['a','name':'marks'])
# print(df2.loc[df2['marks']<40,['name','marks']])
# for i in df2.iterrows():
#     print(i)
#     print(i,type(i))
#     break
    # print(i[0],type(i[1]))
for index,data in df2.iterrows():
    # print(index,type(index))
    print(index, data)



# print(df2,type(df2))
# print(df2)