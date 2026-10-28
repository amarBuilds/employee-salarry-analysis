import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employee.csv')

print("Employee Names, Departments, and Salaries:")
print(df[['Name', 'Department', 'Salary']])

avg_salary_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary for Each Department:")
print(avg_salary_dept)

avg_salary_dept.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()