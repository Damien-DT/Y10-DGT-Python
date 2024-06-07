# Fence Cost Calculator 
# Author - Damien Du Toit 
# Version 1.0 

# Greet user to the Fence Cost Calculator 
print("Welcome to the Fence Cost Calculator") 

# Ask user for all measurements. 
print("What are the desired measurements? ") 

# Ask user for the measurements, inputs need to be >0 
error = "Chosen number is not above zero, please enter a new number\n" 
while True: 

    try: 
        width = float(input("Width: ")) 
        length = float(input("Length: ")) 
        cost_per_meter = float(input("Cost per meter: "))  

        if width > 0: 
            done = True 
        if length > 0: 
            done = True 
        if cost_per_meter > 0: 
            done = True
        else: 
            print(error)  

    except ValueError: 
        print(error) 
    perimeter = (width + length * 2)
    total = (cost_per_meter * perimeter) 
    
    print(f"Perimeter is {perimeter} ")
    print(f"Total cost is {total} ") 

    if True: break



