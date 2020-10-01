my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append('cannoli')
friends_food.append('ice cream')

for food in my_foods:
    print(food)

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's faorite foods are:")
for food in friends_food:
    print(food)