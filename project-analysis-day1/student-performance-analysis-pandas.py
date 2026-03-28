import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')
# This Just to see the Dataset 
print(df.head())
# Data Analysis Starts Here !

print(df.tail())

print(df.info())
# Total 10 Rows ,7 Columns 
# no non 0 Values so No Data Fixing 
# Name is String Rest all is Integer

print(df.describe())
# Checking Wrong Values so no Wrong Value in Numbers by Observing Min and Max 
# As the Data set is Small so No Need For Conditional Checks or Iterations 
# Now to Understand the Corelation between Each Columns I need to Drop the String Name Column
new_df = df.drop(df[['name']],axis='columns')
print(new_df)
print(new_df.corr())
# From these I can Clearly Conclude that Student The Attendance as Study Hour Highly Linear 
#  study_hours and attendance ---> 0.897643
# Math Science English are Also Highly Linearly Related 
# math    and study_hours  --->  0.922861
# science and study_hours  --->  0.894929
# English and study_hours  --->  0.897643
# All the marks of subjects are also in linear relation based on the student performance
# This means the student who studied well perfromed well in all the exams 
# Which Indicates that the student with higher attendance and study_hours have higher probablity of scoring good 

# let as add a percentage column in the new_df
total_marks_list = []
percentage_list = []
for id in range(0,10):
    total_marks = new_df[['math','science','english']].loc[id].sum()
    percentage = int(total_marks/3)
    print(id,total_marks,percentage)
    total_marks_list.append(total_marks)
    percentage_list.append(percentage)

print(new_df.info())
print(len(total_marks_list))
new_df['total_marks'] = total_marks_list
new_df['percentage %'] = percentage_list
print(new_df)

# After 1 hour continous search on document I ended up with this solution to 
# get the total_marks and percentage but this was without cheating
# and no Ai is used purely My brain and Understanding and Implementing the doc
# Trail and Error approach 

# Now Lets know What is the greatest percentage 
maximum_percentage = new_df['percentage %'].max()
print(maximum_percentage)

# To know the name of the Topper 
new_df['name'] = df[['name']]

# Who is the topper ?
topper_row = new_df[new_df['percentage %']== maximum_percentage]
print(topper_row)
topper_name = topper_row['name']
print(topper_name)


# Lowest Scorer ?
minimum_percentage = new_df['percentage %'].min()
print(minimum_percentage)

# Who is the minimum scorer?
minimum_scorer_row = new_df[new_df['percentage %'] == minimum_percentage]
print(minimum_scorer_row)
minimum_scorer_name = minimum_scorer_row['name']
print(minimum_scorer_name)

# What is the Average Percentage ?
average_percentage = new_df['percentage %'].mean()
print(average_percentage)

# What Subject is Toughest ?
science_total = new_df['science'].sum()
print(science_total)
math_total = new_df['math'].sum()
print(math_total)
english_total = new_df['english'].sum()
print(english_total)
toughest_subject = max(science_total,math_total,english_total)
print(toughest_subject)
# By Printing the Total I observe that 766 is the highest for Science and English Both since Same
# Math is the Toughest Subject

# What Subject is Easiest ?
science_total = new_df['science'].sum()
print(science_total)
math_total = new_df['math'].sum()
print(math_total)
english_total = new_df['english'].sum()
print(english_total)
easiest_subject = min(science_total,math_total,english_total)
print(easiest_subject)
# Hence Science and English Both are same Both are Easy



# Higher Performers 
high_performers_df = new_df[new_df['percentage %'] > 80]
high_performers_name = high_performers_df['name']

# To print Top 5 Performers Only
print(high_performers_name[:4])


# Low Performers 
low_performers_df = new_df[new_df['percentage %'] < 60]
low_performers_name = low_performers_df['name']

# To Low Performers 
print(low_performers_name)


# Low Attendance Students
low_attendance_students_df = new_df[new_df['attendance'] < 80]
low_attendance_students_name = low_attendance_students_df['name']

# Low Attendance Students
print(low_attendance_students_name)

# Group by analysis 
result1 = new_df.groupby('study_hours')[['percentage %']].mean()
print(result1)

result2 = new_df.groupby('attedance')[['percentage %']].mean()
print(result2)


# Bar Chat 
x = high_performers_df['name']
y = high_performers_df['percentage %']

plt.bar(x,y)
plt.show()

# Line Graph
x = new_df['study_hours']
y = new_df['percentage %']

plt.plot(x,y)
plt.show()


# Conclusion 
#  Math is the Toughest Subject 
#  Attendance + Study Hours = Good Result 

