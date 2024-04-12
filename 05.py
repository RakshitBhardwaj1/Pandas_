import pandas as pd
df=pd.DataFrame({'ID':[1,2,3,4],'Name':['Alice','Bob','Charlie','Dana'],'Math_Score':[85,75,90,80],'Science_Score':[90,85,80,95]})
# print(df)

# Ans:1
mean_math_score=df.Math_Score.mean()
# print(mean_math_score)

# Ans:2
highest_science_score=df.Science_Score.max()
# print(highest_science_score)

# Ans:c
df['total_score']=df['Math_Score']+df['Science_Score']
# print(df)

# Ans:d
highest_total_score=df.loc[df['total_score']==df['total_score'].value_counts().idxmax()]
print(highest_total_score['Name'])

# Ans:e
diff_math_science_score=df.Math_Score.mean()-df.Science_Score.mean()
print(diff_math_science_score)

# 
