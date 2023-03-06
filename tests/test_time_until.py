import pytest
from typer.testing import CliRunner

from src.time_until import app
from tests.date_builder import DateBuilder

runner = CliRunner()

@pytest.fixture
def default_date_format():
    """Return the format of date: YYYY-MM-DD HH:MM:SS"""
    return "%Y-%m-%d %H:%M:%S"

def accepted_date_formats_list():
    """Return a list of accepted date formats"""
    accepted_formats_list = []
    accepted_formats_list.append("%Y-%m-%dT%H:%M:%S.%f%z")
    accepted_formats_list.append("%Y-%m-%d %H")
    accepted_formats_list.append("%Y-%m-%d %H:%M")
    accepted_formats_list.append("%Y-%m-%d-%H:%M:%S")
    accepted_formats_list.append("%Y-%m-%d")
    accepted_formats_list.append("%Y-%m")
    accepted_formats_list.append("%Y")
    accepted_formats_list.append("%c")
    accepted_formats_list.append("%x")
    accepted_formats_list.append("%A")
    accepted_formats_list.append("%A-%Y")
    accepted_formats_list.append("%Hh%Ss")
    accepted_formats_list.append("%Y-%m-%d %Hh")
    accepted_formats_list.append("%Y-%m-%d %Hh%Ss")
    accepted_formats_list.append("%Y-%m-%d %Hh%Mm")
    accepted_formats_list.append("%Y-%m-%d %Hh%Mm%Ss")
    
    return accepted_formats_list

def invalid_date_formats_list():
    """Return a list of invalid date formats"""
    invalid_formats_list = []
    invalid_formats_list.append("%j")
    invalid_formats_list.append("%Y-%D")
    invalid_formats_list.append("%Y-%m-%d %Hh%Mmin")
    invalid_formats_list.append("%Y-%m-%d %Hh%Mmin%Ss")

    return invalid_formats_list

@pytest.fixture
def small_date_format():
    """Return the format of date: YYYY-MM-DD"""
    return "%Y-%m-%d"

@pytest.fixture
def date_one_year_from_now(default_date_format):
    one_year_from_now = DateBuilder().with_years_ahead(1).build()
    return one_year_from_now.strftime(default_date_format)

def test_successful_future_date_happy_path(date_one_year_from_now):
    result = runner.invoke(app, [date_one_year_from_now])
    assert result.exit_code == 0
    assert "month(s)" in result.stdout
    assert "day(s)" in result.stdout
    assert "hour(s)" in result.stdout
    assert "minute(s)" in result.stdout
    assert "second(s)" in result.stdout

@pytest.mark.parametrize("accepted_format", accepted_date_formats_list())
def test_successful_future_date_with_different_date_formats(accepted_format):
    future = DateBuilder().with_years_ahead(2).with_months_ahead(1).with_days_ahead(2).with_hours_ahead(1).with_minutes_ahead(12).with_seconds_ahead(15).build().strftime(accepted_format)

    result = runner.invoke(app, [future])
    assert result.exit_code == 0
    assert "(s)" in result.output

@pytest.mark.parametrize("invalid_format", invalid_date_formats_list())
def test_failure_future_date_with_different_date_formats(invalid_format):
    future = DateBuilder().with_years_ahead(2).with_months_ahead(1).with_days_ahead(2).with_hours_ahead(1).with_minutes_ahead(12).with_seconds_ahead(15).build().strftime(invalid_format)

    result = runner.invoke(app, [future])
    assert result.exception is not None
    assert result.exit_code == 1

def test_successful_one_month_from_now(default_date_format):
    one_month_from_now = DateBuilder().with_months_ahead(1).with_seconds_ahead(15).build().strftime(default_date_format)

    result = runner.invoke(app, [one_month_from_now])
    assert result.exit_code == 0
    assert "1 month(s)" in result.stdout
    assert "year" not in result.stdout

def test_successful_one_day_from_now(default_date_format):
    one_day_from_now = DateBuilder().with_days_ahead(1).with_seconds_ahead(15).build().strftime(default_date_format)

    result = runner.invoke(app, [one_day_from_now])
    assert result.exit_code == 0
    assert "1 day(s)" in result.stdout
    assert "month" not in result.stdout

def test_successful_one_hour_from_now(default_date_format):
    one_hour_from_now = DateBuilder().with_hours_ahead(1).with_seconds_ahead(15).build().strftime(default_date_format)

    result = runner.invoke(app, [one_hour_from_now])
    assert result.exit_code == 0
    assert "1 hour(s)" in result.stdout
    assert "day" not in result.stdout

def test_successful_one_minute_from_now(default_date_format):
    one_minute_from_now = DateBuilder().with_minutes_ahead(1).with_seconds_ahead(15).build().strftime(default_date_format)

    result = runner.invoke(app, [one_minute_from_now])
    assert result.exit_code == 0
    assert "1 minute(s)" in result.stdout
    assert "hour" not in result.stdout

def test_successful_a_few_second_from_now(default_date_format):
    one_second_from_now = DateBuilder().with_seconds_ahead(5).build().strftime(default_date_format)

    result = runner.invoke(app, [one_second_from_now])
    assert result.exit_code == 0
    assert "second(s)" in result.stdout
    assert "minute" not in result.stdout

def test_failure_with_a_past_datetime_from_a_few_seconds_ago(default_date_format):
    one_second_from_now = DateBuilder().with_seconds_ago(5).build().strftime(default_date_format)

    result = runner.invoke(app, [one_second_from_now])
    assert result.exit_code == 1
    assert result.exception is not None

def test_version_option():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Version" in result.stdout

def test_version_option_along_other_parameter(date_one_year_from_now):
    result = runner.invoke(app, [date_one_year_from_now, "--version"])
    assert result.exit_code == 0
    assert "Version" in result.stdout
    assert "seconds" not in result.stdout
    assert "days" not in result.stdout

def test_help_option():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
    assert "Arguments" in result.stdout
    assert "help" in result.stdout

def test_help_option_along_other_parameter(date_one_year_from_now):
    result = runner.invoke(app, [date_one_year_from_now, "--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
    assert "help" in result.stdout
    assert "seconds" not in result.stdout
    assert "days" not in result.stdout