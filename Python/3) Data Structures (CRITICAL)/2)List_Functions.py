lucky_numbers = [5, 8, 7, 77, 6]
friends = ["ketan", "uday", "amit", "kalpesh", "om"]

# friends.extend(lucky_numbers)       #it will extend the list
friends.insert(1,"radhe")             #insertion using index number
friends.append("sumit")               #add value at the end of list
friends.remove("amit")                #remove value
friends.sort()                        #sorts list in alphabeticl order
friends.reverse()                     #reverse the list

friends2 = friends.copy()             #copies the list and create another list using existing

print(friends2)
# print(friends.index("kalpesh"))     #guve the index of element
# print(friends.count("kalpesh"))     #counts the total number of elements present in the list