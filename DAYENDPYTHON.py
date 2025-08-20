# we can read and write data 
# f=open("demo.txt","r")
# data=f.read()
# print(data)


# r for readig
# w for writing and truccating the file first(overwrite)
# x create a new file and open it for writing
# a open for writing , appending to the end the file if it exist
# b binary mode
#t text mode(default)
# + open a disk file for updating(reading and writing)

# line1 =f.readline()
# line2=f.readline()
# print(line1)
# print(line2)
# f.close()

#writing to a file
# f=open("demo.txt","w")
# z=f.write("hi my name is uday ")
# print(z)
# f.close()

# we also can open the file with setence 
#ex. with open("demo.txt","r")as f:
# data=f.read()
# print(data) 
#with with stetamnet it automaticaaly close the file

#deleting a file
# import os
#os.remove(filename)

#Practice question 1
f=open("practice.txt","r")
data=f.read()
new_data=data.replace("python","JAVA")
print(new_data)
f=open("practice.txt","w")
data=f.write(new_data)