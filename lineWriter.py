
# - add some transcription lines from file

#filename = input("what is the name of the file")

#if filename == "y":
filename = "arctic20.transcription"
# arctic_a0121
# need to find last line and take note of the number
# need to make sure you add the 0 before the output number
# use this number as the start pointer for the line to be transcribed
# alternativly Enter it manually

#line = input("enter current fileline")

file = open("transcript", "r") ##write functions

if (file == ''):
    file = open("transcript", "w")
    file.close()

file = open("transcript", "r") ##write functions

lines = [line.rstrip('\n') for line in file]
lines2 = []
for line in lines:
    #line.rstrip(('.'))
    line = line.replace('"', "")
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.replace("-", " ")
    line = line.replace("—", " ")
    line = line.replace("'", "")
    line = line.replace(";", "")
    lines2.append(line)


file.close()
print (lines2)



fileA = open(filename, "w")
fileA.write("this is out new text file \n")
fileA.write("and this is a new ewew line \n")
#<s> Text </s> (arctic_a0089)
p = 126
i = 126
newid =0
limit = p + len(lines2)
while p < limit:
    text = "<s> "
    ln = '{0:04}'.format(p)
    newLine = lines2[newid]
    transcriptline = f"{newLine}"
    text += transcriptline
    text += " </s>"
    text += f" (arctic_a{ln}) \n"
    fileA.write(text)
    p += 1
    newid+=1

fileA.close()


file2 = open("arctic20.fileids","w")##write functions


while i < limit:
    ln2 = '{0:04}'.format(i)
    text2 = f"arctic_a{ln2}\n"
    file2.write(text2)
    i += 1

file2.close()

#for i in range(10):
#    nu = '{0:04}'.format(i)
#    print(nu)
