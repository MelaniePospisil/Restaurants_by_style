#what do you want to eat? - Restaurant recomendation

#the lists to choose from
styles = ["italian", "german", "american", "french", "vietnamese", "japanese"]
italian_restaurants=["La Nonna", "Bocconchino", "Soulkitchen"]
german_restaurants=["Hofbräuhaus", "Heimwerk"]
american_restaurants=["Hans im Glück", "Bagels and Donuts", "McDonalds"]
french_restaurants=["Hoiz", "Rocca Rivera", "Guy Sauvage"]
vietnamese_restaurants=["SOY", "PhoYou", "Bami House"]
japanese_restaurants=["TOKAMI", "Tenmaya"]
added_by_user = []

style_to_restaurant_dic = {}
style_to_restaurant_dic["italian"] = italian_restaurants
style_to_restaurant_dic["german"] = german_restaurants
style_to_restaurant_dic["american"] = american_restaurants
style_to_restaurant_dic["french"] = french_restaurants
style_to_restaurant_dic["vietnamese"] = vietnamese_restaurants
style_to_restaurant_dic["japanese"] = japanese_restaurants



#the talking methods
def say_hi():
    print("----------------------------")
    print("Welcome to RESTAURANT SEARCH.")
    print("----------------------------")
    print("Today I will help you to find the restaurant you didn't know you were looking for!")
    print("")
    name = input("But first let me know your name: ")
    print("")
    print("Oh, hi " + name + ".")
    print("")

def ask_for_style():
    style = input("So what country do you want your tastebuds to travel? (To see the full list of available styles type \"Help\":  ")
    print("")
    if style == "Help":
        print("You can choose between: ")
        print("")
        print("\n".join(styles))
        print("")
        ask_for_style()
    elif style not in styles:
        print("Oh no, I couldn't find this style. Try again!")
        print("") 
        ask_for_style()
    else:
        return style

def adding_restaurants():
    print("So there are restaurants you want to add?")
    print("")
    new_style = input("What style of food does the restaurant serve? (Enter the country): ")
    print("")
    new_rest = input ("And what is the restaurant's name?: ")
    if new_style in styles:
        style_to_restaurant_dic[new_style].append(new_rest)
    else:
        style_to_restaurant_dic[new_style] = [new_rest]
        added_by_user.append(new_rest)
    print("")
    print("Thanks!")

    
def say_bye():
    print("It was a plessure. Hope you are happy and to see you soon!")
    print("<3")

#the main method
def the_food_guide(again = 0):
    if again == 0:
        say_hi()
    choice = input("So are you looking for restaurants (type 1) or do you want to add one to the list? (type 2): ")
    if choice == "1":
        print("")
        style = ask_for_style()
        print("")
        print("Here are the restaurants that I can recommend you: ")
        print("")
        print("\n".join(style_to_restaurant_dic[style]))
        print("")
        end = input("Do you want to end the session?: ")
        if end == "Yes":
            say_bye()
            return
        else:
            print("")
            the_food_guide(1)
    elif choice == "2":
        adding_restaurants()
        end = input("Do you want to end the session?: ")
        if end == "Yes":
            say_bye()
            return
        else:
            the_food_guide(1)
    else:
        print("I am sorry, i didn't understand you. Try again.")
        the_food_guide(1)
    
the_food_guide()





