# WhatsApp Chat Analyzer

This Streamlit application analyzes WhatsApp chat logs, providing insights into communication patterns, busiest times, and popular words used in the conversations. It supports analysis for overall chat activity and individual user contributions.


## Screenshots 

(Add screenshots of your app in action here)
![Screenshot 2025-01-30 112127](https://github.com/user-attachments/assets/97006436-e923-4895-890f-bf8a39938911)
![Screenshot 2025-01-30 112433](https://github.com/user-attachments/assets/ed3e70bf-6db2-4f35-aff0-c4d80cbed672)
![Screenshot 2025-01-30 112340](https://github.com/user-attachments/assets/40bc85e8-cf30-4e63-9129-30bcd5da27b3)
![Screenshot 2025-01-30 112321](https://github.com/user-attachments/assets/4c5fa6d6-135c-476b-92be-6d36b02a64c8)
![Screenshot 2025-01-30 112241](https://github.com/user-attachments/assets/67685b67-7e65-460d-ad9a-02625b174368)


## Table of Contents

- [Features](#features)
- [Deployment](#deployment)
- [How to Use](#how-to-use)
- [Code Structure](#code-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Screenshots](#screenshots) (Optional)
- [Contributing](#contributing) (Optional)
- [License](#license) (Optional)

## Features

- **Overall Chat Statistics:** Displays total messages and words exchanged.
- **Individual User Statistics:** Provides the same statistics for a selected user.
- **User Chat Percentage:** Visualizes the contribution of each user in the chat.
- **Busy Members:** Identifies the most active members in the group chat.
- **Word Cloud:** Generates a word cloud to show the most frequent words used.
- **Common Words:** Displays the most common words in a horizontal bar chart.
- **Monthly Timeline:** Shows message frequency over time (monthly).
- **Daily Timeline:** Shows message frequency over time (daily).
- **User-Specific Analysis:** All visualizations and statistics are available for individual users as well as the overall chat.

## Deployment

This app is deployed on Render.  You can access it at https://whatsanalyse.onrender.com

To deploy your own version of this app, follow these steps:

1.  **Create a Render account:** If you don't have one, sign up for a Render account.
2.  **Create a new web service:** In your Render dashboard, create a new web service.
3.  **Connect your repository:** Connect your GitHub (or other Git provider) repository that contains this code.
4.  **Configure the build:**
    -   Build command: `pip install -r requirements.txt`
    -   Publish directory: `.` (or your appropriate directory)
5.  **Set environment variables:** If you need to set any environment variables (e.g., API keys), do so in the Render dashboard.
6.  **Deploy:** Deploy your web service.

## How to Use

1.  **Upload Chat Log:** In the Streamlit app, upload your exported WhatsApp chat log file (as a `.txt` file).
2.  **Select User:** Choose a user from the dropdown menu in the sidebar. Select "Overall" for group chat analysis.
3.  **Show Analysis:** Click the "Show Analysis" button.
4.  **View Results:** The app will display various statistics, charts, and visualizations based on the selected user or overall chat activity.

## Code Structure

-   `app.py`: The main Streamlit application file, handling user interface and calling processing functions.
-   `processor.py`: Contains functions for parsing and processing the raw chat data.
-   `helper.py`: Contains helper functions for data analysis, visualization, and generating word clouds.
-   `requirements.txt`: Lists the required Python libraries for the app.

## Requirements

-   Python 3.7+
-   Streamlit
-   Pandas
-   Matplotlib
-   Seaborn
-   WordCloud
-   Urlextract
-   Emoji

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/)[Your GitHub Username]/[Your Repository Name].git
    ```

2.  **Navigate to the directory:**

    ```bash
    cd [Your Repository Name]
    ```

3.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv  # Create a virtual environment
    source venv/bin/activate  # Activate the environment (Linux/macOS)
    venv\Scripts\activate  # Activate the environment (Windows)
    ```

4.  **Install the requirements:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the app:**

    ```bash
    streamlit run app.py
    ```

