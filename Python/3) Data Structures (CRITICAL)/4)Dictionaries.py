month = {
    "jan": "january",         #we can also use num instead of "jan"
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun":  "june",
    "jul":  "july",
    "aug": "august",
    "sep": "sepetember",
    "oct": "octomber",
    "nov": "november",
    "dec": "december"
}

print(month)
print(month["jan"])
print(month.get("luv", "not a valid key"))            #gives the output as a not a valid key