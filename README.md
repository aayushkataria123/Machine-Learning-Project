# Restaurant-Recommendation-Model

## Introduction

Welcome to the Restaurant Recommendation Model repository! This project aims to provide you with restaurant suggestions based on data scraped from the Swiggy website for the Bangalore location.



##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="48" height="48"> **User's Manual**

| Files/Folder| Description |
| ------------- | ------------- |
| **Files Folder** | This folder provides data Files  |
| **FinalData File** | This contains the excel file of the analysis for Data Extract and Data cleaning.  |
| **ML_Project_web File** | This contains the .ipynb file for the model building.  |
| **updatedwebpage File** | This contains the .py file for the webpage building.  |



<br>

<p align="center"><img src="https://camo.githubusercontent.com/9873bda0ab2987caef5c0d8255c0daf4f447dc9b889389651bf3bc52d5f9e9bd/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f656e2f7468756d622f312f31322f5377696767795f6c6f676f2e7376672f3132303070782d5377696767795f6c6f676f2e7376672e706e67" width="400" ></p>



## Problem Aimed to Solve:

1.Personalized Recommendations: Delivering Tailored Dining Experiences  

2.Exploration Made Easy: Effortless Discovery of New Restaurants

3.User-Centric Engagement: Enhancing Satisfaction and Convenience

4.Data-Driven Insights: Empowering Restaurant Owners with Market Knowledge

5.Algorithmic Excellence: Crafting Precise and Relevant Recommendations

6.Interactive Webpage: Seamlessly Navigating Culinary Choices for New Ventures





## Methodology

The following methodology was used to accomplish the project objectives:

1. _Data Scraping:_We've harnessed the power of Selenium and BeautifulSoup in Python to scrape restaurant data from the Swiggy website. Selenium enables us to interact with the website, while BeautifulSoup helps extract relevant information from the HTML content

2. _Data Conversion:_ Utilizing Excel, the scraped data underwent transformation into  table.

3. _Data Cleaning and Preparation:_ The collected data has undergone thorough cleaning using Excel and Python(pandas). This process includes handling missing values, removing duplicates, and ensuring data consistency.

4. _Prediction:_ 
Price Prediction using Linear Regression : Developed a linear regression model that predicts restaurant prices based on the chosen location and cuisine. This model provides estimates of restaurant prices based on specific features.
Location Prediction using Logistic Regression and Random Forest Classifier : Developed a Logistic Regression and Random Forest Classifier model that predicts location  based on the chosen prices and cuisine.

5. _User-Friendly Interface:_ Our project culminates in an interactive webpage powered by the Streamlit library in Python.

## Results

### 1. This webpage is designed to accept user input for cuisine,preferred location and preferred price for one.
<p align="center">
  <img width="800" alt="image" src="https://github.com/AnjaliBakshi17/Restaurant-Recommendation-Model/blob/main/Image/ImageHosting/1.jpeg">
</p>

<p align="center">
  <img width="800" alt="image" src="https://github.com/AnjaliBakshi17/Restaurant-Recommendation-Model/blob/main/Image/ImageHosting/2.jpeg">
</p>

### 2. The webpage generates output based on the Preferred Location and Cuisine by the users.

<p align = "center">
<img width="800" alt="image" src="https://github.com/AnjaliBakshi17/Restaurant-Recommendation-Model/blob/main/Image/ImageHosting/3.jpeg">
</p>



## Challenges:

- Scrapping Data from the swiggy dynamic site.
- Building various models to get better Accuracy.
- Creating Webpage with the help of Streamlit Library,Basic HTML and Basic CSS Styling.
- Creating a backend with Streamlit and returning output to a webpage.
- Understanding the different ways to deploy the model.


## Future Scope

Real-Time Data Integration: Automating data scraping to collect real-time restaurant information, ensuring that users receive the most up-to-date recommendations.

Mobile App Development: Expanding the project with a mobile app to reach a wider audience and provide real-time, on-the-go restaurant recommendations based on user preferences and location.

User Profiles and Ratings: Implementing user profiles, integrating real-time user reviews and ratings, and offering personalized restaurant suggestions for an enhanced and dynamic user experience.

Promotion and Marketing: Incorporate tools for new restaurant owners to promote their establishments through the platform, including advertising opportunities, special promotions, and partnerships to increase visibility and customer engagement for their businesses.


## Contributions

Contributions to this project are highly encouraged! Should you encounter any issues or have ideas for improvement.
Please create a pull request.

## Acknowledgements

We extend our gratitude to Swiggy for sharing the restaurant data that underpins this recommendation model. 
Furthermore, we express our appreciation to the open-source community for providing valuable tools and libraries that empower this project.
Your feedback is invaluable as we strive to refine the project and enhance user experiences.
Thank you for engaging with our interactive webpage.
