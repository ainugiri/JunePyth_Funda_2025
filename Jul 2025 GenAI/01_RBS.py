# Early and Simple AI System using if-then statements.

# Function to determine action based on traffic signal color
def traffic_signal_action(signal):
    if signal == "Green":
        return "You can move the vehicle."
    elif signal == "Red":
        return "You must stop the vehicle."
    elif signal == "Yellow":
        return "You must slow down the vehicle."
    else:
        return "Invalid signal."

# Get user input for traffic signal and print the corresponding action
signal = input("Enter the traffic signal (Green, Red, Yellow): ")
action = traffic_signal_action(signal)
print(action)

# Function to determine grade based on score
def grade_action(grade):
    if grade == 100:
        return "You got an A+."
    elif grade >= 90:
        return "You got an A."
    elif grade >= 80:
        return "You got a B."
    elif grade >= 70:
        return "You got a C."
    elif grade >= 60:
        return "You got a D."
    else:
        return "You failed."

# Get user input for grade and print the corresponding grade action
grade = int(input("Enter your grade (0-100): "))
action = grade_action(grade)
print(action)

# Function to predict car price based on its age
def car_price_prediction(age):
    if age == 1:
        return "The car price is 104,000."
    elif age == 2:
        return "The car price is 95,000."
    elif age == 3:
        return "The car price is 90,000."
    elif age == 4:
        return "The car price is 80,000."
    elif age == 5:
        return "The car price is 75,000."
    else:
        return "Invalid age."
    
# Get user input for car age and print the predicted price
age = int(input("Enter the age of the car (1-5 years): "))
price = car_price_prediction(age)
print(price)    

# Simple chat bot function to answer product-related queries
def chat_bot():
    print("Welcome to the Chat Bot!")
    print("You can ask about the products.")
    
    while True:
        user_input = input("You: ")
        # Exit the chat bot if user types 'exit' or 'quit'
        if user_input.lower() in ["exit", "quit"]:
            print("Chat Bot: Goodbye!")
            break
        # Respond to queries about iPhone
        elif "iphone" in user_input.lower():
            print("Chat Bot: The iPhone is a smartphone made by Apple.")
            print("Enter the options 1. Purchase 2. Repair 3. Support")
            # Get user option for iPhone
            option = input("Choose an option (1, 2, or 3): ")
            if option == "1":
                print("Chat Bot: You chose to purchase the iPhone.")
            elif option == "2":
                print("Chat Bot: You chose to repair the iPhone.")
            elif option == "3":
                print("Chat Bot: You chose support for the iPhone.")
            else:
                print("Chat Bot: Invalid option.")
        # Respond to queries about Samsung
        elif "samsung" in user_input.lower():
            print("Chat Bot: The Samsung Galaxy is a popular Android smartphone.")
        # Respond to queries about Google
        elif "google" in user_input.lower():
            print("Chat Bot: The Google Pixel is known for its excellent camera.")
        # Default response for unknown products
        else:
            print("Chat Bot: I'm not sure about that product.")

# Start the chat bot
chat_bot()
