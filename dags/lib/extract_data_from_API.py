# import necessary packages
import requests
import json
import datetime
import pandas as pd

# define functions
def get_bar_data_from_api():
    '''
    Description: This function helps users to extract bar json data from Melbourne Government API,
                 make data in a format users want, and save data in a CSV file format in local system
    Parameters: None
    Returns: None
    '''
    # extract date from Melbourne government API
    r = requests.get('https://data.melbourne.vic.gov.au/resource/mffi-m9yn.json')

    if r.status_code == requests.codes.ok:
        # extract data from HTTP response and put data in a dataframe
        rawdata_str = r.text
        rawdata_dict = json.loads(rawdata_str)
        rawdata_df = pd.DataFrame(rawdata_dict)
        rawdata_df = rawdata_df.reset_index()
        rawdata_df['row_index'] = rawdata_df['index'].apply(lambda x: datetime.datetime.now().strftime('%Y%m%d') + '_bar_row_' + str(x))
    
        # get necessary columns
        result_df = rawdata_df[['row_index', 'trading_name', 'census_year', 'street_address', \
                                'clue_small_area', 'number_of_patrons', 'y_coordinate', 'x_coordinate']]
        result_df.columns = ['row_index', 'trading_name', 'census_year', 'street_address', \
                             'clue_small_area', 'number_of_patrons', 'latitude', 'longitude']
        
        # drop duplicated data
        result_df = result_df.drop_duplicates(subset='trading_name', keep='first')      
        
        # replace null value 
        result_df['trading_name'] = result_df['trading_name'].fillna('no_data')
        result_df['census_year'] = result_df['census_year'].fillna('0')
        result_df['street_address'] = result_df['street_address'].fillna('no_data')
        result_df['clue_small_area'] = result_df['clue_small_area'].fillna('no_data')
        result_df['number_of_patrons'] = result_df['number_of_patrons'].fillna('0')
        result_df['latitude'] = result_df['latitude'].fillna('0')
        result_df['longitude'] = result_df['longitude'].fillna('0')
                
        # save result into a csv file
        csv_created_time = datetime.datetime.now().strftime('%Y%m%d')
        result_df.to_csv('bar_' + csv_created_time + '.csv' ,header=False, index=False)
        print('Data bar_' + csv_created_time + '.csv already saved.')

	# return the file name to airflow context
	return 'bar_' + csv_created_time + '.csv'
        
def get_streetlight_data_from_api():
    '''
    Description: This function helps users to extract streetlight json data from Melbourne Government API,
                 make data in a format users want, and save data in a CSV file format in local system
    Parameters: None
    Returns: None
    '''
    # extract date from Melbourne government API
    r = requests.get('https://data.melbourne.vic.gov.au/resource/4j42-79hg.json')

    if r.status_code == requests.codes.ok:
        # extract data from HTTP response and put data in a dataframe
        rawdata_str = r.text
        rawdata_dict = json.loads(rawdata_str)
        rawdata_df = pd.DataFrame(rawdata_dict)
        rawdata_df = rawdata_df.reset_index()
        rawdata_df['row_index'] = rawdata_df['index'].apply(lambda x: datetime.datetime.now().strftime('%Y%m%d') + '_streetlight_row_' + str(x))
    
        # get necessary columns
        result_df = rawdata_df[['row_index', 'asset_number', 'asset_description', 'lamp_type_lupvalue', \
                                'lamp_rating_w', 'mounting_type_lupvalue', 'lat', 'lon']]
        result_df.columns = ['row_index', 'asset_number', 'asset_description', 'lamp_type_lupvalue', \
                             'lamp_rating_w', 'mounting_type_lupvalue', 'latitude', 'longitude']
        
        # drop duplicated rows
        result_df = result_df.drop_duplicates(subset='asset_number', keep='first')
        
        # replace null value
        result_df['asset_number'] = result_df['asset_number'].fillna('0')
        result_df['asset_description'] = result_df['asset_description'].fillna('no_data')
        result_df['lamp_type_lupvalue'] = result_df['lamp_type_lupvalue'].fillna('0')
        result_df['lamp_rating_w'] = result_df['lamp_rating_w'].fillna('0')
        result_df['mounting_type_lupvalue'] = result_df['mounting_type_lupvalue'].fillna('no_data')
        result_df['latitude'] = result_df['latitude'].fillna('0')
        result_df['longitude'] = result_df['longitude'].fillna('0')
        
        # save result into a csv file
        csv_created_time = datetime.datetime.now().strftime('%Y%m%d')
        result_df.to_csv('streetlight_' + csv_created_time + '.csv' ,header=False, index=False)
        print('Data streetlight_' + csv_created_time + '.csv already saved.')
    
	# return the file name to airflow context
        return 'streetlight_' + csv_created_time + '.csv'

    else:
        print('some errors occur when getting streetlight data, please check your code')        

def get_restaurant_data_from_api():
    '''
    Description: This function helps users to extract restaurant json data from Melbourne Government API,
                 make data in a format users want, and save data in a CSV file format in local system
    Parameters: None
    Returns: None
    '''
    # extract date from Melbourne government API
    r = requests.get('https://data.melbourne.vic.gov.au/resource/xt2y-tnn9.json')

    if r.status_code == requests.codes.ok:
        # extract data from HTTP response and put data in a dataframe
        rawdata_str = r.text
        rawdata_dict = json.loads(rawdata_str)
        rawdata_df = pd.DataFrame(rawdata_dict)
        rawdata_df = rawdata_df.reset_index()
        rawdata_df['row_index'] = rawdata_df['index'].apply(lambda x: datetime.datetime.now().strftime('%Y%m%d') + '_restaurant_row_' + str(x))
    
        # get necessary columns
        result_df = rawdata_df[['row_index', 'trading_name', 'census_year', 'street_address', \
                                'clue_small_area', 'number_of_seats', 'y_coordinate', 'x_coordinate']]
        result_df.columns = ['row_index', 'trading_name', 'census_year', 'street_address', \
                             'clue_small_area', 'number_of_seats', 'latitude', 'longitude']
        
        # drop duplicated rows
        result_df = result_df.drop_duplicates(subset='trading_name', keep='first')
        
        # replace null value
        result_df['trading_name'] = result_df['trading_name'].fillna('no_data')
        result_df['census_year'] = result_df['census_year'].fillna('0')
        result_df['street_address'] = result_df['street_address'].fillna('no_data')
        result_df['clue_small_area'] = result_df['clue_small_area'].fillna('no_data')
        result_df['number_of_seats'] = result_df['number_of_seats'].fillna('0')
        result_df['latitude'] = result_df['latitude'].fillna('0')
        result_df['longitude'] = result_df['longitude'].fillna('0')
        
        # save result into a csv file
        csv_created_time = datetime.datetime.now().strftime('%Y%m%d')
        result_df.to_csv('restaurant_' + csv_created_time + '.csv' ,header=False, index=False)
        print('Data restaurant_' + csv_created_time + '.csv already saved.')
    
	# return the file name to airflow context
        return 'restaurant_' + csv_created_time + '.csv'

    else:
        print('some errors occur when getting restaurant data, please check your code')

def get_construction_data_from_api():
    '''
    Description: This function helps users to extract construction json data from Melbourne Government
                 API, make data in a format users want, and save data in a CSV file format in local
                 system
    Parameters: None
    Returns: None
    '''
    # extract date from Melbourne government API
    r = requests.get('https://data.melbourne.vic.gov.au/resource/gh7s-qda8.json')

    if r.status_code == requests.codes.ok:
        # extract data from HTTP response and put data in a dataframe
        rawdata_str = r.text
        rawdata_dict = json.loads(rawdata_str)
        rawdata_df = pd.DataFrame(rawdata_dict)
        rawdata_df = rawdata_df.reset_index()
        rawdata_df['row_index'] = rawdata_df['index'].apply(lambda x: datetime.datetime.now().strftime('%Y%m%d') + '_construction_row_' + str(x))
    
        # get necessary columns, drop duplicated rows
        result_df = rawdata_df[['row_index', 'development_key', 'status', 'clue_small_area', \
                                'street_address', 'floors_above', 'car_spaces', 'latitude', 'longitude']]
        result_df = result_df.drop_duplicates(subset='development_key', keep='first')

        # replace null value
        result_df['development_key'] = result_df['development_key'].fillna('no_data')
        result_df['status'] = result_df['status'].fillna('no_data')
        result_df['clue_small_area'] = result_df['clue_small_area'].fillna('no_data')
        result_df['street_address'] = result_df['street_address'].fillna('no_data')
        result_df['floors_above'] = result_df['floors_above'].fillna('0')
        result_df['car_spaces'] = result_df['car_spaces'].fillna('0')               
        result_df['latitude'] = result_df['latitude'].fillna('0')
        result_df['longitude'] = result_df['longitude'].fillna('0')
        
        # save result into a csv file
        csv_created_time = datetime.datetime.now().strftime('%Y%m%d')
        result_df.to_csv('construction_' + csv_created_time + '.csv' ,header=False, index=False)
        print('Data construction_' + csv_created_time + '.csv already saved.')
    
	# return the file name to airflow context
        return 'construction_' + csv_created_time + '.csv'

    else:
        print('some errors occur when getting construction data, please check your code')
		
def get_pedestrian_data_from_api():
    '''
    Description: This function helps users to extract pedestrian json data from Melbourne Government API,
                 make data in a format users want, and save data in a CSV file format in local system
    Parameters: None
    Returns: None
    '''
    # extract date from Melbourne government API
    r_sensor_location = requests.get('https://data.melbourne.vic.gov.au/resource/h57g-5234.json')
    r_sensor_data = requests.get('https://data.melbourne.vic.gov.au/resource/d6mv-s43h.json')

    if r_sensor_location.status_code == requests.codes.ok and r_sensor_data.status_code == requests.codes.ok:       
        # extract data from HTTP response and put data in a dataframe
        sensor_location_rawdata_str = r_sensor_location.text
        sensor_location_rawdata_dict = json.loads(sensor_location_rawdata_str)
        sensor_location_df = pd.DataFrame(sensor_location_rawdata_dict)        
        sensor_data_rawdata_str = r_sensor_data.text
        sensor_data_rawdata_dict = json.loads(sensor_data_rawdata_str)
        sensor_data_df = pd.DataFrame(sensor_data_rawdata_dict)
                
        # get necessary columns, drop duplicated rows, and combine two dataframes
        sensor_location_df_filterd = sensor_location_df[['sensor_id', 'sensor_name', 'sensor_description', \
                                                         'status', 'latitude', 'longitude']]
        sensor_location_df_filterd_dropduplicated = sensor_location_df_filterd.drop_duplicates(subset='sensor_id', keep='first')
        sensor_data_df_filterd = sensor_data_df[['sensor_id', 'date', 'time', 'total_of_directions']]
        sensor_data_df_filterd_dropduplicated = sensor_data_df_filterd.drop_duplicates(subset='sensor_id', keep='first')
        result_df = pd.merge(sensor_location_df_filterd_dropduplicated, \
                             sensor_data_df_filterd_dropduplicated, on=['sensor_id', 'sensor_id'], how='inner')
        
        # create a row_index column and rearrange the column order in this dataframe
        result_df = result_df.reset_index()
        result_df['row_index'] = rawdata_df['index'].apply(lambda x: datetime.datetime.now().strftime('%Y%m%d') + '_pedestrian_row_' + str(x))
        result_df = result_df.drop(columns='index')
        result_df = result_df[['row_index', 'sensor_id', 'sensor_name', 'sensor_description', 'status', \
                      'latitude', 'longitude', 'date', 'time', 'total_of_directions']]
        
        # replace null value
        result_df['sensor_id'] = result_df['sensor_id'].fillna('0')
        result_df['sensor_name'] = result_df['sensor_name'].fillna('no_data')
        result_df['sensor_description'] = result_df['sensor_description'].fillna('no_data')
        result_df['status'] = result_df['status'].fillna('no_data')
        result_df['latitude'] = result_df['latitude'].fillna('0')
        result_df['longitude'] = result_df['longitude'].fillna('0')               
        result_df['date'] = result_df['date'].fillna('no_data')
        result_df['time'] = result_df['time'].fillna('no_data')
        result_df['total_of_directions'] = result_df['total_of_directions'].fillna('0')
        
        # save result into a csv file
        csv_created_time = datetime.datetime.now().strftime('%Y%m%d')
        result_df.to_csv('pedestrian_' + csv_created_time + '.csv' ,header=False, index=False)
        print('Data pedestrian_' + csv_created_time + '.csv already saved.')

    	# return the file name to airflow context
	return 'construction_' + csv_created_time + '.csv'

    else:
        print('some errors occur when getting pedestrain data, please check your code')
