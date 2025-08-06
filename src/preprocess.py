import pandas as pd 
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    data = df.copy()

    data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], dayfirst=True)

    data = data.dropna(subset='Income')

    data['TotalChildren'] = data['Kidhome'] + data['Teenhome']
    data['Age'] = 2025 - data['Year_Birth']
    data['TotalSpent'] = data[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)
    data['Customer_Tenure'] =(pd.to_datetime('2025-01-01') - data['Dt_Customer']).dt.days

    return data

def remove_outliers_iqr(dataframe, features):
    df_out = dataframe.copy()
    for col in features:
        Q1 = df_out[col].quantile(0.25)
        Q3 = df_out[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_out = df_out[(df_out[col] >= lower_bound) & (df_out[col] <= upper_bound)]
    return df_out


def scale_features(dataframe, features):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(dataframe[features])
    return X_scaled, scaler

