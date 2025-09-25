import pickle
import math

# Load the pickle file
with open("similarity_part4.pkl", "rb") as f:
    data = pickle.load(f)

# Split into 2 parts
half = math.ceil(len(data) / 2)

part1 = data[:half]
part2 = data[half:]

# Save as two smaller pickle files
with open("similarity_part4a.pk4", "wb") as f:
    pickle.dump(part1, f)

with open("similarity_part4b.pk4", "wb") as f:
    pickle.dump(part2, f)

print("✅ Split similarity_part1.pkl into similarity_part1a.pkl and similarity_part1b.pkl")
