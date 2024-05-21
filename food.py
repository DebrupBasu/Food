import streamlit as st
from PIL import Image
import base64
import io
import toml

def load_config():
    try:
        with open("config.toml", "r") as config_file:
            config = toml.load(config_file)
        return config
    except FileNotFoundError:
        print("Config file not found.")
        return None


def main():
    config = load_config()
    st.image("Group 265.png")
    st.title("Dinner Chatbot")
    st.write("Hey there! What’s cookin’? Looking for breakfast, lunch, dinner, or a snack idea?")
    meal_choice = st.text_input("Meal Choice", "")

    if meal_choice.lower() == "dinner":
        st.write("Cool! What are you in the mood for? Chicken, beef, veggies, or something else?")
        protein_choice = st.text_input("Protein Choice", "")

        if protein_choice.lower() == "chicken":
            st.write("Got it! How much time do you have to whip up something tasty? Less than 30 mins, 30-60 mins, or more than an hour?")
            cook_time_choice = st.text_input("Cook Time", "")

            if cook_time_choice.lower() == "more than an hour":
                st.write("Awesome. How do you wanna cook it? Bake, grill, fry, or slow cook?")
                cooking_method_choice = st.text_input("Cooking Method", "")

                if cooking_method_choice.lower() == "bake":
                    st.write("Any diet goals or restrictions I should know about? Like keto, gluten-free, vegan, etc.?")
                    diet_restrictions = st.text_input("Diet Restrictions", "")

                    st.write("Sweet! What flavors are you feelin’? Spicy, savory, herbal, or sweet?")
                    flavors_choice = st.text_input("Flavors", "")

                    st.write("What’s in your fridge or pantry? Any specific ingredients you wanna use?")
                    ingredients = st.text_input("Ingredients", "")

                    st.write("How many calories are you aiming for in this meal?")
                    calories = st.number_input("Calories", min_value=0, step=10)

                    st.write("Is this for a special occasion or just a regular night in?")
                    occasion = st.radio("Occasion", ["Special Occasion", "Regular Night In"])

                    if st.button("Get Dinner Recommendation"):
                        # Recommendation logic based on inputs
                        recommendation = recommend_dinner(flavors_choice, ingredients, calories, occasion, ingredients)
                        st.write(recommendation)

def recommend_dinner(flavors, servings, calories, occasion, ingredients):
    # Hardcoded recommendation for roast chicken
    return f"How about a roast chicken with potatoes and carrots? It’s delish and should fit your calorie goal."

if __name__ == "__main__":
    main()
