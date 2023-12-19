with open('example.txt','r') as file:
    lines = file.readlines()

    if len(lines) >= 2:
        # print(lines[1].strip())
        print(lines[1])
    
    else:
        print("The file does not have enough lines.")