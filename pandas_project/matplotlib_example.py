# import matplotlib
# print(matplotlib.__version__)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
print(df)
# df['Calories'].fillna(130, inplace=True)


# draw a plot. By default, the plot() function draws a line from point to point. 
# Line plot
# plt.plot(df['Duration'])
# plt.plot(df['Duration'],  linestyle='dashed')
# plt.plot(df['Duration'],  linestyle='dotted')
# plt.show()

# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:
# df.plot(kind='scatter', x="Duration", y="Calories")

# Add Title
# plt.title('Workout Duration Vs Calorie Count')
# plt.title('Workout Duration Vs Calorie Count', loc='left')
# plt.show()

# Add labels
# df.plot(kind='scatter', x="Duration", y="Calories")
# plt.title('Workout Duration Vs Calorie Count')
# plt.xlabel('Workout Duration')
# plt.ylabel('Calorie Count')
# plt.show()

# Add color and diff Font
# font1 = {'color':'green','size':20, 'family':'serif'}
# plt.scatter(df["Duration"], df["Calories"])
# plt.title('Workout Duration Vs Calorie Count', fontdict=font1)
# plt.xlabel('Workout Duration')
# plt.ylabel('Calorie Count')
# plt.show()

# Add font family, color and font size for xlabel and ylabel
# font1 = {'family':'serif', 'color':'green','size':20}
# font2 = {'family':'arial','color':'darkred','size':15}
# plt.scatter(df["Duration"], df["Calories"])
# plt.title('Workout Duration Vs Calorie Count', fontdict=font1)
# plt.xlabel('Workout Duration', fontdict=font2)
# plt.ylabel('Calorie Count', fontdict=font2)
# #  add grid lines to the plot
# plt.grid()
# plt.show()

# # Bar plot. The bar function takes arguments that describes the layout of the bars.The categories and their values represented by the first and second argument as arrays.
# x = ['Duration', 'Calories']
# y = [df['Duration'][0] , df['Calories'][0]]
# plt.bar(x, y, color = 'hotpink')
# plt.show()

# histogram plot. showing frequency distributions.
# plt.hist(df['Duration'], color='#4CAF50')
# plt.title('Duration frequency distribution')
# plt.show()

# # Pie Chart. The pie chart draws one piece (called a wedge) for each value in the array.
# x = df['Goodworkout']
# # The labels parameter must be an array with one label for each wedge:
# mylabels = [True, False]
# plt.pie(x.value_counts(), labels=mylabels)
# plt.title('Workout stats')

# # To add a list of explanation for each wedge, use legend
# plt.legend()
# plt.show()
