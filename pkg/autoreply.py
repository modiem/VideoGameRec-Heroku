#main function
import pandas as pd

def global_autoreply(data):
    string_list = []
    for i, row in data.iterrows():
        cat = row.category
        if len(cat) == 0 or len(cat) == 1:
            df.drop(index, inplace = True)
            continue
        name = get_name(data.name[i])
        product = get_product(data.title[i])
        recommandation = get_recommandation(data.product_to_recommand[i])
        string = autoreply(data.Rating[i], name, product, recommandation)
        string_list.append(string)
    data["autoreply"] = string_list



#all the functions that are called

def autoreply(review_score, name, product, recommandation):
    if str(name) == "nan":
        name = "Customer"
    if review_score == 0:
        return f('''Dear {name}, we are terribly sorry that '{product}' didn't meet your expectations.\n
        We have a few options for you.\n
        First of all, you can  send us back the package and get a full refund.\n 
        Another option is to ask for a discount code that you will be able to use on your next Amazon order. \n
        We hope to see you again soon! The Amazon Team. We would like to propose you another product : {recommandation}. It has repetitively gotten good reviews!''')
        
    elif review_score == 1:
        return (f'''Dear {name}, We are glad to hear that you are satisfied with '{product}'.\n 
        Based on your purchase history, we would also like to recommand you following products {recommandation}, \n
        which is a similar product that has repetitively gotten good reviews. \n
        We hope to see you again soon!
        The Amazon Team''')



