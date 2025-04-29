import numpy as np

# Step 1: Create the dataset
age = np.random.randint(18,81,10000)
income = np.random.randint(20000,120001,10000)
exp = np.random.randint(0,51,10000)
children = np.random.randint(0,6,10000)
gender = np.random.randint(0,2, 10000)

# Stack them into a dataset
data = np.stack([age, income,exp,children,gender],axis=1)
print(data)

# Step 2a: Mean income per gender
mean_income_male = data[data[:,4]== 0][:,1].mean()
mean_income_female = data[data[:,4]== 1][:,1].mean()
print(mean_income_male)


