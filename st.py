import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas_datareader as data1
from datetime import date
from keras.models import load_model
import numpy as np
from prophet import Prophet
from prophet.plot import plot_plotly
from datetime import date
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor



st.title('Stock Price Predictions')
st.sidebar.info('Welcome to the Stock Price Prediction App. Choose your options below')
#st.sidebar.info("Created and designed by [Rushi](https://www.linkedin.com/in/jonathan-ben-okah-7b507725b)")

def main():
    option = st.sidebar.selectbox('Make a choice', ['Visualize','Prediction', 'Analysis'])
    if option == 'Visualize':
        tech_indicators()
    elif option == 'Prediction':
        predict()
    else:
        dataframe()



@st.cache_resource
def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df


stock= ('AAPL','GOOG','ICICIPRULI.BO','LICI.NS','SBI','PAYTM.NS','ZOMATO.NS','NESTLEIND.BO')
option = st.sidebar.selectbox("selected stock",stock)
option = option.upper()
today = datetime.date.today()
#duration = st.sidebar.number_input('Enter the duration',)
before = today - datetime.timedelta(days=3000)
start_date = st.sidebar.date_input('Start Date', value=before)
end_date = st.sidebar.date_input('End date', today)
if st.sidebar.button('Send'):
    if start_date < end_date:
        st.sidebar.success('Start date: `%s`\n\nEnd date: `%s`' %(start_date, end_date))
        download_data(option, start_date, end_date)
    else:
        st.sidebar.error('Error: End date must fall after start date')




#data = download_data(option, start_date, end_date)
scaler = StandardScaler()
df = yf.download(option, start_date, end_date)
    # describing data

    # maps

fig = plt.figure(figsize=(10, 5))
plt.plot(df.Close, color='yellow')
plt.legend()

ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(10, 5))
plt.plot(ma100, color='red')
plt.plot(df.Close, color='yellow')
plt.legend()
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(10, 5))
plt.plot(ma100, color='red')
plt.plot(ma200, color='green')
plt.plot(df.Close, color='yellow')
plt.legend()
###############predict#############################
data_training = pd.DataFrame(df['Close'][0:int(len(df) * 0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df) * 0.70):int(len(df))])
print(' taining ', data_training.shape)
print(' testing ', data_testing.shape)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
data_training_array = scaler.fit_transform(data_training)
# load Model
model = load_model('model.h5')
# testing past
pass_100_days = data_training.tail(100)
final_df = pd.concat([pass_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)
x_test = []
y_test = []
for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i - 100:i])
    y_test.append(input_data[i, 0])
x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)
scaler = scaler.scale_
scale_factor = 1 / scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor
@st.cache_data
def load_data(ticker):
    data1 = yf.download(ticker, start_date, end_date)
    data1.reset_index(inplace=True)
    return data1


data_load_state = st.text('Loading data...')
data = load_data(option)
data_load_state.text('Loading data... done!')
# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
m = Prophet()
m.fit(df_train)





def tech_indicators():
    st.subheader('Stock Data')
    st.write(df.describe())
    # maps
    st.subheader('closing Price VS Time Chart ')
    st.pyplot(fig)
    st.subheader('closing Price VS Time Chart with 100 moving Average  ')
    st.pyplot(fig)
    st.subheader('closing Price VS Time Chart with 100 & 200 moving Average  ')
    st.pyplot(fig)




def predict():
    n_years = st.slider('Years of prediction:', 1, 4)
    period = n_years * 365
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)
    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)




def dataframe():
    st.subheader('prediction vs Original')
    fig2 = plt.figure(figsize=(12, 6))
    plt.plot(y_test, 'b', label='Original Price')
    plt.plot(y_predicted, 'r', label='prdicted Price')
    plt.style.use('dark_background')
    plt.xlabel('time')
    plt.ylabel('price')
    plt.legend()
    st.pyplot(fig2)



#def model_engine(model, num):


if __name__ == '__main__':
    main()
