from operator import truth
import boto3
import streamlit as st
import datetime
#Martinskod

AWS_REGION = "eu-west-1"
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
def get_entries_by_week(week):
    response = database.scan(
        FilterExpression=boto3.dynamodb.conditions.Attr('week').eq(week)
    )
    return response['Items']
def huvudsida():
    st.subheader('Se inlägg')

table = dynamodb.Table('Streamlit_Data')
allowed_weeks = [str(week) for week in range(41, 49) if week != 44]

vecka = st.selectbox("Välj vecka att visa", allowed_weeks)

items = get_entries_by_week(int(vecka))

if not items:
    st.info(f"Inga inlägg hittades för vecka {vecka}.")
else:
    for item in items:
        st.write(f"**Vecka:** {item['vecka']}")
        st.write(f"**Datum:** {item['date']}")
        st.write(f"**Titel:** {item['title']}")
        st.write(f"**Innehåll:** {item['textruta']}")
        st.write(f"**Humör:** {item['mood']}")
        st.write(f'**Tags:** {item['taggar']}')
        st.write(f"**Taggar:** {', '.join(item['tags'])}")
        st.write ('~~~~')






from pyarrow import dictionary
#min kod
def database (title, textruta, taggar, mood, date, vecka):
    date.put_item(
     dictionary = {
        "Week": vecka,
        "tags": taggar,
        "title": title,
        "textruta": textruta,
        "mood": mood,
        "datum": date,

     })
st.header('Zakkis bloggsida')
date = dynamodb.Table("inlägg")
today = datetime.datetime.today()
currentweek = today.isocalendar()[1]

st.write (f'Välkommen Zakk! dagens datum: {currentweek}, Ha en trevlig dag!')


st.subheader('Vänligen välj vecka nedan')
#vecka = st.selectbox    ('Veckoval',
       #                 ['Vecka 41',
  #                       'Vecka 42',
  #                       'Vecka 43',
  #                       'Vecka 44',
 #                        'Vecka 45',
 #                        'Vecka 46',
 #                        'Vecka 47',
#                         'Vecka 48',
#                         'Vecka 49'])
title = st.text_input ('Välj titel här')
textruta = st.text_area('')
st.subheader('Vänligen välj taggar här')
taggar = st.multiselect('Tagg alternativ',
                      ['#Koding',
                       '#Kundtjänst',
                       '#Felsökning',
                       "#Teamwork",
                       '#Enskillt',
                       '#Lugn',
                       '#Stressigt',
                       '#Nöjd',
                       '#Handledare'])
mood = st.selectbox('Välj humör', ['😄', '🙂', '😐', '😕', '😢'])
spara = st.button('Spara')
redi = st.button('Redigera')

if st.button('Spara'):
 if not title or not textruta:
  st.error('Titel och innehåll är obligatoriska')
else:
 database(title, textruta, mood, taggar, vecka, date)
 st.success('Inlägg sparat!')
