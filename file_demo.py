# Write to a file
# with open("notes.txt", "w") as f:
#     f.write("Hello from Python!\n")
#     f.write("This will be saved in a file.\n")

# # Read the file back
# with open("notes.txt", "r") as f:
#     content = f.read()

# print("File contents:")
# print(content)
FILENAME = "notes.txt"

# Load existing tasks (if file exists)
notes = []

try:
    with open(FILENAME, "r") as f:
        for line in f:
            task = line.strip()
            if task:  # skip empty lines
                notes.append(task)
except FileNotFoundError:
    # First run: no file yet.
    pass

while True:
    task = input("Add a task (or 'q' to quit): ")
    if task.lower() == "q":
        break
    notes.append(task)

print("\nYour tasks:")
for t in notes:
    print("-", t)
