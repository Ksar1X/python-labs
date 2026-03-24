result = lambda x, y: y in x
print("Letter was founded in string" if result("Python".lower(), "z") else "Letter wasn't founded in string")
print("Letter was founded in string" if result("Python".lower(), "p") else "Letter was not founded in string")
