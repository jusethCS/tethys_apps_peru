from tethys_sdk.base import TethysAppBase


class HydroviewerPeru(TethysAppBase):
    """
    Tethys app class for Hydroviewer Peru.
    """

    name = 'Hydroviewer Peru'
    description = ''
    package = 'hydroviewer_peru'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hydroviewer-peru'
    color = '#286090'
    tags = ''
    enable_feedback = False
    feedback_emails = []