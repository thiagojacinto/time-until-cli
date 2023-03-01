from datetime import datetime
from dateutil.relativedelta import relativedelta

class DateBuilder:
    """Builder to generate a Date entity"""

    def __init__(self):
        """Initialise with datetime object of current time"""
        self._date = datetime.now()

    def with_years_ahead(self, years_from_now : int):
        """Set the the number of years from now"""
        self._date += relativedelta(years=years_from_now)
        return self

    def with_months_ahead(self, months_from_now : int):
        """Set the the number of months from now"""
        self._date += relativedelta(months=months_from_now)
        return self

    def with_days_ahead(self, days_from_now : int):
        """Set the the number of days from now"""
        self._date += relativedelta(days=days_from_now)
        return self

    def with_hours_ahead(self, hours_from_now : int):
        """Set the the number of hours from now"""
        self._date += relativedelta(hours=hours_from_now)
        return self

    def with_minutes_ahead(self, minutes_from_now : int):
        """Set the the number of minutes from now"""
        self._date += relativedelta(minutes=minutes_from_now)
        return self

    def with_seconds_ahead(self, seconds_from_now : int):
        """Set the the number of seconds from now"""
        self._date += relativedelta(seconds=seconds_from_now)
        return self

    def build(self):
        """Return the curret datetime entity"""
        return self._date