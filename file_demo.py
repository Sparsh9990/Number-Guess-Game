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

# Load existing notes (if file exists)
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

def show_notes(notes_list):
    if not notes_list:
        print("\nNo notes yet.")
        return
    print("\nYour notes:")
    for i, t in enumerate(notes_list, start=1):
        print(f"{i}. {t}")

while True:
    print("\nChoose an option:")
    print("A - Add a note")
    print("L - List notes")
    print("D - Delete a note")
    print("Q - Quit")
    choice = input("Your choice: ").strip().lower()

    if choice == "a":
        task = input("Enter a note: ").strip()
        if task:
            notes.append(task)
            print("Note added.")
    elif choice == "l":
        show_notes(notes)
    elif choice == "d":
        show_notes(notes)
        if notes:
            num = input("Enter note number to delete: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(notes):
                    removed = notes.pop(idx)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid note number.")
            else:
                print("Please enter a number.")
    elif choice == "q":
        break
    else:
        print("Unknown option, try again.")

# Save notes back to file
with open(FILENAME, "w") as f:
    for t in notes:
        f.write(t + "\n")

print("\nNotes saved to", FILENAME)


