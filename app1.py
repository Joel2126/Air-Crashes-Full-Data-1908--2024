import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import re
import plotly.express as px

def load_data():
    df = pd.read_csv("aircrahesFullDataUpdated_2024.csv")

    df['Country/Region'].fillna("unknown", inplace = True)

    df.fillna({'Operator': "unknown"}, inplace = True)

    df.loc[:,"Country/Region"] = df.loc[:,"Country/Region"].str.replace("'-", "unknown").str.replace('The', 'unknown').str.replace("?", 
    '').str.replace('Djibouti\tDjibouti', 'Djibouti').str.replace('Tajikistan\tMilitary', 'Tajikistan').str.replace("Prov.", 
    "Province").str.replace("Surrey", "unknown").str.replace('10', 'unknown').str.replace('Black', 'unknown').str.replace("Norway\tCHC", 
    "Norway").str.replace("Brazil\tAmazonaves", "Brazil").str.replace("India\tPawan", "India").str.replace('110', 
    'unknown').str.replace("116", "unknown").str.replace("\r\n", '').str.replace("unknown0", "unknown").str.replace("Brazil\tLoide", 
    "Brazil").str.replace('near', 'unknown').str.replace('miles', 'unknown').str.replace("Reunion", 
    "unknown").str.replace("Virginia.American", "Virginia").str.replace("SC", 
    "Scotland").str.replace("DR","DominicanRepublic").str.replace("US", "United States").str.replace('Inner', 
    'unknown').str.replace("Chile\tAerolineas", "unknown").str.replace("Volcano", "unknown").str.replace("18", 
    "unknown").str.replace("Newfoundlandu.s.", "unknown").str.replace('N', "unknown").str.replace("1unknown", 
    "unknown").str.replace("570", "unknown").str.replace("800", "unknown").str.replace("325", "unknown").explode().str.strip()



    location_mapping = {'OT': 'Ontario', 'NSW': 'New South Wales', 'New': 'Newfoundland', 'NYUS': 'New York', 'ON': 'unknown', 
    'Channel': 
    'unknown', 'SK': 'Saskatchewan', 'Sri': 'Sri Lanka', 'USSRAeroflot': 'unknown', 'Spain\tMoron': 'Spain', 'United': 'United States', 
    'Upper': 'unknown',
                    'BC': 'British Columbia', 'unknownevada': 'Nevada', 'unknownew': 'unknown', 'unknownewfoundland': 'Newfoundland', 
    'unknownicaragua': 'Nicaragua', 'unknowniger': 'Niger', 'unknownigeria':'Nigeria', 'unknownorth':'North', 'unknownorthern':'North', 
    'unknownorway': 'Norway', 'unknownYUnited States': 'United States', 'Ounknown': 'unknown', 'unknownebraska':'Ebraska', 
    'unknownepal': 
    'Epal', 'unknownunavut': 'Unavut', 'unknownorthwest':'Northwest', 'unknownWT':'unknown', 'WYUnited States':'United States', 
    'unknownE': 'unknown', 'unknownorrbotten':'Orrbotten', 'unknownorfork':'Orfork', 'unknownamibia':'Namibia', 'unknownapal': 'Apal', 
    'unknownuevo': 'Uevo', 'Qld.': 'Queensland', 'unknownova':'unknown', 'United StatesSRBalkan':'United States'
                    ,'unknownetherlands' :'Netherlands', 'Brazil\tLoide': 'unknown', 'PQ': 'Quebec', 'San': 'San Francisco','Airlines': 
    'unknown','Da': 'unknown', 'NWT': 'Northwest Territories', 'off': 'unknown', 'WA': 'Washington State','WYUS': 'unknown', 'El': 
    'unknown', 'HIPan': 'unknown', 'Indonesia\tSarmi': 'Indonesia', 'Los': 'Los Angeles','NSW': 'New South Wales', 'PE': 'Peru', 
    'Rio':'Rio de Janeiro', 'UARMisrair': 'United Arab Republic','Warks': 'unknown', 'Air': 'unknown', 'D.C.Air': 'Congo', 
    'Minnesota46826/unknown9': 'Minnesota', 'NE': 'New England','Qld': 'Queensland', 'U.S.': 'United States', 'Western': 'unknown', 
    'HIAir': 'unknown', 'Covington/Hebron': 'Covington','Great': 'Great Britain', 'OLD': 'unknown', 'QC': 'Quebec', 'Azerbaijan\tBakou': 
    'Azerbaijan', 'CADuncan': 'unknown','Mt.': 'Mount', 'St.': 'Saint Petersburg', 'BrazilFlorianopolis': 'unknown', 'FL': 'Florida', 
    'de': 'unknown', 'Sao': 'São Paulo'}

    df['Country/Region'] = df['Country/Region'].apply(lambda x: location_mapping.get(x.strip(), x))


    def fix_incomplete_parentheses(text):
        if '(' in text and ')' not in text:
            return text + ')'
        else:
            return text
        
        df['Aircraft Manufacturer'] = df['Aircraft Manufacturer'].apply(fix_incomplete_parentheses)

    df.loc['Aircraft Manufacturer'] = df.loc[:,'Aircraft Manufacturer'].str.replace("?", '').str.replace("\r\n", 
    '').str.replace('Hawker Siddeley Trident 2E /', 'Hawker Siddeley Trident 2E ').str.replace('Mi', 'Mil').str.replace('C', 
    'unknown').str.replace('HS', 'unknown').str.replace('Unknown /', 'unknown').str.replace('H', 'unknown').str.replace('UH', 
    'BellHelicopter').str.replace('CH', 'unknown').str.replace('CF', 'unknown').str.replace('?42', 
    'unknown').str.replace('PA','PiperAircraft').str.replace('DC', 'Douglas Aircraft Company').str.replace('Let', 
    'Let410UVP').str.replace('L', 'unknown').str.replace('B', 'unknown').str.replace('?139', 'unknown').str.replace('?', '', 
     regex=False).str.replace('139', 'unknown').explode().str.strip()


    df.loc[:,"Aircraft Manufacturer"]=df.loc[:,"Aircraft Manufacturer"].str.replace("?", "unknown").str.replace('C', 'C47(DC)')


    def fix_incomplete_parentheses(text):
        if '(' in text and ')' not in text:
            return text + ')'
        else:
            return text
            
            df['Aircraft'] = df['Aircraft'].apply(fix_incomplete_parentheses)

    
    df.loc[:,"Aircraft"]=df.loc[:,"Aircraft"].str.strip("?")



    df['Location'] = df['Location'].str.rstrip('- ').str.strip('?')


    df['Operator'] = df['Operator'].str.strip('?')



    df.dropna(inplace = True)


    survival_rate = df["Aboard"] - df["Fatalities (air)"]

    df.loc[:, 'survival_rate'] = survival_rate
    
    


    




    return df


data = load_data()

#Display the data

st.title("Air Crashes Full Data 1908 -2024")




# add a filter

filters = {
    "Year": data["Year"].astype(int).unique(),
    "Month": data["Month"].unique(),
    "Country": data["Country/Region"].unique(),
    "Aircraft Manufacturer": data["Aircraft Manufacturer"].unique(),
    "Operator": data["Operator"].unique(),

}


selected_filters = {}


#generate multi-select widgets dynamically

for key, options in filters.items():
    selected_filters[key] = st.sidebar.multiselect(key,options)


# add a dynamic filter 

filtered_data = data 



for key, selected_values in selected_filters.items():
    if selected_values:
        filtered_data = filtered_data[filtered_data[key].isin(selected_values)]






# THE KPI'S 
sum_of_fatalities = filtered_data['Fatalities (air)'].sum()

sum_of_ground = filtered_data['Ground'].sum()

sum_of_abroad = filtered_data['Aboard'].sum()

num_survivors = filtered_data['survival_rate'].sum()

total_individuals = len('survival_rate')

percentage_of_survival = (num_survivors / total_individuals) * 100



col1, col2, col3, col4 = st.columns(4)

with col1: 
    st.metric(label="Sum of Fatalities", value=f"{sum_of_fatalities:.2f}", delta=None)

with col2:
    st.metric(label = "Sum of Ground", value =f"{sum_of_ground:.2f}", delta=None)

with col3:
    st.metric(label = "Sum of Abroad", value= f"{sum_of_abroad:.2f}", delta=None)

with col4:
    st.metric(label = "survival percentage", value = f"%{percentage_of_survival:.2f}")



st.write(filtered_data)


# visualization & research questions

# Create a scatter plot chart of the Year against Fatalities 

Year = filtered_data.groupby(['Year'])['Fatalities (air)'].sum().reset_index()

top_Year = Year.sort_values(by = 'Fatalities (air)', ascending =False)

Year_plt = px.scatter(Year, x='Year', y='Fatalities (air)', title='Sum of Fatalities Vs. Year')

Year_plt.update_layout(xaxis_title='Year', yaxis_title='Fatalities')

st.plotly_chart(Year_plt)


# create a combined chart for Months and Quarters against Fatalities to show the trend of death over the month

Datax = filtered_data.groupby(['Month', 'Quarter'])['Fatalities (air)'].sum().reset_index()

data_sort = Datax.sort_values(by = 'Fatalities (air)', ascending =False)

# Create a stacked area chart
fig = px.area(data_sort, x='Month', y='Fatalities (air)', color='Quarter', title='Monthly and Quarterly Fatalities')

fig.update_layout(xaxis_title='Month', yaxis_title='Fatalities')

st.plotly_chart(fig)


# Which countries have experienced the highest number of aircraft crashes?


Countries = filtered_data.groupby (['Country/Region'])['Fatalities (air)'].sum().reset_index()

countries_sort = Countries.sort_values(by = 'Fatalities (air)', ascending =False)



fig = px.choropleth(countries_sort, locations = "Country/Region", 
                   locationmode = "country names", color = "Fatalities (air)", color_continuous_scale = "Viridis",
                   title = "Aircraft crashes by Country")


st.plotly_chart(fig)


# Which aircraft manufacturers have the highest incidence of crashes?

Aircraft = filtered_data.groupby(['Aircraft Manufacturer'])['Fatalities (air)'].sum().reset_index()

Aircraft_sort = Aircraft.sort_values(by = 'Fatalities (air)', ascending =False)


Aircraft_10 = Aircraft_sort.head(10)

barchart = px.bar(Aircraft_10, x = "Aircraft Manufacturer", y = "Fatalities (air)")

barchart.update_layout(xaxis_title='Aircraft Manufacturer', yaxis_title='Fatalities', title = 'Aircraft Manufactures Vs. Fatalities' )

st.plotly_chart(barchart)


# Which aircraft manufacturers have the highest survival rate?

Aircraft_survival = filtered_data.groupby(['Aircraft Manufacturer'])['survival_rate'].sum().reset_index()

Aircraft_sort = Aircraft_survival.sort_values(by = 'survival_rate', ascending =False)

Aircraft_sort_5 = Aircraft_sort.head(5)


pie_chart = px.pie(Aircraft_sort_5, values ='survival_rate', names = 'Aircraft Manufacturer', title = 'Aircraft Manufactures Vs. Survival Rate')

st.plotly_chart(pie_chart)


#Does the aircraft size (total aboard) correlate with survival rates or total fatalities?


size_aircraft = filtered_data.groupby(['Fatalities (air)','survival_rate'])['Aboard'].sum().reset_index()

size_aircraft_sort = size_aircraft.sort_values(by = 'Aboard', ascending =False)

fig = px.area(size_aircraft_sort, x='Aboard', y=['Fatalities (air)', 'survival_rate'], 
              title='Correlation of Sum of Abord Vs. survival rates and total fatalities ') 

st.plotly_chart(fig)