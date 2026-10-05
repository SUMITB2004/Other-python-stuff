import numpy as np

np.random.seed(7)

subjects = ["physics", "math", "chemistry", "coding", "sex"]
marks = np.random.randint(40,101, size = (50,5))

print("sample marks (first 5 students):")
print(marks[:5])

print("\n datasheet info")
print(f"shape: {marks.shape}")
print(f"dimensions: {marks.ndim}")
print(f"num students: {marks.shape[0]}")
print(f"num subjects: {marks.shape[1]}")

total = np.sum(marks, axis=1)
print("\n student totals (first 5)")
for i in range(5):
    print(f"students {i+1:2d} total = {total[i]}")

subject_avg = np.mean(marks, axis = 0)                      #np.mean calculates the avg
for name, avg in zip (subjects, subject_avg):               #zip() pairs two lists.
    print(f" {name:<10} avg = {avg:.1f}")                   #?

    

