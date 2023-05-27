from tethys_sdk.base import TethysAppBase


class HistoricalValidationToolPeru(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool Peru.
    """

    name = 'Historical Validation Tool Peru'
    description = ''
    package = 'historical_validation_tool_peru'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'historical-validation-tool-peru'
    color = '#286090'
    tags = ''
    enable_feedback = False
    feedback_emails = []