"""Demonstrations of dictionary capabilities"""

# Declaring type of dictionary
schools: dict[str, int]
# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150
# print a dictionary literal representation
print(schools)

# Acess a value by it's key
print(f"UNC has {schools['UNC']} students.")

# Remove a key value pair by it's key value
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
print(schools)

# Update / Reassign a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200
print(schools)

# Demonstration of dictionary literals
# empty dictionary
schools = {} # same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400,
    "Duke": 6717,
    "NCSU": 26150
}
print(schools)

# What happens when a key doesnt exist?
# print(schools["UNCC"])
# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")