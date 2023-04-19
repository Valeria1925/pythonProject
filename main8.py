f = open('New file1.txt', 'w')
with open('New file.txt', 'r') as f1:
    line = f1.read()
line_1 = line[::-1]
f.write(line_1)
f.close()





