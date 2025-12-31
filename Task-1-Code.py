import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='--', color='green')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
plt.bar(categories, values, color='blue')
plt.title("Bar Chart Example")
plt.show()
data = [12, 17, 15, 12, 18, 20, 22, 15, 17]
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.show()
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red','green','blue','yellow'])
plt.title("Pie Chart Example")
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
# Load sample dataset
data = sns.load_dataset("tips")
sns.lineplot(x='size', y='total_bill', data=data, marker='o')
plt.title("Seaborn Line Plot")
plt.show()

sns.scatterplot(x='total_bill', y='tip', hue='sex', style='time', data=data, s=100)
plt.title("Seaborn Scatter Plot")
plt.show()

sns.barplot(x='day', y='total_bill', data=data, palette='pastel')
plt.title("Seaborn Bar Plot")
plt.show()
sns.histplot(data['total_bill'], bins=10, kde=True, color='orange')
plt.title("Seaborn Histogram")
plt.show()
sns.boxplot(x='day', y='total_bill', data=data, palette='Set2')
plt.title("Seaborn Box Plot")
plt.show()
