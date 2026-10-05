is_male = False
is_tall = False

if (is_male and is_tall):
    print("you are a male and tall")
elif (is_male and not(is_tall)):
    print("you are a short male")
elif (not(is_male) and is_tall):
    print("you are not a male but you are tall")        
else:
    print("you neither a male nor a tall")