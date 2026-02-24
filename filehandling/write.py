def write_lines(a):
    try:
        with open (a,"w") as f:
            f.writelines("hello python ")
    except:
        print("file not found")
print(write_lines("file.txt"))    


   