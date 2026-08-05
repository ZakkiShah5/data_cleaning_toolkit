import pandas as pd

def clean_text(series):
    """
    Cleans a text Series: strips whitespace, converts to title case,
    fills missing values with 'Unknown'.
    
    Args:
        series (pd.Series): text data to clean
    Returns:
        pd.Series: cleaned text
    """
    return series.str.strip().str.title().fillna("Unknown")

def clean_email(series):
    """
    Cleans an email Series: strips whitespace, converts to lowercase,
    fills missing values with 'Unknown'.
    
    Args:
        series (pd.Series): email data to clean
    Returns:
        pd.Series: cleaned emails
    """
    return series.str.strip().str.lower().fillna("Unknown")

def clean_date(series):
    """
    Cleans a date Series: converts to pandas datetime, takes in 3 date formats ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"),
    return NaT (Not a Time) for "invalid" date.
    
    Args:
        series (pd.Series): date data to clean
    Returns:
        pd.Series: cleaned date
    """
    def parse_single(date_str):
        formats = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"]
        for fmts in formats:
            try:
                return pd.to_datetime(date_str, format=fmts)
            except (ValueError, TypeError):
                continue
        return pd.NaT
    return series.apply(parse_single)

def clean_currency(series):
    """
        Cleans an currency Series: removes currency sign (e.g, $ etc.), converts to numeric value,
        fills "invalid" with NaN.
        
        Args:
            series (pd.Series): currency data to clean
        Returns:
            pd.Series: cleaned amount
        """
    return pd.to_numeric(series.str.replace(r"[^\d.]","",regex=True), errors='coerce')
