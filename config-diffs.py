import difflib

#Open up test1.txt and test2.txt files
with open("test1.txt") as text1, open("test2.txt") as text2:
    #Read the text files and store them in diff
    diff = difflib.ndiff(text1.readlines(), text2.readlines())
#Write the contents of diff into diff.txt file
with open("diff.txt", "w") as result:
    for output in diff:
        result.write(output)
        print(output)
