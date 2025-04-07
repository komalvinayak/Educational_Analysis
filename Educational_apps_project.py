# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importing dataset
file = "Appdata1 (1).xlsx"
df=pd.read_excel(file)

# checking columns
print("Columns in Dataset")
print(df.columns)

# Sets pandas to display all columns in a DataFrame
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)

# data description
print("Data Description")
print(df.describe())

# shape of dataset
print("Shape of dataset")

print(df.shape)

# Type-conversion
df['Review(Phone)']=pd.to_numeric(df['Review(Phone)'])
df['Review(Tablet)']=pd.to_numeric(df['Review(Tablet)'])
df['Review(Watch)']=pd.to_numeric(df['Review(Watch)'])
df['Review(TV)']=pd.to_numeric(df['Review(TV)'])
df['Review(Chromebook)']=pd.to_numeric(df['Review(Chromebook)'])
df['Rating(Phone)']=pd.to_numeric(df['Rating(Phone)'])
df['Rating(TV)']=pd.to_numeric(df['Rating(TV)'])
df['Rating(Chromebook)']=pd.to_numeric(df['Rating(Chromebook)'])
df['Rating(Watch)']=pd.to_numeric(df['Rating(Watch)'])
df['Downloaders']=pd.to_numeric(df['Downloaders'])

# priting dataset
print(df)

# filling nan values
df['Founder'] = df['Founder'].fillna('Unknown')
df[['Rating(Phone)','Rating(Tablet)','Rating(TV)','Rating(Watch)','Rating(Chromebook)','Review(Phone)','Review(Tablet)','Review(Watch)','Review(TV)','Review(Chromebook)','Downloaders']] = df[['Rating(Phone)','Rating(Tablet)','Rating(TV)','Rating(Watch)','Rating(Chromebook)','Review(Phone)','Review(Tablet)','Review(Watch)','Review(TV)','Review(Chromebook)','Downloaders']].fillna(0)
df[['Science','Vocabulary','Mathematics','English','Computer-Science','Competitive Exams','Social-Science','Language ','Commerce','Law','CBSE Syllabus','NCERT','Astronomy','Productivity']] = df[['Science','Vocabulary','Mathematics','English','Computer-Science','Competitive Exams','Social-Science','Language ','Commerce','Law','CBSE Syllabus','NCERT','Astronomy','Productivity']].fillna('N')
df[['Review(Phone)','Review(Tablet)']].replace(',','')
# print(df)

# Feature Engineering
def total_review(df):
    return df['Review(Phone)'] + df['Review(Tablet)'] + df['Review(Watch)'] + df['Review(TV)'] + df['Review(Chromebook)']
def avg_rating(df):
    return np.mean(df['Rating(Phone)'] + df['Rating(Tablet)'] + df['Rating(Watch)'] + df['Rating(TV)'] + df['Rating(Chromebook)'])/5
def total_subject(df):
    return df[['Science','Vocabulary','Mathematics','English','Computer-Science','Competitive Exams','Social-Science','Language ','Commerce','Law','CBSE Syllabus','NCERT','Astronomy','Productivity']].eq('Y').sum()

df['Total Review'] = df.apply(total_review, axis=1)
df['Average Rating']=(df.apply(avg_rating,axis=1))
df['Total Subjects']=df.apply(total_subject,axis=1)
print("Total Review\n",df['Total Review'])
print("Average Rating\n",df['Average Rating'])
print("Total Subjects\n",df['Total Subjects'])

# Queries
# Query 1 apps have high downloaders than 10M
print("Name of Apps which have high downloaders than 10M")
print(df[df['Downloaders']>1000000][['Name','Downloaders']])

# Query 2 Sorting data
df.sort_values(by='Downloaders',ascending=False,inplace=True)
print("Data set\n",df)

# # Query 3  Apps which teaches 1 subjects
print("Name of Apps which teaches 1 subjects")
print(df[df['Total Subjects']<2][['Name','Downloaders']])

# Query 4 Apps which teaches more than 10 subjects
print("Apps which teaches more than 10 subjects")
print(df[df['Total Subjects'] >10][['Name','Downloaders']])

# Query 5 Apps which help students to prepare competitive exams
print("Apps which help students to prepare competitive exams")
print(df[df['Competitive Exams']=='Y' ][['Name','Downloaders']])

# # Query 6 Apps which teach Science subject
print("Apps which teach Science subject")
print(df[df['Science'] =='Y'][['Name','Average Rating']])

# Query 7 Subjects teaches by Apps
print("Subjects teaches by those apps which teaches Science subject")
print(df[df['Science'] =='Y'][['Name','Total Subjects']])

# Query  8 Apps which has average rating more than 4.0
print("Name of Apps which has average rating more than 4.0")
print(df[df['Average Rating'] > 4.0][['Name','Average Rating']])

# Query 9 Apps which has total review more than 10000
print("Apps which has total review more than 10000")
print(df[df['Total Review'] > 10000][['Name']])

# Query 10 app avialble on all devices
print("Name of Apps which are available on all devices")
print(df[ (df['Review(Phone)'] > 0) & (df['Review(TV)'] > 0) & (df['Review(Chromebook)'] > 0) & (df['Review(Watch)'] > 0)] [['Name']])

# Query 11 Apps which teach Computer-Science subject
print("Apps which teach Computer-Science subject")
print(df[df['Computer-Science']=='Y'][['Name','Average Rating']])

# 1 graph
# Show number of subject teaches by first 20 App
plt.figure(figsize=(38, 6))
m=df['Name'].head(20)
n=df['Total Subjects'].head(20)
plt.barh(m,n,color='orange',label='Subject')
plt.legend()
plt.title("Number of subjects teaches by each app")
plt.xlabel('Number of subjects')
plt.ylabel('Name of App')
plt.show()

# 2 graph analysing the rating of app on phone with horizontal graph
phone_ratings = df['Rating(Phone)']
app_names = df['Name']
plt.figure(figsize=(12, 8))
plt.barh(app_names[20:41], phone_ratings[20:41], color='skyblue')
plt.xlabel('Phone Ratings')
plt.title('Phone Ratings of Educational Apps')
plt.tight_layout()
plt.show()

# 3 graph : Visualizing the type of each app.
app_type_counts = df['Type'].value_counts()
# print(app_type_counts)
# Plotting a pie chart for app types
plt.figure(figsize=(8, 6))
labels = ['Free', 'Paid']  # Labels for each portion
explode = (0, 0.5)
colors=['pink','seagreen']
# Creating the pie chart
plt.pie(app_type_counts,explode=explode,colors=colors, labels=labels, autopct='%1.1f%%', startangle=140)
# Adding title
plt.title('Distribution of App Types (Free vs. Paid)')
# Displaying the pie chart
plt.axis('equal')
plt.tight_layout()
plt.show()

# 4 graph Visualizing rating gives by users from different devices.
rating_columns = ['Rating(Phone)', 'Rating(Tablet)', 'Rating(TV)', 'Rating(Watch)', 'Rating(Chromebook)']
# Extracting ratings from the dataset
ratings = df[rating_columns].mean()
# Plotting a pie chart for app ratings across devices
plt.figure(figsize=(8, 8))
explode=[0,0,00.3,0.01,0.02]
colors=['Yellow','seagreen','pink','red','blue']
label=['Phone','Tablet','TV','Watch','Chromebook']
# Creating the pie chart
plt.pie(ratings,explode=explode,colors=colors,labels=label, autopct='%1.1f%%',startangle=140)
# Adding title
plt.title('App Ratings Across Devices')
# Displaying the pie chart
plt.axis('equal')
plt.tight_layout()
plt.show()

# 5 graph
# Plotting a bar plot for average ratings across devices
rating_columns = ['Rating(Phone)', 'Rating(Tablet)', 'Rating(TV)', 'Rating(Watch)', 'Rating(Chromebook)']
ratings = df[rating_columns].mean()
# Plotting a bar plot for average ratings across devices
plt.figure(figsize=(10, 6))
devices = ratings.index #['Rating(Phone)', 'Rating(Tablet)', 'Rating(TV)', 'Rating(Watch)', 'Rating(Chromebook)']
avg_ratings = ratings.values #mean values
plt.bar(devices, avg_ratings, color='yellow')
plt.title('Average Ratings Across Devices')
plt.xlabel('Devices')
plt.ylabel('Average Ratings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# worldcloud of apps
import matplotlib.pyplot as plt
from wordcloud import WordCloud
wordcloud = WordCloud(background_color='white',colormap='tab10',width=800, height=400)
text=df['Name'].str.cat(sep=' ')
wordcloud.max_font_size = 80
wordcloud.max_words = 80
wordcloud.min_font_size=10
wordcloud.generate(text)
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()

# EDA
# import numpy as np
# import pandas as pd
# from ydata_profiling import ProfileReport
# file = "Appdata1 (1).xlsx"
# df=pd.read_excel(file)
# profile = ProfileReport(df)
# profile.to_file(outputfile="eduactional.html")



