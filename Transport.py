from cleaners import Cleaner
import pandas as pd 

df=pd.read_excel("26_May_2024 _Daily.xlsx", sheet_name="67")
# print(df.info())

cln=Cleaner()

df_1=cln.clean_df(df)

df_1[df_1.columns[df_1.columns.str.contains("Date")]].info()

df_2=cln.prep(df_1)
print(df_2.columns[-3:])

