'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


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
    # Calculez le total de lignes par acteur pour chaque acte
    line_counts = my_df.groupby(['Act', 'Player']).size().reset_index(name='LineCount')

    # Calculez le total de lignes par acte
    total_lines_per_act = my_df.groupby('Act').size()

    # Ajoutez une colonne pour le pourcentage de lignes par acteur pour chaque acte
    line_counts['PercentCount'] = line_counts.apply(
        lambda row: (row['LineCount'] / total_lines_per_act.loc[row['Act']]) * 100, axis=1)

    # Retournez le nouveau DataFrame avec seulement les colonnes souhaitées
    final = line_counts[['Act', 'Player', 'LineCount', 'PercentCount']]
    return final

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
    top5 = my_df.groupby('Player')['LineCount'].sum().nlargest(5).index
    def replace(row):
        if row['Player'] not in top5 :
            row['Player'] = 'OTHER'
        return row
    my_df = my_df.apply(replace, axis=1)
    my_df = my_df.groupby(['Act', 'Player']).agg({'LineCount': 'sum', 'PercentCount': 'sum'}).reset_index()
    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df['Player'] = my_df['Player'].str.title()
    print(my_df)
    return my_df
