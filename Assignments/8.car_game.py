command = ""
started = False
while True:
    command = input("> ").upper()
    if command == "START":
        if not started:
            print("Car started... Ready to go!")
            started = True
        else:
            print("Car already running!")
    elif command == "STOP":
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Car already stopped!")
    elif command == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "QUIT":
        break
    else:
        print("I don't understand")

