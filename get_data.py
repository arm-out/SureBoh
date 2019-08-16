import pandas as pd
import pickle

def grab_df1():
    #grabbing dataset1
    df = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")
    df = df.drop("Unnamed: 0", axis=1)
    #print(df.head)
    #df.label.value_counts()

    #pickling def
    pickle_out = open('Data/df1.pickle', 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()

'''
def grab_df2():
    #grabbing dataset2
    df = pd.read_csv("Data/fake.csv")

    l = []
    for i in range(len(df.text)):
        l.append(len(str(df.text[i])))

    l = pd.DataFrame(l)
    df['textlen'] = l

    df = df[df.language == 'english']
    df = df[(df.textlen > 500) & (df.textlen < 12000)]
    df = df[['site_url', 'title', 'text']]
    df.reset_index(drop = 'index', inplace=True)
    df.drop('site_url', axis=1, inplace=True)
    df['label'] = 'FAKE'

    #pickling df2
    pickle_out = open('Data/df2.pickle', 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()

'''

#grab_df1()
grab_df2()
