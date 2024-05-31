import pandas as pd 
class Cleaner:

    def clean_df(self,df):
     df.drop(['Actual Arrival Date/Time', 'Actual Offload Date'], inplace=True, axis=1)
     date_cols=df.columns[df.columns.str.contains("Date")]
     date_obj=df[date_cols].select_dtypes('object').columns
     for c in date_obj:
        df[c]=pd.to_datetime(df[c], errors='coerce')
     
     return df
    
    
    def get_district_code(self, x):
     if len(x.split('-'))>1:
        t=x.split('-')[-1]
        return t[:4]
     return 0

    def get_district_name(self,x):
     if len(x.split('/'))>1:
        return x.split('/')[-1]
     elif len(x.split(' ',1))>1:
        return x.split(' ',1)[1]
     
    def prep(self,df):
      df['leadtime in days']=df['End Date']-df['Start Date']
      df['District_Name']=df['Delivery Address Street'].apply(self.get_district_name)
      df['District_Code']=df['Delivery Address Name'].apply(self.get_district_code)
      date_cols=df.columns[df.columns.str.contains("Date")]
      for c in date_cols:
         df[c]=df[c].dt.strftime('%d-%m-%Y')
      return df
