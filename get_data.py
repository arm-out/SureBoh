import pandas as pd
import pickle

def grab_df1():
    #grabbing dataset1
    df = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")
    df = df.drop("Unnamed: 0", axis = 1)
    print(df.head)

    #pickling def
    pickle_out = open('df1.pickle', 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()

grab_df1()
