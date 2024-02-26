import numpy as np
import pandas as pd

videogames_df = pd.read_csv("Video_Game_Sales.csv")

# videogames_df.info()
print(videogames_df['Platform'].unique())
# ['Wii' 'NES' 'G' 'DS' 'X360' 'PS3' 'PS2' 'SNES' 'GBA' '3DS' 'PS4' 'N64'
# 'PS' 'X' 'PC' '2600' 'PSP' 'XOne' 'WiiU' 'GC' 'GEN' 'DC' 'PSV' 'SAT'
# 'SCD' 'WS' 'NG' 'TG16' '3DO' 'GG' 'PCFX']
print(len(videogames_df['Publisher'].unique()))
# There are 628 different publishers
print(videogames_df['Publisher'].value_counts())
# Top 5
# Electronic Arts                 1380
# Activision                      1005
# Namco Bandai Games               972
# Ubisoft                          970
# Konami Digital Entertainment     865

# Limiting the dataframe to only those that have critic scores, critic counts, user scores, user counts, and ratings 
# for more accurate statistical results
df_cleaned = videogames_df.dropna(subset=['Critic_Score', 'Critic_Count','User_Score','User_Count','Rating'], how='all').head(1000)
# Limiting the cleaned dataframe to only 1000
print(df_cleaned.info()) 
# Counting the different data types in the dataframe
print(df_cleaned.dtypes.value_counts())
# Checking for NaN values
print(df_cleaned.isnull().any())
nan_variables = df_cleaned.columns[df_cleaned.isnull().any()].tolist()
print(nan_variables)
print(df_cleaned[nan_variables].isnull().sum())
print(df_cleaned.shape)
exclude_variables = ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Rating']
dropped_variables = list(set(nan_variables) - set(exclude_variables))
df_cleaned = df_cleaned.dropna(subset=dropped_variables)
df_cleaned.info()
