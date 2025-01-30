import streamlit as st
from collections import Counter
import pandas as pd
import processor, helper
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page layout
st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

st.sidebar.title("WhatsApp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Upload patient data text file", type="txt")

if uploaded_file is not None:
    try:
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

            if selected_user != "Overall":
                df_selected = df[df['Name'] == selected_user].copy()  # Filter for selected user
            else:
                df_selected = df.copy() # Use the overall df if "overall is selected"

            num_messages, t_words = helper.fetch_stats(selected_user, df_selected) #pass the correct dataframe to the helper functions

            st.title("Statistics")
            col1, col2 = st.columns(2)

            with col1:
                st.header("Total Messages")
                st.subheader(num_messages)
            with col2:
                st.header("Total Words")
                st.subheader(t_words)

            # User chat percentage (Improved with seaborn)
            st.header("User Chat Percentage")
            fig, ax = plt.subplots()
            user_counts = df["Name"].value_counts()
            sns.set_palette("pastel")  # added colour
            ax.pie(user_counts.head(10), labels=user_counts.index[:10], autopct='%1.1f%%', startangle=90)  # limit to top 10
            st.pyplot(fig)

            # ... (rest of your Streamlit code)

            if selected_user == "Overall":
                # st.title("Busy Members")
                col1, col2 = st.columns(2)
                x, dff = helper.busy_user(df) #use overall df here
                fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size
                sns.set_palette("viridis")  # added colour

                with col1:
                    st.header("Most Busy Member")
                    sns.barplot(x=x.index, y=x.values, ax=ax)  # use seaborn for better bar plot
                    plt.xticks(rotation=40, ha='right')  # Improved rotation
                    st.pyplot(fig)


            # Word cloud (Handles both Overall and individual user)
            st.header("Word Cloud")
            df_wc = helper.create_wordcloud(selected_user, df_selected) # Pass the correct df
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            plt.axis("off")
            st.pyplot(fig)

            # Common words (Handles both Overall and individual user)
            words = []
            for i in df_selected["Chat"]:  # Use df_selected here
                words.extend(i.split())
            cleaned_list = helper.clean_text(words)
            wd_df = pd.DataFrame(Counter(cleaned_list).most_common(20), columns=["Words", "Count"])

            st.header("Most Common Words")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x='Count', y='Words', data=wd_df, ax=ax, palette='Blues_r')  # Horizontal bar chart
            st.pyplot(fig)

            # Monthly timeline (Handles both Overall and individual user)
            st.header("Monthly Timeline")
            timeline = helper.monthly_timeline(df_selected) # Pass the correct df
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x=timeline['time'], y=timeline['Message Count'], ax=ax, color='coral')
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

            # Daily timeline (Handles both Overall and individual user)
            st.header("Daily Timeline")
            daily_timeline = helper.daily_timeline(df_selected) # Pass the correct df
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x=daily_timeline['Date'], y=daily_timeline['Message Count'], ax=ax, color='mediumseagreen')
            plt.xticks(rotation="vertical")
            st.pyplot(fig)


    except ValueError as e:
        st.error(str(e))
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.stop()
