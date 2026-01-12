import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Aarav", "Diya", "Rohan", "Isha", "Kabir", "Anaya", "Neel", "Pooja"],
    "Age": [18, 19, 18, 20, 21, 19, 18, 22],
    "Hours_Studied": [4.5, 6.0, 3.0, 7.5, 2.0, 5.5, 6.5, 1.0],
    "Attendance": [85, 92, 78, 95, 60, 88, 90, 55],
    "Score": [72, 85, 65, 90, 50, 80, 88, 45]
}
df = pd.DataFrame(data)
df_new = pd.DataFrame()
print(df.head())
print(df.shape)
print(df.columns)
print(df['Age'].dtype)
print('Median score is', np.median(df['Score']))
print('Mean score is ', np.mean(df['Score']))
print('Max Hours studied is ', np.max(df['Hours_Studied']))
print('Min Hours studied is ', np.min(df['Hours_Studied']))
df['Result'] = np.where(df['Score'] >= 60, 'Pass', 'Fail'  )
print('The total duplicates are ', np.sum(df.duplicated()))
df = df.drop_duplicates() # There arent any but still i did it 😆
df_new = df[(df['Attendance'] < 75)]
df = df.sort_values(by = 'Score', ascending = False) 
df.rename(columns={'Hours_Studied': 'Study_Hours'}, inplace=True)
print(df['Score'].dtype)
avg_score = np.mean(df['Score'])
df['Score_Above_Avg'] = np.where(df['Score'] > avg_score, True, False)
score = df['Score'].to_numpy()
print('Mean is ', np.mean(score))
print('Standard Deviation is ', np.std(score))
z = (df['Score']-np.mean(score))/np.std(score)
print('Noramlization i.e Z score is \n', z)
print('Total students with above avg score are', np.sum(df['Score_Above_Avg']))
df['Efficiency'] = df['Score']/df['Study_Hours']
df['Eff_above_avg'] = np.where(df['Efficiency'] > np.mean(df['Efficiency']), True, False)
df.sort_values(by='Efficiency', ascending=False, inplace=True)
print('Top efficient students are \n', df.head(3))
plt.hist(df['Efficiency'])
plt.show()
colors = np.where(df['Eff_above_avg'] == True, 'Green', 'Red')
plt.scatter(df['Score'], df['Study_Hours'], color = colors )
plt.show()