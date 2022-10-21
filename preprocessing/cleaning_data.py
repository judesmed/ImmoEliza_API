import pandas as pd
from numpy import NaN


class Cleaning():

    def __init__(self) -> None:
            pass
    # def __init__(self):
    #     self.json_file = '/home/juliendesmedt/Documents/becode/immo_web_project/ImmoEliza_API/test_app.json'

 
    def input_check(self, json_file):
        #SELECT THE FILE
        df = pd.DataFrame([json_file.values()],columns=json_file.keys() )
        #df = pd.DataFrame([json_file.values()],columns=json_file.keys() )

    #DROP NAN AND USELESS VALUES

        name_API = {'area': 'surface',\
            'building_state':'state_of_the_building',\
            'equipped_kitchen':'fully_equipped_kitchen',\
            'facades_number': 'number_of_facades',\
            'furnished': 'furnished',\
            'garden_area': 'garden_surface',\
            'land_area': 'land_surface',\
            'open_fire': 'open_fire',\
            'property_type': 'type_of_property',\
            'rooms_number':'number_of_bedrooms',\
            'swimming_pool': 'swimming_pool',\
            'terrace_area': 'terrace_surface',\
            'zip_code':'postal_code' }
            
        df = df.rename(columns= name_API)
        status_code ='200'
        if df[['surface','type_of_property','number_of_bedrooms','postal_code']].isna().any().sum() != 0:
            status_code = 'error_missing_required_values'
        # if df[['type_of_property']]=='OTHERS':
        #     status_code = 'error_property-type'

        #REPLACE NAN BY 0
        df["swimming_pool"] = df["swimming_pool"].replace(NaN, 0).astype(int)
        df["garden"] = df["garden"].replace(NaN, 0).astype(int)
        df["terrace"] = df["terrace"].replace(NaN, 0).astype(int)
        self.df = df
        self.status_code = status_code


    def preprocess(self, json_file):
        
        self.input_check(json_file)
        df = self.df

        #TRANSLATE CATEGORIES IN NUM VALUES
            #Property_type
        map_property = {"HOUSE":1, "APARTMENT":0}
        df["type_of_property"] = df["type_of_property"].map(map_property).astype(int)

            #State_of_building
        map_state = {"GOOD":1, "TO RENOVATE":0, "NEW":1, "JUST RENOVATED":1, "TO REBUILD":0}
        df["state_of_the_building"] = df["state_of_the_building"].map(map_state).astype(int)

        zip_code_score = pd.read_csv('model/zip_code_score.csv')
        df_cp = zip_code_score
        df = df.merge(df_cp, how='left', on='postal_code')


        #DROP FEATURES
        del df["postal_code"]
        del df["full_address"]
        del df["fully_equipped_kitchen"]
        del df["land_surface"]
        del df["number_of_facades"]
        del df["garden_surface"]
        del df["terrace_surface"]
        del df["furnished"]
        del df["open_fire"]

        df = df[['type_of_property',\
                'number_of_bedrooms',\
                'surface',\
                'terrace',\
                'garden',\
                'swimming_pool',\
                'state_of_the_building',\
                'postal_code_score']]

        self.df = df
        return self