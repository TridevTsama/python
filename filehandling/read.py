def line_count(a):
    with  open (a,"r") as f:
        count=0
        for i in f:
            count +=1
        return count
print(line_count("file.txt")) 


def word_count(a):
    with open (a,"r") as f:
        data=f.read()
        words=data.split()
        count=len(words)
        return count
print(word_count("file.txt"))

def ch_count(a):
    with open (a,"r") as f:
        data = f.read()
        count=len(data)
        return count
print(ch_count("file.txt"))  

def line_count(a):
    try:
        with open (a,"r") as f:
            count = 0
            for i in f:
                count+=1
            return count
    except:
        print("file not found")
print(line_count("file.txt"))        
        
        
def read_lines(a):
    with open(a,"r") as f:
        data=f.read()
        print(data)
read_lines("file.txt")

def read_line(a):
    with open (a,"r") as f:
        data=f.readline()
        return data
print(read_line("file.txt"))  


def read_lines(a):
    with open(a,"r") as f:
        data = f.readlines()
        return data
print(read_lines("file.txt")) 




def word_freq(a):
    with open(a,"r") as f:
        data=f.read()
        word= data.split()
        freq={}
        for i in word:
            if i in freq:
                freq[i]+=1
            
            else:
                freq[i]=1
        return freq
print(word_freq("file.txt"))    



