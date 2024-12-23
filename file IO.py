f=open("poems.txt")
t=f.read()
if "twinkle" in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()


file=open("hiscore.txt","r")
c=file.read()
file.close()

new_score=int(input("Enter ur new score"))
file=open("hiscore","w")
file.write(c)

for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt", "w") as f:
        j=1
        while j<=10:
            f.write(f"{i}x{j}={i*j}\n")
        j+=1



file = open("dock.txt", "r")
content = file.read()
file.close()
content = content.replace("donkey", "######")
file = open("dock.txt", "w")
file.write(content)
file.close()
print("Words have been replaced successfully")


with open("log.txt") as f:
    y=f.read()

if "python" in y.lower():
    print("Yes Python is present")
else:
    print("Python is not present")

file = open("log.txt", "r")
for line_number, line in enumerate(file, start=1):
    if "python" in line:
        print(f"Line {line_number}: {line}")
file.close()


file= open("this.txt","r") 
content=file.read()
file.close()
copy=open("copy.txt","w")
copy.write(content)
copy.close
print("the file has been copied successfully")


with open("f1.txt") as f:
    y1=f.read()
with open("f2.txt") as f:
    y2=f.read()

if y1==y2:
    print("Both file are identical & matches the content")
else:
    print("Both file are not identical & not matches the content")



f = open("sample.txt", "r+") 
f.seek(0)  
f.truncate() 

import os   
oldfile="sample.txt"
newfile="renamed_by_python.txt"
with open(oldfile) as f:
    y=f.read()
with open(newfile,"w") as f:
   f.write(y)

os.remove(oldfile)

