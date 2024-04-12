import pandas as pd
df=pd.DataFrame([(10,'Alice',25,'Female','New York'),(2,'Bob',30,'Male','London'),(3,'Charlie',28,'Male','Paris'),(4,'Dana',35,'Female','Berlin')],columns=['ID','Name','Age','Gender','City'])
df2=pd.DataFrame(df)
# Ans:a
unique_city=df2.City.unique()
# print(unique_city)

# Ans:b
Average_age=df2.Age.mean()
# print(Average_age)

# Ans:c
males=df2.loc[df['Gender']=='Male']
# print(males.Gender.count())
Females=df2.loc[df['Gender']=='Female']
# print(Females.Gender.count())

# Ans:d
oldest_person=df2.loc[df['Age']==df2.Age.max()]
# print(oldest_person['Name'])

# Ans:e
highest_number_individual=df2.City.mode()
print(highest_number_individual.max())

