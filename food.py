import streamlit as st
from PIL import Image
import toml
from streamlit_image_select import image_select

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
    st.title("Berchook AI for Chef Jean-Pierre")
    st.write("Hey there! What’s cookin’? Looking for breakfast, lunch, dinner, or a dessert idea?")

    meal_images = {
        "Breakfast": "breakfast.jpg",
        "Lunch": "lunch.jpg",
        "Dinner": "dinner.jpg",
        "Dessert": "dessert.jpg"
    }
    st.markdown("<b>Meal Choice</b>", unsafe_allow_html=True)
    meal_choice = image_select(
        label="",
        images=[meal_images[key] for key in meal_images.keys()],
        captions=list(meal_images.keys())
    )
    
    if meal_choice == "dinner.jpg":
        st.write("Cool! What are you in the mood for? Beef, chicken, lamb, or veggies?")
        
        protein_images = {
            "Beef": "beef.jpg",
            "Chicken": "Best-Roasted-Chicken-Recipe-1080x675.jpg.webp",
            "Lamb": "lamb.jpg",
            "Veggies": "veg.webp"
        }

        protein_choice = image_select(
            label="Protein Choice",
            images=[protein_images[key] for key in protein_images.keys()],
            captions=list(protein_images.keys())
        )

        if protein_choice == "Best-Roasted-Chicken-Recipe-1080x675.jpg.webp":
            st.write("Got it! How much time do you have to whip up something tasty? Less than 30 mins, 30-60 mins, or more than an hour?")
            cook_time_choice = st.selectbox("Cook Time", ["Less than 30 mins", "30-60 mins", "More than an hour"])


            if cook_time_choice == "More than an hour":
                st.write("Awesome. How do you wanna cook it? Grill, bake, fry, or slow cook?")
                
                cooking_method_images = {
                    "Grill": "grill.jpg",
                    "Bake": "bake.jpg",
                    "Fry": "fry.jpg",
                    "Slow Cook": "slow.jpg"
                }

                cooking_method_choice = image_select(
                    label="Cooking Method",
                    images=[cooking_method_images[key] for key in cooking_method_images.keys()],
                    captions=list(cooking_method_images.keys())
                )

                if cooking_method_choice == "bake.jpg":
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
