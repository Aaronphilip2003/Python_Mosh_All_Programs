command=""
start= False

while command.lower()!="quit":
    command = input("> ").lower()
    if command == "start":
        if start:
            print("Car already started!")
        else:
            start=True
            print("Car Started.....")
    elif command == "stop":
        print("Car Stopped.....")
    elif command == "help":
        print("start-to start the car")
        print("stop-to stop the car")
        print("quit-to quit the program")
        print("help-help menu")
    else:
        print("I don't understand")



