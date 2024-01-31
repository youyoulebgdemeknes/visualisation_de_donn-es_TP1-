'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''

    
    player_name_html = f'<span style="font-family: Grenze Gotish; font-size: 24px; color: black;">{name}</span>'
    
    if mode == 'count':
        hover_text = f"{player_name_html}<br><br><i>%{{y}} lignes</i><extra></extra>"
    elif mode == 'percent':
        hover_text = f"{player_name_html}<br><br><i>%{{y:.2f}}% des lignes</i><extra></extra>"
    else:
        raise ValueError("Mode must be 'count' or 'percent'")

    return hover_text