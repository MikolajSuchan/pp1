def f(dictionary,grade):
        if grade in dictionary["subject"]["grades"]:
            return True
        else:
            return False

print(f({"subject":{"grades":[3,4,5]}},5))