import streamlit as st
from PIL import Image
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
    st.write("Hey there! What’s cookin’? Looking for breakfast, lunch, dinner, or a dessert idea?")
    meal_choice = st.selectbox("Meal Choice", ["Breakfast", "Lunch", "Dinner", "Dessert"])

    if meal_choice.lower() == "dinner":
        st.write("Cool! What are you in the mood for? Chicken, beef, lamb, or veggies?")
        protein_choice = st.selectbox("Protein Choice", ["Chicken", "Beef", "Lamb", "Veggies"])

        if protein_choice.lower() == "chicken":
            st.write("Got it! How much time do you have to whip up something tasty? Less than 30 mins, 30-60 mins, or more than an hour?")
            cook_time_choice = st.selectbox("Cook Time", ["Less than 30 mins", "30-60 mins", "More than an hour"])

            if cook_time_choice.lower() == "more than an hour":
                st.write("Awesome. How do you wanna cook it? Bake, grill, fry, or slow cook?")
                cooking_method_choice = st.selectbox("Cooking Method", ["Bake", "Grill", "Fry", "Slow Cook"])

                if cooking_method_choice.lower() == "bake":
                    st.write("Any diet goals or restrictions I should know about? Like keto, gluten-free, vegan, etc.?")
                    diet_restrictions = st.text_input("Diet Restrictions", "")

                    st.write("Sweet! What flavors are you feelin’? Spicy, savory, herbal, or sweet?")
                    flavors_choice = st.selectbox("Flavors", ["Spicy", "Savory", "Herbal", "Sweet"])

                    st.write("What’s in your fridge or pantry? Any specific ingredients you wanna use?")
                    ingredients = st.text_input("Ingredients", "")

                    st.write("How many calories are you aiming for in this meal?")
                    calories = st.number_input("Calories", min_value=0, step=10)

                    st.write("Is this for a special occasion or just a regular night in?")
                    occasion = st.radio("Occasion", ["Special Occasion", "Regular Night In"])

                    if st.button("Get Dinner Recommendation"):
                        # Recommendation logic based on inputs
                        recommendation = recommend_dinner(flavors_choice, ingredients, calories, occasion)
                        st.write(recommendation)
                        # Display roast chicken image
                        st.image("Best-Roasted-Chicken-Recipe-1080x675.jpg.webp", caption="Roast Chicken with Potatoes and Carrots", use_column_width=True)
                        # Provide recipe link
                        st.write("Check out the recipe [here](https://chefjeanpierre.com/recipes/roasted-chicken/).")
                        # Provide product purchase link
                        st.write("Want to buy the ingredients and tools needed? [Click here](https://chefjeanpierre.com/recipes/roasted-chicken/)")

def recommend_dinner(flavors, ingredients, calories, occasion):
    # Hardcoded recommendation for roast chicken
    return f"How about a roast chicken with potatoes and carrots? It’s delish and should fit your calorie goal."

if __name__ == "__main__":
    main()
