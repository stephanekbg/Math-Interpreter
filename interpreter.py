def main():
    
    # The Rules and Logic for the Program
    # re inside the READEME File 
    # check it for more information
    
    # Get expression from user
    expression = input("enter your rithetich expression: ")
    
    # Split them into 3 to have the first the operand and
    # the second number  
    x , y , z = expression.split(" ")
    
    x = int(x)
    z = int(z)
    
    # have conditionals for each of the 4 main
    # arithmetic operand for y
    
    if y == "+":
        result = x + z
        result = float(result)
        print(result)
    elif y == "-":
        result = x - z
        result = float(result)
        print(result)
    elif y == "/":
        result = x / z
        result = float(result)
        print(result)
    else:
        result = x * z
        result = float(result)
        print(result)
    
        
        
    # Another way to make the result at 1 decimal
    # position
    
    # if(y == "+"):
    #     print(f"{x + z: .1f}")

    # elif(y == "-"):
    #     print(f"{x - z: .1f}")
    # elif (y == "/"):
    #     print(f"{x / z: .1f}")
    # else:
    #     print(f"{x * z: .1f}")
        
    
    
main()