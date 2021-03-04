'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('./assets/data/arbres.csv')

def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe['Date_Plantation']= pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    filter_date = (dataframe['Date_Plantation'] > pd.to_datetime(start,format='%Y')) & (dataframe['Date_Plantation'] <= pd.to_datetime(end + 1,format='%Y'))
    dataframe = dataframe.loc[filter_date]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    dataframe["Count"] = 1
    dataframe["Date_year"] = dataframe['Date_Plantation'].dt.year
    dataframe = dataframe.groupby(["Arrond_Nom", "Date_year"])["Count"].count().reset_index(name="Counts")
    return dataframe


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    # yearly_df['Date_Plantation'] = pd.to_datetime(yearly_df['Date_Plantation']*1000 + 365, format = "%Y%j")
    yearly_df = yearly_df.pivot(index ='Arrond_Nom', columns ='Date_year', values='Counts') 
    yearly_df = yearly_df.fillna(0)
    return yearly_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    date_start = datetime.datetime.strptime( (str(year) +'0101'), '%Y%m%d')
    date_end = datetime.datetime.strptime((str(year) + '1231'), '%Y%m%d') 
    dataframe["Count"] = 1
    dataframe = dataframe.loc[(dataframe['Arrond_Nom'] == arrond) & (dataframe['Date_Plantation'] > date_start)  & (dataframe['Date_Plantation'] <= date_end)]
    dataframe = dataframe.groupby(["Date_Plantation"])["Count"].count().reset_index(name="Counts")
    print(dataframe)
    return dataframe