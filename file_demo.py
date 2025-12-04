# Write to a file
with open("notes.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("This will be saved in a file.\n")

# Read the file back
with open("notes.txt", "r") as f:
    content = f.read()

print("File contents:")
print(content)
