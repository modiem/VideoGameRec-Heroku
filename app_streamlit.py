import streamlit as st
from pkg.utils import *
from pkg.autoreply import autoreply
from pkg.contentBasedRec import ContentRecommender
import joblib
from PIL import Image

sections = st.sidebar.selectbox("choose the section", ["About Us", "Introduction", "Demo"])

#### Cache the elements for prediction
@st.cache(suppress_st_warning=True)
def load_model():
    model = joblib.load(f"NaiveBayes.joblib")
    return model

@st.cache(suppress_st_warning=True)
def get_games():
    game_list = get_game_lst()
    return game_list


### Easter_egg
@st.cache(suppress_st_warning=True)
def easter_egg(inputt):
    names = ["benjamin martin", "carlotta lukarsch", "carly", "chongqing wang", "harrison", "lars", "leo bierbach", "marnix sliepenbeek", "nour din saffour", "tjerk kostelijk"]
    for name in names:
        if (inputt.lower() in name) or (name in inputt.lower()):
            string = "This Review Has not been taken into account as " + inputt + " is retarded"
            return string.capitalize()
        else:
            string = "Thank you " + inputt.Capitalize()
            return string


if sections == "About Us":
    col1, col2, col3 = st.beta_columns(3)

    img1 = Image.open("images/1.jpg")
    col1.header("Matthieu")
    col1.image(img1, width = 200)

    img2 = Image.open("images/2.jpg")
    col2.header("Nicola")
    col2.image(img2, width = 200)

    img3 = Image.open("images/3.jpg")
    col3.header("Mo")
    col3.image(img3, width = 200)





if sections == "Demo":

    st.markdown("## Tell us What do you think about your last Purchase!")

    ########################
    ## User put in his name
    ########################
    user_name = st.text_input("Please Enter Your Name", "Type here...")
    if st.button("submit"):
        st.success(easter_egg(user_name))

    ########################
    ## User put in his name
    ########################
    game_list = get_games()
    game_name = st.selectbox("What is the Game you purchased?", game_list)   


    ########################
    ## User put in his name
    ########################
    message = st.text_area("Enter Your Message", "I Love this game!")
    message = preprocess(message)
    model = load_model()
    pred = model.predict([message])
   

    if st.button("Submit the Review"):
        reply = autoreply(review_score = pred, name=user_name, product=game_name, recommandation = recommendation)
        if pred == 1:
            st.success(reply)
        else:
            st.warning(reply)

    rec = ContentRecommender(example = game_name)
    recommendations = rec.get_recommendation()
    for i in recommendations:
        st.markdown(i)





if sections == "Introduction":
    # model_name = st.selectbox("Which Model do We Use?", ["NaiveBayes", "Logistic"])
    # model = joblib.load('NaiveBayes.joblib')
    # st.code(model)
    # # st.smage(img, caption = "Learning Curve")
    # if st.button("Show Parameters of the Model"):
    #     st.code(model.get_params())
    pass

