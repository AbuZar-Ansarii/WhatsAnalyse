import streamlit as st
from collections import Counter
import pandas as pd
import processor, helper
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for better plotting

# Set Streamlit page layout
st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

st.sidebar.title("Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = processor.process(data)
    df["Name"] = df["Name"].apply(processor.clear_df)

    st.header("DataFrame of Your Chats")
    st.dataframe(df)

    user_list = df["Name"].unique().tolist()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Select User", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, t_words = helper.fetch_stats(selected_user, df)

        st.title("Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Total Messages")
            st.write(num_messages)
        with col2:
            st.header("Total Words")
            st.write(t_words)

        # User chat percentage (Improved with seaborn)
        st.header("User Chat Percentage")
        fig, ax = plt.subplots()
        user_counts = df["Name"].value_counts()
        sns.set_palette("pastel") #added colour
        ax.pie(user_counts.head(10), labels=user_counts.index[:10], autopct='%1.1f%%', startangle=90) #limit to top 10
        st.pyplot(fig)

        if selected_user == "Overall":
            st.title("Busy Members")
            col1, col2 = st.columns(2)
            x, dff = helper.busy_user(df)
            fig, ax = plt.subplots(figsize=(10,6))  # Adjust figure size
            sns.set_palette("viridis") #added colour

            with col1:
                st.header("Most Busy Member")
                sns.barplot(x=x.index, y=x.values, ax=ax) #use seaborn for better bar plot
                plt.xticks(rotation=45, ha='right')  # Improved rotation
                st.pyplot(fig)
            with col2:
                st.header("Top Busy Members")
                st.dataframe(dff)

            # Monthly timeline
            st.header("Monthly Timeline")
            timeline = helper.monthly_timeline(df)
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x=timeline['time'], y=timeline['Message Count'], ax=ax, color='coral')
            plt.xticks(rotation="vertical")
            st.pyplot(fig)


            # Daily timeline
            st.header("Daily Timeline")
            daily_timeline = helper.daily_timeline(df)
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x=daily_timeline['Date'], y=daily_timeline['Message Count'], ax=ax, color='mediumseagreen')
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

            # Week activity map
            st.header("Week Activity Map")
            activity_heatmap = helper.week_activity_map(df)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(activity_heatmap, cmap="YlGnBu", ax=ax)
            st.pyplot(fig)

            # Most active day
            st.header("Most Active Day")
            busy_day = helper.most_active_day(df)
            st.write(busy_day)

            # Most active month
            st.header("Most Active Month")
            busy_month = helper.most_active_month(df)
            st.write(busy_month)


        # Word cloud (No change needed, but good as is)
        st.header("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        plt.axis("off")
        st.pyplot(fig)

        # Common words (Improved with seaborn and horizontal bar chart)
        words = []
        for i in df["Chat"]:
            words.extend(i.split())
        cleaned_list = helper.clean_text(words)
        wd_df = pd.DataFrame(Counter(cleaned_list).most_common(20), columns=["Words", "Count"])

        st.header("Most Common Words")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='Count', y='Words', data=wd_df, ax=ax, palette='Blues_r') # Horizontal bar chart
        st.pyplot(fig)
