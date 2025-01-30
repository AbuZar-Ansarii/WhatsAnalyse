# from wordcloud import WordCloud
# import string
# from nltk.corpus import stopwords
# def fetch_stats(selected_user, df):
#     # fetch messages
#     if selected_user == "Overall":
#         num_messages = df.shape[0]
#         # fetch words
#         words = []
#         for i in df["Chat"]:
#             words.extend(i.split())
#             t_words = len(words)
#         return num_messages, t_words
#     else:
#         new_df = df[df["Name"] == selected_user]
#         num_messages = new_df.shape[0]
#         words = []
#         for i in new_df["Chat"]:
#             words.extend(i.split())
#             t_words = len(words)
#         return num_messages, t_words


# def busy_user(df):
#     x = df["Name"].value_counts().head()
#     dff = round((df["Name"].value_counts().head(10) / df.shape[0]) * 100, 2).reset_index().rename(
#         columns={"index": "Name", "count": "Percentage"})
#     return x,dff

# def create_wordcloud(selected_user,df):
#     if selected_user != "Overall":
#         df = df[df["Name"] == selected_user]

#     wc = WordCloud(width=500,height=500,max_font_size=60,background_color='white')
#     df_wc = wc.generate(df["Chat"].str.cat(sep=" "))
#     return df_wc


# def clean_text(input_list):
#     # Load English stopwords
#     stop_words = set(stopwords.words('english'))

#     # Create a translation table to remove punctuation
#     translator = str.maketrans('', '', string.punctuation)

#     cleaned_list = []
#     for sentence in input_list:
#         # Remove punctuation
#         no_punctuation = sentence.translate(translator)
#         # Split sentence into words, remove stopwords, and join back
#         cleaned_sentence = ' '.join(
#             word for word in no_punctuation.split() if word.lower() not in stop_words
#         )
#         cleaned_list.append(cleaned_sentence)

#     return cleaned_list
import re
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['Chat']:
        words.extend(message.split())

    return num_messages, len(words)

def busy_user(df):
    x = df['Name'].value_counts().head()
    dff = round((df['Name'].value_counts() / df.shape[0]) * 100, 2).reset_index(name='Percent')
    return x, dff

def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['Chat'].str.cat(sep=" "))
    return df_wc

def clean_text(words):
    temp = []
    for w in words:
        w = w.lower()
        if w not in emoji.UNICODE_EMOJI_ALIAS:
            temp.append(w)

    return temp

def monthly_timeline(df):
    timeline = df.groupby(['Year', 'Month']).count().reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(f"{timeline['Month'][i]}-{timeline['Year'][i]}")

    timeline['time'] = time
    timeline = timeline[['time', 'Message']]
    timeline.rename({'Message': 'Message Count'}, axis=1, inplace=True)
    return timeline

def daily_timeline(df):
    daily_timeline = df.groupby('Date').count().reset_index()
    daily_timeline.rename({'Message': 'Message Count'}, axis=1, inplace=True)
    return daily_timeline

def week_activity_map(df):
    period = []
    for i in df[['Day_name', 'Hour']]['Hour']:
        if i == 23:
            period.append('23-0')
        elif i == 0:
            period.append('0-1')
        else:
            period.append(f'{i}-{i+1}')
    df['Period'] = period
    active_heatmap = pd.pivot_table(df, index="Day_name", columns="Period", values="Message", aggfunc='count').fillna(0)
    return active_heatmap

def most_active_day(df):
    busy_day = df['Day_name'].value_counts().head(1)
    return busy_day

def most_active_month(df):
    busy_month = df['Month'].value_counts().head(1)
    return busy_month

def clear_df(name):
    return name.split(',')[0]
