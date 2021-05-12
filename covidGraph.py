import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/Puranjay/OneDrive/Desktop/c103/covid.csv")
fig = px.scatter(df, x="date", y="cases",size="size" ,color="country",size_max=10)
fig.show()