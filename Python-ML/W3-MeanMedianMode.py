#Mean, Median, Mode
import numpy as np
from scipy import stats
speed= [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)

print(f"Mean value for speed {x:.2f}")

speed.sort()
print("sorted list", speed)
x = np.median(speed)

print(f"Median value for speed {x:.2f}")

#if two middle values
speed1= [99,86,87,111,86,103,87,94,78,77,85,86]
speed1.sort()
x = np.median(speed1)
print(f"Median value for speed1 {x:.2f}")

x = stats.mode(speed)
print(f"Mode value for speed {x}")
