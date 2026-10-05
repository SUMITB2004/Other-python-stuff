new = open("sample.txt", "a")                 #1)so if i write something like sample1 in "a" or "w" mode it will create new file
new.write("\nkalpy cse")                      #2)if i use "a" it will add at the end of file and if i use "w" it will override on everything 
new.close()                                              



new = open("index.html", "a")                 #it creates HTML file
new.write("<p>this is HTML file</p>")
new.close()