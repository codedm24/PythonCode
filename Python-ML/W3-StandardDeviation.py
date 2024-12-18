#MachineLearning - Standard Deviation
import numpy as np

#[86 87 88 86 87 85 86]
speed = input("Enter number seperated by spaces:")
speedlist = [int(num) for num in speed.split(" ")]
print(f"you entered {speedlist}")

x = np.std(speedlist)
print("Standard deviation: ", x)

#another array
speed = [32, 111, 138, 28, 59, 77, 97]
x = np.std(speed)
print(f"Standard deviation for {speed} is {x}")
x = np.var(speed)
print(f"Variance for {speed} is {x}")