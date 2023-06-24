import os
import datetime

CURR_FILE = "june.txt"

# Function to display the main menu
def display_menu():
    print("------ Journal Program ------")
    print("1. Write a new entry")
    print("2. View past entries")
    print("3. Add short term goal")
    print("4. Add long term goal")
    print("5. View short and long term goals")
    print("6. Exit")

# Function to get user input for a new journal entry
def write_entry():
    title = input("Enter a title for your entry: ")
    content = input("Enter the content for your entry: ")
    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CURR_FILE, "a") as file:
        # Write the title, content, and date to the file
        file.write(f"\nTitle: {title}\nContent: {content}\nDate: {current_datetime}")

# Function to view past journal entries
def view_entries():
    if not os.path.isfile("journal.txt"):
        print("No entries found.")
        return
    with open("journal.txt", "r") as file:
        entries = file.read().split("\n\n")
    for i, entry in enumerate(entries):
        if not entry:
            continue
        # Split the entry into title, content, and date
        title, content, date = entry.split("\n")
        print(f"--- Entry {i+1} ---")
        print(f"Title: {title[7:]}")
        print(f"Content: {content[9:]}")
        print(f"Date: {date[6:]}")

# Function to add a short term goal
def add_short_term_goal():
    goal = input("Enter a short term goal: ")
    with open("short_term_goals.txt", "a") as file:
        file.write(f"\n{goal}")

# Function to add a long term goal
def add_long_term_goal():
    goal = input("Enter a long term goal: ")
    with open("long_term_goals.txt", "a") as file:
        file.write(f"\n{goal}")

# Function to display short and long term goals
def view_goals():
    print("------ Short and Long Term Goals ------")
    if not os.path.isfile("short_term_goals.txt"):
        print("No short term goals found.")
    else:
        with open("short_term_goals.txt", "r") as file:
            short_term_goals = file.read().split("\n")
        print("Short Term Goals:")
        for i, goal in enumerate(short_term_goals):
            if not goal:
                continue
            print(f"{i+1}. {goal}")
    if not os.path.isfile("long_term_goals.txt"):
        print("No long term goals found.")
    else:
        with open("long_term_goals.txt", "r") as file:
            long_term_goals = file.read().split("\n")
        print("Long Term Goals:")
        for i, goal in enumerate(long_term_goals):
            if not goal:
                continue
            print(f"{i+1}. {goal}")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        add_short_term_goal()
    elif choice == "4":
        add_long_term_goal()
    elif choice == "5":
        view_goals()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
    