import streamlit as st
from pkg.utils import *
# from pkg.autoreply import autoreply
from pkg.contentBasedRec import ContentRecommender
import joblib
from PIL import Image
from urllib.request import urlopen
import pickle
import webbrowser



st.set_page_config(
            page_title="VideoGameSquad", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # 
            


sections = st.sidebar.selectbox("choose the section", ["About Us","Demo"])




if sections == "About Us":


    st.title("🎡 🎡 Play Hard!  Play Smart!  🧮 🧮 ")

    st.markdown("### Let's meet the squad!")

    col1, col2, col3 = st.beta_columns(3)
    img1 = Image.open("images/1.png")   
    col1.image(img1, use_column_width=True)
    col1.markdown("### 🧝🏻 Matthieu ")
    col1.text(" ")

    

    img2 = Image.open("images/2.png")
    col2.image(img2, use_column_width=True)
    col2.markdown("### 🦹🏻‍♂️ Nicola ")
    col2.text(" ")

    

    img3 = Image.open("images/3.png")
    col3.image(img3, use_column_width=True)
    col3.markdown("### 🧛‍♀️ Mo ‍")
    col3.text(" ")

    

    my_expander = st.beta_expander('Our Favorite Game:')
    with my_expander:
        col1, col2, col3 = st.beta_columns(3)
        col1.markdown("### Call of Duty 🕵🏻‍♂️")
        col2.markdown(" ### The Longest 5 Minutes ⌛️")
        col3.markdown(" ### Duck Hunt 🐣")

if sections == "Demo":

    st.title("Tell us what do you think about your last Purchase!")

    ########################
    ## User put in his name
    ########################
    user_name = st.text_input("What's your name?", "lovely Customer")
    # if st.button("submit"):
    #     st.success(easter_egg(user_name))

    ########################
    ## User put in his name
    ########################
    game_list = get_game_lst()
    game_name = st.selectbox("Which game?", game_list)   


    ########################
    ## User put in his name
    ########################
    message = st.text_area("Your review...", "I Love this game!")
    message = preprocess(message)
    
    
    with open("model_try.plk", "rb") as file:
         model = pickle.load(file)
    pred = model.predict([message])
   
    
    if st.button("Submit the Review"):
        my_expander = st.beta_expander('New Message! 📬 📬 ')
        with my_expander:
            if pred == 0:
    
                st.markdown(" ")
                st.markdown(" ")
                st.markdown(f"## Dear 👑 **{user_name.capitalize()}**   👑,")
                st.markdown(" ")
                st.markdown(f"## we are terribly sorry that **{game_name}** didn't meet your expectations.   😔")
                st.markdown("## Of course, you can get a full refund.")
                st.markdown("## Please give us a second chance and check the special recommendations we prepared for you.")
                st.markdown(" ")
                st.markdown(" ")
            else:
                st.markdown(" ")
                st.markdown(" ")
                st.markdown(f"## Dear 👑 **{user_name.capitalize()}**   👑,")
                st.markdown(" ")
                st.markdown(f"## We are glad to hear that you are satisfied with **{game_name}**.  🎊")
                st.markdown("## Want more games?")
                st.markdown("## Please check out the recommendations.")
                st.markdown(" ")
                st.markdown(" ")

        
        rec = ContentRecommender(example = game_name)
        game1 = rec.get_recommendation()[0]
        game2 = rec.get_recommendation()[1]
        game3 = rec.get_recommendation()[2]

        
        
        
        my_expander_2 = st.beta_expander('The First Recommendation!')
        with my_expander_2:
            st.subheader(f"{game1} 🤖")
            st.markdown(" ")

            st.markdown(f"### {game_summary(game1)[0]}")
            st.markdown(" ")

            url = get_img_url(game1)
            try:
                img = Image.open(urlopen(url))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                st.image(img, width = 300)
            except:
                pass
            st.markdown(" ")
        
        my_expander_3 = st.beta_expander('The Second!')
        with my_expander_3:
            st.subheader(f"{game2} 👾")
            st.markdown(" ")
            
            st.markdown(f"### {game_summary(game2)[1]}")
            st.markdown(" ")

            url = get_img_url(game2)
            try:
                img = Image.open(urlopen(url))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                st.image(img, width = 300)
            except:
                pass
            st.markdown(" ")
 
        my_expander_4 = st.beta_expander('One more? Sure!')
        with my_expander_4:
            st.subheader(f"{game3} 🤖")
            st.markdown(" ")

            st.markdown(f"### {game_summary(game3)[2]}")
            st.markdown(" ")

            url = get_img_url(game3)
            try:
                img = Image.open(urlopen(url))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                st.image(img, width = 300)
            except:
                pass
            st.markdown(" ")

        


 



    my_expander_4 = st.beta_expander("Feedback", expanded=False)
    with my_expander_4:
        st.markdown("Do you like this recommendation?")
    
        feedback = st.radio(" ", ('No opinion.', 'Awesome Recommendation. Keep giving me that!!!', 'Interesting... Let me know when the price drops.', 'Total garbage!!'))
        if feedback == 'Awesome Recommendation. Keep giving me that!!!':
            st.balloons()

        





if sections == "Introduction":
    # model_name = st.selectbox("Which Model do We Use?", ["NaiveBayes", "Logistic"])
    # model = joblib.load('NaiveBayes.joblib')
    # st.code(model)
    # # st.smage(img, caption = "Learning Curve")
    # if st.button("Show Parameters of the Model"):
    #     st.code(model.get_params())
    pass

