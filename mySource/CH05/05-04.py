def ask(prompt = "Please enter a value: "):
    if prompt.endswith(" "):    
        return input(prompt)
    else:
        return input(prompt + " ")
    

a = ask()

print(a)