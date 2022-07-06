import pandas as pd
import geopandas as gpd
from typing import NamedTuple, Optional
import joblib as jb
import pickle

df_ibague = pd.read_csv('./data/dftrees/Datos_Ibague_limpios.csv',dtype={'latitude':float,'longitude':float},low_memory=False)

df_comunas = gpd.read_file('./data/dftrees/COMUNAS.geojson')

def load_random_forest_model():
    #model = open("./data/model/model.pkl", 'rb')
    #pickled_model = pickle.load(open('./data/model/finalized_model_pickle.pkl', 'rb'))
    with open('./data/model/finalized_model_pickle.pkl', 'rb') as f:
       rf = pickle.load(f)
    #rf=jb.load(model)
    return rf

loaded_model = load_random_forest_model()

#df1=df_ibague[df_ibague['comuna']==1]
#for i in range(len(df1)):
#    print(df1['latitude'].iloc[i],df1['longitude'].iloc[i])

#print(len(df1))

class Contact(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None