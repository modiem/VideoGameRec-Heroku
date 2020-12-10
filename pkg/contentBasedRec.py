
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from pkg.utils import *
import wikipedia


class ContentRecommender(object):

    def __init__(self, example = 'Beyblade Burst', top_num = 3):
        self.top_num = top_num
        self.example = example
        self.latent_df = get_latent_df()
        self.vector = np.array(self.latent_df.loc[self.example]).reshape(1, -1)
        self.sim = cosine_similarity(self.latent_df, self.vector).reshape(-1)

    def get_recommendation(self):
        recommendation_df = pd.DataFrame({'content': self.sim}, index = self.latent_df.index)
        recommendation_df = recommendation_df.sort_values('content', ascending = False)
        recommendation = recommendation_df.head(self.top_num + 1).index.tolist()
        try:
            recommendation.remove(self.example)
        except:
            pass
        return recommendation

    # def game_info(self.name):
    #     pass

    
    
    
    




