"""
    DS 5110 Final Project
    Takes all the csv files for all the trip data from BlueBikes
    Combines into pandas dataframes by trip year
    Outputs these dataframes to csvs
"""

import os
import pandas as pd


def create_year_df(year, filelocation):
    """
    Creates a dataframe for a certain year. Combines all input csvs in filelocation into one df.
    :param filelocation: location of all input bluebikes data csvs (str)
    :param year: year to search for (str)
    :return: df_temp, a pandas dataframe
    """

    year_df = []
    # add all file names with year in them to list
    for each in os.listdir(filelocation):
        if year in each:
            # add name to list
            year_df.append(pd.read_csv((filelocation + str(each))))
    # concat all into one dataframe
    df_temp = pd.concat(year_df, axis=0, ignore_index=True)
    # drop columns as needed - birth year and gender, and then postal code (from different data sets)
    try:
        df_temp.drop(['birth year', 'gender'], axis=1, inplace=True)
    except KeyError:
        pass
    try:
        df_temp.drop(['postal code'], axis=1, inplace=True)
    except KeyError:
        pass
    
    # sort by date
    df_temp.sort_values('starttime', inplace=True)
    
    return df_temp


def main():

    # update file location to where all Bluebikes csv data is located and where to export outputs
    filelocation = '/Users/zacharyarmand/Documents/DS5110/Project/Data/bluebike_trips/Source data/'
    outputlocation = '/Users/zacharyarmand/Documents/DS5110/Project/Data/bluebike_trips/'

    # years of data to parse for
    years_of_data = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    # create a csv file for each yar
    for each in years_of_data:
        filename = 'bluebike_trips' + each + '.csv'
        # output to csv
        full_path = outputlocation + filename
        create_year_df(each, filelocation).to_csv(full_path, index=False)


if __name__ == '__main__':
    main()
