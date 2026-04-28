from datetime import datetime

def show_menu():
    print("\nFood-Finder-2-For-5-Survival-Guide")
    print("1. Log a new restaurant ")
    print("2. View restaurant  log")
    print("3. Exit")
    print("4. View only high-rated restaurant  (8–10)")
    print("5. Show total number of restaurant  logged")
    print("6. Clear all restaurant logs")

def log_restaurant():
    name = input("Restaurant name: ")
    food_type = input("Type of food (e.g., Italian, Mexican, Sushi): ")
    location = input("Where is it located?: ")
    rating = input("Rate it (1–10): ")
    
    while not rating.isdigit() or not (1 <= int(rating) <= 10):
        print("Please enter a valid number from 1 to 10.")
        rating = input("Rate it (1–10): ")
    
    notes = input("Optional notes: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("restaurant_log.txt", "a") as file:
        file.write(f"{timestamp} | {name} | {food_type} | {location} | {rating} | {notes}\n")
    
    print("Restaurant logged!")

def view_log():
    try:
        with open("coffee_log.txt", "r") as file:
            print("\nTimestamp | Name | Type | Location | Rating | Notes")
            print("-" * 80)
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No coffee log found.")

def filter_high_rated():
    try:
        with open("coffee_log.txt", "r") as file:
            print("\nHigh-Rated Coffees (8–10):")
            print("-" * 80)
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 6 and parts[4].isdigit() and int(parts[4]) >= 8:
                    print(line.strip())
    except FileNotFoundError:
        print("No coffee log found.")

def show_count():
    try:
        with open("coffee_log.txt", "r") as file:
            lines = file.readlines()
            print(f"\nTotal coffees logged: {len(lines)}")
    except FileNotFoundError:
        print("No coffee log found.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1–6): ")
        if choice == "1":
            log_coffee()
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            filter_high_rated()
        elif choice == "5":
            show_count()
        elif choice == "6":
            confirm = input("Are you sure you want to delete all logs? (y/n): ")
            if confirm.lower() == "y":
                with open("coffee_log.txt", "w") as file:
                    file.write("")
                print("Coffee log cleared.")
            else:
                print("Cancelled. Coffee log not cleared.")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

