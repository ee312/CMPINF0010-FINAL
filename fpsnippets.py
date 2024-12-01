import geopandas
import pandas as pd

# Load tracts
TRACTS = pd.read_csv("https://data.wprdc.org/dataset/pittsburgh-2014-cdbg-census-tracts/resource/116d28e7-fbdb-4c58-a845-6e2c00a4fde0/download/116d28e7-fbdb-4c58-a845-6e2c00a4fde0.csv")

def zip_to_neighborhoods(zip_code):
    tracts = pd.read_csv("./ZIP_TRACT_032020.csv")
    filt_tracts = tracts[tracts["ZIP"] == zip_code]
    hoods = []
    for index, row in filt_tracts.iterrows():
        hood = tract_to_neighborhoods(int(row["TRACT"]))
        for ho in hood: 
            if ho not in hoods: 
                hoods.append(ho)
    return hoods

def tract_to_neighborhoods(tract): 
    hoods = []
    for index, row in TRACTS.iterrows():
        st = str(row["geoid10"])
        if st.startswith(str(tract)): 
            hoods.append(row["hood"])

    return hoods