marks = {
    "nhrakib" : 100,
    "goodman" : 500,
    "raul" : 452,
    100 : "ronaldo"
}

print(marks.values())

marks.update({"raul": 550, "naymerJr": 30})

print(marks)

print(marks.get("raul5")) # prints none

print(marks["raul5"]) # prints error