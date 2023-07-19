import streamlit as st
import plotly.express as px
from services import get_data


st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


d,t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (Celsius)"})
st.plotly_chart(figure)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

