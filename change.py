import copy

data = [[20, 30], [40, 50], [60, 70]]

# Create a deep copy
update_data = copy.deepcopy(data)

# Modify inner element
update_data[1][1] = 99

# Print both
print("Original data:", data)
print("Updated data:", update_data)