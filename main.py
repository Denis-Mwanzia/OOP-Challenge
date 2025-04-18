from pet import Pet

def main():
    name = input("🐾 Enter your pet's name: ")
    pet = Pet(name)

    print(f"\n🎉 Welcome, {pet.name} is ready to play with you!\n")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train a new trick")
        print("5. Show tricks")
        print("6. Show status")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter the trick to teach your pet: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"\n👋 Goodbye! {pet.name} will miss you!\n")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()