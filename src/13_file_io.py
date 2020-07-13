"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("foo.txt") as f:
    for line in f:
        print(line, end="")
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "w") as f:
    f.write("There is some good in this world, Mr. Frodo. And it's worth fighting for.")
    f.write("\n")
    f.write("Even the smallest person can change the course of the future.")
    f.write("\n")
    f.write("The time will soon come when Hobbits will shape the fortunes of all.")
    f.write("\n")
    f.close()