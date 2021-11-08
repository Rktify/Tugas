import os
def hapax(s):
    word = s.split()
    for i in word:
        if i in end:
            end[i] += 1
        else:
            end[i] = 1
    return end

os.chdir("/Users/Wilbert")
file = open("Book.txt", "r")

s = file.read().lower()
end = dict()
end = hapax(s)

for i in end:
    if end[i] == 1:
        print(i)

file.close()