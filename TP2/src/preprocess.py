'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN

df = pd.read_csv('./assets/data/romeo_and_juliet.csv')

def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    df = my_df.groupby(["Act","Player"])["Line"].count().reset_index(name="PlayerLine")
    acts = df['Act'].unique()
    differentActs = []
    for act in acts:
        temp = df[df['Act'] == act]
        temp['PlayerPercent'] = temp["PlayerLine"] / temp["PlayerLine"].sum() * 100
        differentActs.append(temp)
    df = pd.concat(differentActs)
    return df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    top5 = my_df.groupby('Player')['Player','PlayerLine'].sum().nlargest(5, ['PlayerLine'])
    top5_df = my_df[my_df['Player'].isin(top5.index)]
    others_df = my_df[~my_df['Player'].isin(top5.index)]
    differentActs = []
    acts = others_df['Act'].unique()
    for act in acts:
        df_top5 = top5_df[top5_df['Act'] == act]
        temp = others_df[others_df['Act'] == act]
        tempPlayerLine = temp['PlayerLine'].sum()
        tempPlayerPercent = temp['PlayerPercent'].sum()
        tempDF = {'Act': [act], 'Player': ['OTHER'],'PlayerLine': [tempPlayerLine], 'PlayerPercent': [tempPlayerPercent]}
        df_others = pd.DataFrame(data=tempDF)
        df = pd.concat([df_top5,df_others]).sort_values('Player')
        differentActs.append(df)
    df = pd.concat(differentActs).reset_index(drop=True)
    return df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    my_df["Player"] = my_df["Player"].str.title()
    return my_df
