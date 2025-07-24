import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('data/products.csv')
df['category'] = df['category'].fillna('').apply(lambda x: x.replace('|', ' '))
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['category'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['productName']).drop_duplicates()

def get_recommendations(product_name, num=5):
    if product_name not in indices:
        return []
    idx = indices[product_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    product_indices = [i[0] for i in sim_scores]
    return df['productName'].iloc[product_indices].tolist()
