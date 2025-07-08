**Analysis of the Linguistic Style of Social Robot "Comment Robert" Based on Sina Weibo Data**
**Project Overview**
This project aims to analyze the linguistic style and emotional tendencies of the social robot "Comment Robert" on the Sina Weibo platform and explore its specific impact on user interactions.    Through data analysis and natural language processing (NLP) techniques, this study investigates how "Comment Robert" interacts with users, revealing how its humorous and friendly language style enhances user engagement on the platform.

**Research Objectives:**
Investigate how the linguistic style of "Comment Robert" affects user interaction.
Use sentiment analysis to understand user attitudes and feedback towards the robot.
Provide recommendations for the optimization of social robots based on the findings, ensuring the sustained development of such technologies.

**Data Source**
The data for this research was collected from the Sina Weibo platform between January 1, 2024, and May 1, 2024, which includes 8965 Weibo posts and 9613 comments.    The data contains information such as user IDs, post IDs, posting times, content of posts, comments, likes, shares, and more.

**Data Processing:**
Data Cleaning: Removal of punctuation, numbers, and stopwords.
Tokenization: Chinese text was tokenized using the jieba library.
Stopword Filtering: We used the ChineseStopWords.txt file to filter out irrelevant words.
Sentiment Analysis: We used Baidu's AI sentiment analysis API to analyze the sentiment of the comments.

**Usage**
Install Dependencies:
pip install pandas jieba wordcloud matplotlib chardet aip

**Data Files:**
ChineseStopWords.txt: Contains the stopwords list for text preprocessing.
Comment_Robert_Data.xls: Contains the Weibo data (replace with actual data path).
wordfrequency.py: A script for performing word frequency analysis and generating word cloud diagrams.
nlplinebyline.py: A script for performing sentiment analysis on the comments.
weibocomment.py: A web scraper script to collect and clean Weibo data.

**Instructions:**
Word Frequency Analysis: Run wordfrequency.py to perform word frequency analysis on the Weibo data and generate word clouds.
Sentiment Analysis: Run nlplinebyline.py to perform sentiment classification of comments using Baidu's AI sentiment analysis API.
Data Scraping: Run weibocomment.py to collect data from Weibo and clean it for analysis.

**Key Results**
Sentiment Tendencies: The sentiment analysis shows that approximately 92% of the comments on "Comment Robert" are positive, reflecting users' highly favorable responses to the robot's interactions.
Language Style: Word frequency analysis reveals that users predominantly respond to "Comment Robert" with positive, humorous, and interactive language.
Challenges & Recommendations: The research also discusses the challenges faced by social robots, such as potential incitement of actions, limitations in emotional recognition, and privacy and security concerns, and provides suggestions for their improvement.

**Contribution**
This study provides a detailed analysis of "Comment Robert" and its impact on user interaction, offering valuable insights into how social robots influence social media environments.    The findings also contribute to the theoretical and practical development of similar robots in the future.

**Future Work**
Emotional Recognition Optimization: Improve the emotional recognition and emotional intelligence of social robots.
Privacy Protection: Strengthen privacy protection for users and ensure the legal use of data.
Multi-domain Applications: Explore the use of social robots in other fields such as education and therapy.

**Acknowledgements**
We would like to express our sincere gratitude to Professor Huang Yifan for his invaluable guidance and support throughout this research.    
We also thank the team members Yingying Jiang and Jinyao Li for their hard work and contributions.
