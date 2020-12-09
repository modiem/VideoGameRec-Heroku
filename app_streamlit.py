import streamlit as st
from VideoGame.utils import *
from VideoGame.autoreply import autoreply
from VideoGame.contentBasedRec import ContentRecommender


def main():

    sections = st.sidebar.selectbox("choose the section", ["About Us", "Introduction", "Demo"])

    if sections == "About Us":
        pass

    if sections == "Introduction":
        model_name = st.selectbox("Which Model do We Use?", ["Naive Bayes", "Logistic"])
        model = get_model(model_name = model_name)
        # st.smage(img, caption = "Learning Curve")
        if st.button("Show Parameters of the Model"):
            st.code(model.get_params())


    if sections == "Demo":
        model  = "PUT THE MODEL HERE"
        print("load model")

        st.header("Tell us waht how do you feel about your last Purchase!")

        ## input from user
        user_name = st.text_input("Please Enter Your Name", "Type here...")
        if st.button("submit"):
            result = user_name.title()
            st.success(f"Thank You {result}")
        
        game_list = get_game_lst()
        game_name = st.selectbox("What is the Game you purchased?", game_list)

        rec = ContentRecommender(example = game_name)
        recommendation = rec.get_recommendation()

        review_score = 1

        message = st.text_area("Enter Your Message", "I Love this game!")
        if st.button("Submit the review"):
            reply = autoreply(review_score, name=user_name, product=game_name, recommandation = recommendation)
            if review_score == 1:
                st.success(reply)
            else:
                st.warning(reply)

if __name__ == "__main__":
    #df = read_data()
    main()
