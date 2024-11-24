alpha = 'abcdefghijklmnopqrstuvwxyz'
path = '.\\configs\\'

def genconf(name='a'):
    if len(name) > 2:
        return

    print(name)
    with open(f"{path}{name}.py","w") as f:
        f.write(f"greeting = '{name}'\n")

    for char in alpha:
        genconf(name+char)

def generate():
    for char in alpha:
        genconf(char)


if __name__ == "__main__":
    generate()
