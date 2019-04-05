

file = input("Enter the filename:")
output = input("Enter new filename:")
f = open(file,'r')
filedata = f.read()
f.close()

find = input("Enter phrase to search for:")
replace = input("Enter phrase to replace it with: ")
newdata = filedata.replace(find, replace)

f = open(output,'w')
f.write(newdata)
f.close()