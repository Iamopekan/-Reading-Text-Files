# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here

file = open('story.txt','r')
f = file.readlines()

print(f)
    
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

file = open("story.txt","r")
count=0
for line in file:
    words = line.split(" ")
    count =+ len(words)
file.close()
print("Number of words in a Text File : ", count)

    return {"as": 10, "would": 20}
