import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder , MinMaxScaler
from sklearn.linear_model import LogisticRegression , LinearRegression
from sklearn.tree import DecisionTreeClassifier
pd.set_option("display.max_columns",None)

df = pd.read_csv(r"C:\Users\HP\Desktop\Swiggy_project1.csv")

print(df)






def predict_price(Cuisine, Location):
    df2=pd.read_csv(r"C:\Users\HP\Desktop\Swiggy_project1.csv")
    df3=df2[['Cusines','Location','Price_for_one']]


    loc = ['malleswaram', 'basaveshwaranagar', 'basavanagudi', 'majestic',
       'j.p nagar', 'st marks road', 'tavarekere', 'banashankari',
       'koramangala', 'vijayanagar', 'ashok nagar', 'cunningham road',
       'rajarajeshwari nagar', 'uttarahalli', 'central bangalore',
       'rajajinagar', 'nagarbhavi', 'lavelle road', 'vasanth nagar',
       'kumaraswamy layout', 'gandhi nagar', 'city market',
       'sampangirama nagar', 'shivajinagar', 'chamarajpet',
       'residency road (shanti nagar)', 'wilson garden',
       'kanteshwar layout', 'adugodi', 'btm layout', 'richmond road',
       'brigade road', 'richmond town', 'prakash nagar', 'seshadripuram',
       'dr rajkumar road', 'indiranagar', 'yeshwanthpur', 'arekere',
       'ulsoor', 'frazer town', 'residency road', 'rt nagar',
       'bannerghatta main road', 'hsr layout',
       'kumaraswamy layout & uttarahalli', 'domlur', 'new bel road',
       'chandralayout', 'mathikere', 'hsr', 'btm', 'race course road',
       'shanti nagar', 'sadashiv nagar', 'btm 1st stage', 'mg road',
       'commercial street', 'bala anjaneya temple road', 'chikpete',
       'high grounds', 'ejipura', 'halasuru', 'kanakapura', 'binnipete',
       'austin town', 'bommanahalli', 'bilekahalli', 'mysore road',
       'doopanahalli, indiranagar', 'pes college hanumanth nagar',
       'audgodi', '2nd stage, btm layout', 'sanjay nagar',
       'vittal mallya road', 'hosur road', 'pattabhirama nagar',
       'azad nagar', 'church street']
    locate= sorted(loc)
    print(locate)


    food = ['South Indian', 'North Indian', 'Indian', 'Snacks', 'Desserts',
       'Biryani', 'Chinese', 'Bakery', 'Healthy Food', 'Asian',
       'Beverages', 'Sweets', 'Thalis', 'Fast Food', 'Punjabi', 'Juices',
       'Ice Cream', 'Mughlai', 'Home Food', 'Salads', 'Cafe', 'Italian',
       'American', 'Coastal', 'Oriental', 'Combo', 'Continental', 'Chaat',
       'Maharashtrian', 'Oriya', 'Tibetan', 'Burgers', 'Bengali',
       'Rajasthani', 'Seafood', 'Street Food', 'Kerala', 'Pastas',
       ' Beverages', 'Kebabs', 'Pizzas', 'Japanese', 'Andhra', 'Tandoor',
       ' Bihari', 'Konkan', 'Mexican', 'Grill', 'Jain', 'Turkish',
       'Chettinad']

    cus = sorted(food)
    print(cus)

    dict1 = {}
    for i in range(len(locate)):
        dict1[locate[i]] = i 

    dict2 = {}
    for i in range(len(cus)):
        dict2[cus[i]] = i
    
    le = LabelEncoder()
    df3['Cusines']=le.fit_transform(df3['Cusines'])
    df3['Location']=le.fit_transform(df3['Location'])

    f1=dict2[Cuisine]
    l1=dict1[Location]

    df1_new=df3[(df3['Cusines']==f1) | (df3['Location']==l1)]
    print(df1_new)

    X=df1_new.drop(['Price_for_one'],axis=1)
    y=df1_new['Price_for_one']

    lr=LinearRegression()
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=10)
    lr.fit(X_train,y_train)

    return round(lr.predict(X_test).mean())


def predict_location(Cuisine, Location, Preferred_Price_For_1):
    df = pd.read_csv(r"C:\Users\HP\Desktop\Swiggy_project1.csv")
    z = pd.DataFrame({"Cusines": [Cuisine], "Location": [Location], "Price_for_one": [Preferred_Price_For_1]})

    print(z)

    df = pd.concat([df, z])
    lst = list(df["Location"].unique())

    dict1 = {}
    for i in range(len(lst)):
        dict1[lst[i]] = i

    dict2 = {}
    for i in range(len(lst)):
        dict2[i] = lst[i]

    df["Location"] = df["Location"].apply(lambda x: dict1[x])
    df = df[["Cusines", "Location", "Price_for_one"]]  # Remove "Index" from the selected columns
    x = df.drop("Location", axis=1)
    y = df["Location"]

    le = LabelEncoder()
    x["Cusines"] = le.fit_transform(x["Cusines"])
    x["Price_for_one"] = MinMaxScaler().fit_transform(x[["Price_for_one"]])  # Normalize only "Price_For_One"

    xtr, xts, ytr, yts = train_test_split(x, y, test_size=0.3)
    model = DecisionTreeClassifier()
    model.fit(xtr, ytr)
    ypred = model.predict(xts)
    return dict2[ypred[-1]]

page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"]
    {
    background-image: url("https://i.pinimg.com/originals/e5/e8/cd/e5e8cdb29ed5ad4903470c07d6475d59.jpg");
    background-size: cover;
    }
    </style>
    ''' 
st.markdown(page_bg_img, unsafe_allow_html=True)



def main():


    
    st.markdown("<h1 style='text-align: center; color: white; padding: 20px; background-color: orange;'>RECOMMENDATION MODEL</h1>", unsafe_allow_html=True)
    
    html_temp = """
    <div style = 'background-color: orange ; padding : 0px ; max-width: 400px; margin: 20px auto;'>
    <h1 style = "color:white;text-align:center;"><b>SWIGGY</b></h1>
    </div>
    """


    st.markdown(html_temp, unsafe_allow_html = True)

    cuisines = df['Cusines'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: yellow;'><b>Cuisine:</b></h2>", unsafe_allow_html=True)
    Cuisine = st.selectbox("",cuisines)

    locations = df['Location'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: yellow;'>Preferred Location:</h2>", unsafe_allow_html=True)
    Preferred_Location = st.selectbox("",locations) 

    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: yellow;'>Preferred Price For One:</h2>", unsafe_allow_html=True)
    Preferred_Price_For_1 = st.text_input("", key="price_input")
    
    if st.button("Submit"):

        avg = round(df[(df['Cusines'] == Cuisine) | (df['Location'] == Preferred_Location)]['Price_for_one'].mean())

        a = df[(df['Location'] == Preferred_Location)]
        Pop_Cuis = a[a['Ratings'] == a['Ratings'].max()]["Cusines"]
        Pop_Cuis=Pop_Cuis.iloc[0]

        Most_Popular_Rest = a[a["Delivery_review_no"] == a["Delivery_review_no"].max()]["Restaurant_Name"]
        Most_Popular_Rest=Most_Popular_Rest.iloc[0]

        Ser = a[a["Delivery_review_no"] == a["Delivery_review_no"].max()]["Cusines"]
        Serves=Ser.iloc[0]

        b = a[(a['Cusines'] == Cuisine)]
        Popular_Rest_Serving_Your_Cuisine = b[b["Delivery_review_no"] == b["Delivery_review_no"].max()]['Restaurant_Name']
        Popular_Rest_Serving_Your_Cuisine=Popular_Rest_Serving_Your_Cuisine.iloc[0]


        Recomm_price = predict_price(Cuisine,Preferred_Location)
        Recomm_location = predict_location(Cuisine,Preferred_Location,Preferred_Price_For_1)

        st.markdown("<h2 style='font-size: 34px;margin-bottom: 0px;'><span style='color: yellow;'>Based on your Preferred Location</h2>", unsafe_allow_html=True)


        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Popular Cuisine:   {}</span>".format(Pop_Cuis), unsafe_allow_html=True)
        
        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Average Price for 1:   {}</span>".format(avg), unsafe_allow_html=True)

        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Most Popular Restaurant:  {}</span>".format(Most_Popular_Rest), unsafe_allow_html=True)
        
        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Serves:  {}</span>".format(Serves), unsafe_allow_html=True)

        st.markdown("<h2 style='font-size: 34px;margin-bottom: 0px;'><span style='color: yellow;'>Popular Restaurant that serves your Cuisine</h2>", unsafe_allow_html=True)

        
        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Popular Restaurant that serves your Cuisine: {}</span>".format(Popular_Rest_Serving_Your_Cuisine), unsafe_allow_html=True)
       
        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Recommended Price:  {}</span>".format(Recomm_price), unsafe_allow_html=True)
        
        st.markdown("<span style='color: white; font-weight: bold; font-size: 30px;'>Recommended Location:  {}</span>".format(Recomm_location), unsafe_allow_html=True)



        
               
if __name__ == '__main__':
    main()