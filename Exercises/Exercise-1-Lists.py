import numpy as np
import statistics
from scipy import stats

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(type(flowers))
print(flowers)

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", 
                "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
print("count: ", len(flowers_list))

print("first entry: ", flowers_list[0])
print("second entry: ", flowers_list[1])

print("Last entry: ", flowers_list[9])

print("first rwo entries: ", flowers_list[:2])
print("last two entries", flowers_list[-2:])
print("from second to fifth entries: ", flowers_list[1:5])

flowers_list.remove("globe thistle")
print(flowers_list)

flowers_list.append("snapdragon")
print(flowers_list)

hardcover_sales = [139,128,172,139,191,168,170]

128, 139, 139, 168, 170,172,191

print("length of the list: ", len(hardcover_sales))

print("Entry at index 2: ", hardcover_sales[2])

print("Minimum: ", min(hardcover_sales))
print("Minimum: ", max(hardcover_sales))
print("Average: ", statistics.mean(hardcover_sales))
print("Median: ", statistics.median(hardcover_sales))
print("Mode: ",  statistics.mode(hardcover_sales))

print("Average: ", np.mean(hardcover_sales))
print("Median: ", np.median(hardcover_sales))
print("Mode: ",  stats.mode(hardcover_sales))

# Sample data 
data = [1, 2, 2, 3, 4, 4, 4, 5, 6] 
# Calculate mean 
mean = sum(data) / len(data) 
print(f"Mean: {mean}") 
# Calculate median 
sorted_data = sorted(data) 
n = len(sorted_data) 
if n % 2 == 0: 
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 
else: 
    median = sorted_data[n//2] 
print(f"Median: {median}") 

# Calculate mode 
print("set(data)", set(data))
mode = max(set(data), key=data.count) 
print(f"Mode: {mode}")

ratings = [1, 2, 3, 4, 5, 4, 5, 1]
liked_ratings = [x for x in ratings if x >= 4]
print(liked_ratings)