'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    fig.update_layout(
        template=pio.templates['simple_white'],
        dragmode=False,
        title={
            'text': 'Lignes par acte',
            'x': 0,
            'xanchor': 'left',
        },
        barmode='stack',
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
        
    fig = go.Figure(fig)

    fig.data = []
    
    Players = data['Player'].unique()
    
    
    for player in Players :
        player_data = data[data['Player'] == player]
        my_hover_template = get_hover_template(player, mode)
        print(player_data[MODE_TO_COLUMN[mode.lower()]])
        player_data["Act"] = player_data["Act"].apply(lambda x : f'Act {x}')
        fig.add_trace(go.Bar(
            x=player_data["Act"],
            y=player_data[MODE_TO_COLUMN[mode.lower()]],
            name=player,
            hovertemplate = my_hover_template
        ))

    fig.update_layout(
        barmode='stack',
        xaxis=dict(
            title='Act',
            type='category'
        ),
        yaxis=dict(
            title='Lines (Count)' if mode == 'count' else 'Lines (Percent)'
        ),
        legend=dict(
            title='Player'
        ),
        template='custom_theme'
    )

    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    yaxis_title2 = 'Lines (Count)' if mode == 'count' else 'Lines (%)'
    fig.update_layout(
        yaxis_title= yaxis_title2
    )
    return fig