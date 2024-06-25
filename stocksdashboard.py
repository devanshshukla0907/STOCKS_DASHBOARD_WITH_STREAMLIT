import streamlit as st, pandas as pd,numpy as np,yfinance as yf
import plotly.express as px

stock_dashboard,technical_analysis=st.tabs(["STOCK DASHBOARD","TECHNICAL ANALYSIS"])
with stock_dashboard:
    st.title("STOCK DASHBOARD")
    ticker= st.sidebar.text_input('Ticker')
    ticker1=ticker.upper()
    start_date=st.sidebar.date_input("Start Date")
    end_date=st.sidebar.date_input("End Date")

    data=yf.download(ticker1,start=start_date,end=end_date)
    fig=px.line(data,x=data.index,y=data["Adj Close"],title=ticker)
    st.plotly_chart(fig)


    pricing_data,fundamental_data,news= st.tabs(["PRICING DATA","FUNDAMENTAL DATA","TOP NEWS"])

with pricing_data:
    st.header("PRICE")
    data2=data
    data2['Returns']= log_returns = np.log(data['Adj Close'] / data['Adj Close'].shift(1)).dropna()
    data2.dropna(inplace=True)
    st.write(data2)
    r=data2['Returns'].mean()*252
    annual_return=(np.exp(r) - 1) * 100
    st.write("Annual Return is",annual_return,'%')
    st.write("Standard Deviation is",data2['Returns'].std()*np.sqrt(252)*100)
    st.write("Risk Adj Return is",annual_return/(data2['Returns'].std()*np.sqrt(252)*100))




from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    st.header("FUNDAMENTALS")
    key='H3REPC7MVBPX1P6O'
    fd=FundamentalData(key,output_format='pandas')
    st.subheader("Balance Sheet")
    balance_sheet=fd.get_balance_sheet_annual(ticker)[0]
    bs=balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)
    
    
from stocknews import StockNews
with news:
    st.header(f'Trending in {ticker}')
    sn = StockNews(ticker , save_news=False)
    df_news =sn.read_rss()
    for i in range(10):
        st.subheader(df_news['title'][i])
        st.write(df_news['published'][i])
        
        st.write(df_news['summary' ][i])
        
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
    
import pandas_ta as ta

with technical_analysis:
    st.title("TECHNICAL ANALYSIS")
    data=yf.download(ticker1,start=start_date,end=end_date)
    df=pd.DataFrame()
    ind_list=df.ta.indicators(as_list=True)
    #st.write(ind_list)
    technical_indicator=st.selectbox("Indicator",options=ind_list)
    method=technical_indicator
    indicator=pd.DataFrame(getattr(ta,method)(low=data["Low"],close=data['Close'],high=data["High"],open=data['Open'],volume=data["Volume"]))
    indicator['Close']=data['Close']
    
    figw_ind_new=px.line(indicator)
    st.plotly_chart(figw_ind_new)
    st.write(indicator)