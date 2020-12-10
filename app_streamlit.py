import streamlit as st
from pkg.utils import *
from pkg.autoreply import autoreply
from pkg.contentBasedRec import ContentRecommender
import joblib
from PIL import Image


# tmp until the feature is released
st.set_page_config(
    page_title="Video Game Fanatic",
    page_icon="🐍",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed


def get_model():
    return model


def main():

    sections = st.sidebar.selectbox("choose the section", ["About Us", "Introduction", "Demo"])

    if sections == "About Us":
        col1, col2, col3 = st.beta_columns(3)

        img = Image.open("images/1.jpg")
        col1.header("Matthieu")
        col1.image(img, width = 200)

        img = Image.open("images/2.jpg")
        col2.header("Nicola")
        col2.image(img, width = 200)

        img = Image.open("images/3.jpg")
        col3.header("Mo")
        col3.image(img, width = 200)

        

    if sections == "Introduction":
        model_name = st.selectbox("Which Model do We Use?", ["NaiveBayes", "Logistic"])
        model = joblib.load('NaiveBayes.joblib')
        # st.smage(img, caption = "Learning Curve")
        if st.button("Show Parameters of the Model"):
            st.code(model.get_params())


    if sections == "Demo":

        st.header("Tell us What do you feel about your last Purchase!")
        st.markdown("### Exciting ###")

        ## input from user
        user_name = st.text_input("Please Enter Your Name", "Type here...")
        if st.button("submit"):
            result = user_name.title()
            st.success(f"Thank You {result}")
        
        game_list = get_game_lst()
        game_name = st.selectbox("What is the Game you purchased?", game_list)

        rec = ContentRecommender(example = game_name)
        recommendation = rec.get_recommendation()

 

        message = st.text_area("Enter Your Message", "I Love this game!")
        message = preprocess(message)

       
        model_name = st.selectbox("Which Model?", ["NaiveBayes", "Logistic"])
        
        
        model = joblib.load(f"{model_name}.joblib")

        pred = model.predict([message])


        if st.button("Submit the Review"):
            reply = autoreply(review_score = pred, name=user_name, product=game_name, recommandation = recommendation)
            if pred == 1:
                st.success(reply)
            else:
                st.warning(reply)

if __name__ == "__main__":
    #df = read_data()
    main()
