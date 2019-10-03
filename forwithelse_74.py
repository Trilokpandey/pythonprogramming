#use of else with for loop
#if item will be in the list else statement won't print

food=["roti","sabji","dal"]

for item in food:
    if item=="paratha":
        break
else:
    print("item not found")