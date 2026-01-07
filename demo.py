import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("hello world")
# Visualize relationships between key variables and heart disease
plt.figure(figsize=(10, 6))
sns.boxplot(x='HeartDiseaseorAttack', y='BMI', data=data)
plt.title('BMI vs Heart Disease or Attack')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='HeartDiseaseorAttack', y='PhysicalHealth', data=data)
plt.title('Physical Health vs Heart Disease or Attack')
plt.show()