
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# order to handle the layout of the project must be first line  
st.set_page_config(layout= 'wide', page_title=('india flight'))

df = pd.read_csv('cleaned_df.csv', index_col= 0)

# st.markdown("<h1 style='text-align: center;'>Internal Indian flight data analysis</h1>", unsafe_allow_html= True)



## Add the sidebar

page = st.sidebar.selectbox('Menu', ['Dataset Info', 'Analysis questions', 'comparsion'])

if page == 'Dataset Info':

    st.markdown("<h1 style='text-align: center;'>Internal Indian flights data analysis</h1>", unsafe_allow_html= True)
    st.markdown("<p> <h3> DATASET </h3> <br> Dataset contains information about flight booking options from the website Easemytrip for flight travel between India's top 6 metro cities <br> <h3>FEATURES</h3></p>", unsafe_allow_html= True)
    
    st.markdown("""<ul>
            <li>Airline-> The name of the airline.</li>
            <li>Source-> the place that person come from.</li>
            <li>Destination-> the place which person want to go.</li>
            <li>Stops Numbers-> the number of stops whichs strat with zero which mean no stops, one means one stop and so on</li>
            <li>price-> the ticket price</li>
            <li>Time Taken-> time of the flight</li>
            <li>stops Location-> if the number of stops zero it's value is no transit and if more than or equal to 1 will put the location</li>
            <li>Price Category-> the price category which contains economy, business and first class</li>
            <li>Day of the week-> the day of the flight will be</li>
            <li>Month Name-> the name of the month in which ticket booked</li>
            <li>Year-> year of the flight</li>
            <li>Arrival time-> the arrival time</li>
            <li>Departure time-> the departure time</li>
        </ul>""", unsafe_allow_html= True)

elif page == 'Analysis questions':
    st.markdown("<h1 style='text-align: center;'>Welcome to analysis questions</h1>", unsafe_allow_html= True)

    fig1 = px.box(data_frame= df, x= 'airline', y= 'price', title= 'what is the price range per airline?')

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(data_frame= df, x= 'price_category', y= 'price', height= 600, title='what is the range of prices per category? ')
    st.plotly_chart(fig2, use_container_width= True)

    fig3 = px.pie(data_frame= df, names= 'departure Time', title= 'what is the day time people most travel at?')

    st.plotly_chart(fig3, use_container_width= True)

    fig4 = px.pie(data_frame= df, names= 'airline', title= 'What is the most airline used?')
    st.plotly_chart(fig4, use_container_width= True)

    fig5 = px.histogram(data_frame= df, x= 'month_name', text_auto= True, title= 'What is most month people travel?')
    st.plotly_chart(fig5, use_container_width= True)

    fig6 = px.pie(data_frame= df, names= 'destination', title= 'What is the most city people travel to?')
    st.plotly_chart(fig6, use_container_width= True)

    day_week_df = df['day_of_week'].value_counts().reset_index()
    day_week_df['day_of_week'] = day_week_df['day_of_week'].astype(str)
    fig7 = px.bar(data_frame= day_week_df, x= 'day_of_week', y= 'count', text_auto= True, title= 'what is the day of week people travel? ')
    st.plotly_chart(fig7, use_container_width= True)

    fig8 = px.pie(data_frame= df, names= 'price_category', title= 'what is the most price category people buying?')
    st.plotly_chart(fig8, use_container_width= True)

    avg_price_airline_df = df.groupby('airline')['price'].median().sort_values(ascending= False).reset_index()
    fig9 = px.bar(data_frame= avg_price_airline_df, x= 'airline', y= 'price', text_auto= True, title= 'what is the average price for each airline ?')
    st.plotly_chart(fig9, use_container_width= True)

    profit_per_month_df = df.groupby(['airline', 'month_name'])['price'].sum().sort_values(ascending= False).reset_index()
    fig10 = px.bar(data_frame= profit_per_month_df, x= 'airline', y= 'price', facet_col= 'month_name', text_auto= True, title= 'what is the profit for each airline per month ? and is it less than the last month ?')
    st.plotly_chart(fig10, use_container_width= True)

    profit_day_df = df.groupby(['airline', 'day_of_week'])['price'].median().sort_values(ascending= False).reset_index()
    # change the day name to str
    profit_day_df['day_of_week'] = profit_day_df['day_of_week'].astype(str)
    fig11 = px.bar(data_frame= profit_day_df, x= 'airline', y= 'price', facet_col= 'day_of_week', text_auto= True, title= 'What is the average day profit per airline? ')
    st.plotly_chart(fig11, use_container_width= True)

    profit_per_category_df = df.groupby(['airline', 'price_category'])['price'].sum().sort_values(ascending=False).reset_index()
    fig12 = px.bar(data_frame= profit_per_category_df, x= 'price_category', y= 'price', facet_col= 'airline', title= 'Which price category more profitable per airline?', text_auto= True)
    st.plotly_chart(fig12, use_container_width= True)

else:


    options = ['-- Select --','Price', 'Time taken']
    
    selection = st.sidebar.radio('Choose what you want comparsion on ', options)

    if selection == '-- Select --':
        # st.info("Please choose a comparison category from the sidebar.")

        st.markdown("""
                    <style>
                        table, th, td {
                            border: 1px solid black;
                            border-collapse: collapse;
                            padding: 8px;
                        }
                        th {
                            background-color: #f2f2f2;
                        }
                    </style>

                    <h3>In this section we have four comparisons: Price, Time Taken, Number of Stops, and Busiest Day</h3>

                    <table>
                        <tr>
                            <th>Item</th>
                            <th>Description</th>
                        </tr>
                        <tr>
                            <td>Price</td>
                            <td>This compares the price of tickets based on airline. You should choose two different cities.</td>
                        </tr>
                        <tr>
                            <td>Time Taken</td>
                            <td>This compares the time taken between two different cities based on airline.</td>
                        </tr>
                       
                        
                    </table>
                    """, unsafe_allow_html=True)





    elif selection == 'Price':
        
        #create options 
        from_options = np.append('-- select --', sorted(df['source'].unique()))
        to_options = np.append('-- select --', sorted(df['destination'].unique()))

        from_choice = st.selectbox('choose where you come from.', from_options)
        to_choice = st.selectbox('choose where you want to go.', to_options)

        #handle if select choosed which is defalut

        if (from_choice == '-- select --') or (to_choice == '-- select --'):
            st.warning('please enter two different cities and not include -- select -- between them')

            
        else:

            filtered = df[(df['destination'] == to_choice)  & (df['source'] == from_choice)]

            if filtered.empty:
                st.warning('please choose two diff cities')

            else:
                compare_price_df = df.groupby(['airline', 'price_category'])['price'].median().sort_values(ascending=False).reset_index()
                fig1 = px.bar(data_frame= compare_price_df, x= 'price_category', y= 'price', facet_col= 'airline', title= 'What is the average price per airline', text_auto= True)

                st.plotly_chart(fig1,  use_container_width=True)

        
    elif selection == 'Time taken':
        
        #sorce, destination and time departuer options 
        from_options = np.append('-- select --', sorted(df['source'].unique()))
        to_options = np.append('-- select --', sorted(df['destination'].unique()))
        departure_time = np.append('-- select --',df['departure Time'].unique())

        #sorce, destination  and departure time choices
        from_choice = st.selectbox('Choose where you come from.', from_options)
        to_choice = st.selectbox('Choose where you want to go.', to_options)
        departure_time_choice = st.selectbox('Choose departure time.', departure_time)

        if (from_choice == '-- select --') or (to_choice == '-- select --') or (departure_time_choice== '-- select --'):
            st.warning('please don\'t select -- select -- in any of them and choose two different cities')

        elif from_choice == to_choice:
            st.warning('Please choose two different cities')

        else:
            filter_by_time_df = df[(df['departure Time'] == departure_time_choice) & (df['destination'] == to_choice) & (df['source'] == from_choice)]
            fig_time = px.box(data_frame= filter_by_time_df, x= 'airline', y= 'time_taken')
            st.plotly_chart(fig_time, use_container_width= True)
