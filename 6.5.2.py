class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_ratings = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.food_ratings:
                self.food_ratings[cuisine] = []
            self.food_ratings[cuisine].append((food, rating))
    def changeRating(self, food, newRating):
        for cuisine in self.food_ratings.values():
            for i in range(len(cuisine)):
                if cuisine[i][0] == food:
                    cuisine[i] = (food, newRating)
                    return
    def highestRated(self, cuisine):
        max_rating = float('-inf')
        max_food = None
        for food, rating in self.food_ratings[cuisine]:
            if rating > max_rating or (rating == max_rating and food < max_food):
                max_rating = rating
                max_food = food
        return max_food

# Simulate the input
inputs = ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
values = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

foodRatings = None
output = []

for i in range(len(inputs)):
    if inputs[i] == "FoodRatings":
        foodRatings = FoodRatings(*values[i])
        output.append(None)
    elif inputs[i] == "highestRated":
        output.append(foodRatings.highestRated(values[i][0]))
    elif inputs[i] == "changeRating":
        foodRatings.changeRating(*values[i])
        output.append(None)

print("Output:", output)

