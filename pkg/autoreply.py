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

def autoreply(review_score, name, product):
    if str(name) == "nan":
        name = "Customer"
    if review_score == 0:
        return f('''Dear {name}, we are terribly sorry that '{product}' didn't meet your expectations.
        We have a few options for you.
        First of all, you can  send us back the package and get a full refund.
        Another option is to ask for a discount code that you will be able to use on your next Amazon order. 
        We hope to see you again soon! The Amazon Team We would like to propose you another product : {recommandation}. 
        It has repetitively gotten good reviews!''')
        
    elif review_score == 1:
        return (f'''Dear {name}, We are glad to hear that you are satisfied with '{product}'.
        Based on your purchase history, we would also like to recommand you following products {recommandation},
        which is a similar product that has repetitively gotten good reviews.
        We hope to see you again soon!
        The Amazon Team''')



