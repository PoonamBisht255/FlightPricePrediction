
import streamlit as st
import numpy as np
import time
import pickle

pickle_in = open("rf_random22.pkl" ,"rb")
dec_cl = pickle.load(pickle_in)

st.title('Flight price prediction')

st.image("flight_price_img.png",width = 800)


st.header("Predict flight price here")

total_stops = st.slider("enter total stops " ,0 ,10)

Airline1 = ['Air India' ,'GoAir' ,'IndiGo' ,'Jet Airways' ,'Jet Airways Business' ,'Multiple carriers'
            ,'Multiple carriers Premium economy' ,'SpiceJet' ,'Trujet' ,'Vistara' ,'Vistara Premium economy']
Airline = st.selectbox('enter airlines', Airline1)

Source1 = ['Kolkata' ,'Delhi' ,'Chennai' ,'Mumbai']
Source = st.selectbox('enter source', Source1)

Destination1 =  ['Kolkata' ,'Delhi' ,'Cochin' ,'Hyderabad' ,'New Delhi']
Destination = st.selectbox('enter destination', Destination1)

Journey_day = st.number_input("Enter journey date" ,0 ,31 ,step = 1)

Journey_month = st.number_input("Enter journey month" ,0 ,12 ,step = 1)

Dep_Time_hour = st.number_input("Enter dep hours" ,0 ,30 ,step = 1)

Dep_Time_minute = st.number_input("Enter dep minute" ,0 ,60 ,step = 2)

Arrival_Time_hour = st.number_input("Enter arrival hours" ,0 ,30 ,step = 1)

Arrival_Time_minute = st.number_input("Enter arrival minute" ,0 ,60 ,step = 2)

Duration_hours = st.number_input("Enter duration hours" ,0 ,40 ,step = 1)

Duration_mins = st.number_input("Enter duration minute" ,0 ,60 ,step = 2)



cat_list = ['air_line' ,'air_line2' ,'air_line3' ,'air_line4' ,'air_line5' ,'air_line6' ,'air_line7' ,'air_line8'
            ,'air_line9' ,'air_line10' ,'air_line11' ,'s_1' ,'s_2' ,'s_3' ,'s_4' ,'d_1' ,'d_2' ,'d_3' ,'d_4' ,'d_5']

for i in cat_list:
    exec("%s = %d" % (i ,0))

if Airline1 == 'Air India':
    air_line = 1
elif Airline1 == 'GoAir':
    air_line2 = 1
elif Airline1 == 'IndiGo':
    air_line3 = 1
elif Airline1 == 'Jet Airways':
    air_line4 = 1
elif Airline1 == 'Jet Airways Business':
    air_line5 = 1
elif Airline1 == 'Multiple carriers':
    air_line6 = 1
elif Airline1 == 'Multiple carriers Premium economy':
    air_line7 = 1
elif Airline1 == 'SpiceJet':
    air_line8 = 1
elif Airline1 == 'Trujet':
    air_line9 = 1
elif Airline1 == 'Vistara':
    air_line10 = 1
elif Airline1 == 'Vistara Premium economy':
    air_line11 = 1
else:
    pass

if Source1 == 'Kolkata':
    s_1 = 1
elif Source1 =='Delhi':
    s_2 = 1
elif Source1 =='Chennai':
    s_3 = 1
elif Source1 =='Mumbai':
    s_4 = 1
else:
    pass

if Destination1 == 'Kolkata':
    d_1 = 1
elif Destination1 == 'Delhi':
    d_2 = 1
elif Destination1 == 'Cochin':
    d_3 = 1
elif Destination1 == 'Hyderabad':
    d_4 = 1
elif Destination1 == 'New Delhi':
    d_5 = 1
else:
    pass



val = np.asarray \
    ([total_stops ,air_line ,air_line2 ,air_line3 ,air_line4 ,air_line5 ,air_line6 ,air_line7 ,air_line8 ,air_line9
     ,air_line10 ,air_line11 ,s_1 ,s_2 ,s_3 ,s_4 ,d_1 ,d_2 ,d_3 ,d_4 ,d_5 ,Journey_day ,Journey_month ,Dep_Time_hour
     ,Dep_Time_minute ,Arrival_Time_hour ,Arrival_Time_minute ,Duration_hours ,Duration_mins]).reshape(1 ,-1)

pred = dec_cl.predict(val)

if st.button("Predict"):

    progress = st.progress(0)    # this is for progress bar
    for i in range(100):
        time.sleep(0.001)
        progress.progress( i +1)

    st.success('The price is {}'.format(pred))

