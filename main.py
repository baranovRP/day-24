with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("file_to_write", mode="a") as file:
    file.write("New text")
