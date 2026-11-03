def vacuum_agent(location, status_A, status_B):
    if location == "A" and status_A == "Dirty":
        return "SUCK"
    elif location == "B" and status_B == "Dirty":
        return "SUCK"
    elif status_A == "Dirty":
        return "LEFT"
    elif status_B == "Dirty":
        return "RIGHT"
    else:
        return "NO-OP"


def vacuum_simulation(initial_location, initial_status_A, initial_status_B):
    location = initial_location
    status_A = initial_status_A
    status_B = initial_status_B
    
    print("\nSimulation Steps:")
    
    while True:
        action = vacuum_agent(location, status_A, status_B)
        
        # Display the action taken first
        print(f"Action: {action}")
        
        if action == "NO-OP":
            break
            
        if action == "SUCK" and location == "A":
            status_A = "Clean"
        elif action == "SUCK" and location == "B":
            status_B = "Clean"
        elif action == "LEFT":
            location = "A"
        elif action == "RIGHT":
            location = "B"
            
        # Display environment state immediately after the action completes
        print(f"Location: {location}, Room A: {status_A}, Room B: {status_B}")
        
    print("\nOutput:")
    print(f"Final Location: {location}")
    print(f"Room A: {status_A}")
    print(f"Room B: {status_B}")


if __name__ == "__main__":
    print("Input:")
    initial_loc = input("Initial Location: ").strip()
    room_a_status = input("Room A: ").strip()
    room_b_status = input("Room B: ").strip()
    
    vacuum_simulation(initial_loc, room_a_status, room_b_status)
