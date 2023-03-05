"""Application that calculate time duration until reach a given date."""
from datetime import datetime
from typing import Optional
import typer
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

__version__ = "0.1.0"

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    help="Application that calculate time duration until reach a given date."
)

def version_callback(value: bool):
    if value:
        print(f"time_until CLI Version: {__version__}")
        raise typer.Exit()

def validate_date(target: str):
    """Validate with the reference date format"""
    parsed_target = parse(target)
    return (True, parsed_target)

def calculate_delta(origin: datetime, target: datetime):
    """calculate time duration from ORIGIN to TARGET"""
    return relativedelta(origin, target)

def print_output(delta: relativedelta):
    """Define a way to output information from the `relativedelta` input"""
    result=[]
    if delta.years > 0:
        result.append("{} year(s) ".format(delta.years))
    if delta.months > 0:
        result.append("{} month(s) ".format(delta.months))
    if delta.days > 0:
        result.append("{} day(s) ".format(delta.days))
    if delta.hours > 0:
        result.append("{} hour(s) ".format(delta.hours))
    if delta.minutes > 0:
        result.append("{} minute(s) ".format(delta.minutes))
    if delta.seconds > 0:
        result.append("{} second(s) ".format(delta.seconds))

    result.insert(0, 'Time remaining: ')
    print(''.join(result))

@app.command()
def time_until(
        target: str = typer.Argument(..., help="Future date or time used as reference."),
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        )
    ):
    """Application that calculate time duration until reach a given date."""

    is_valid, parsed_target = validate_date(target)
    rightnow = datetime.now()

    if parsed_target < datetime.now():
        raise ValueError("Not possible to calculate duration to a past date or time. Try again with future date OR time.")
    
    if is_valid:   
        result = calculate_delta(parsed_target, rightnow)
        print_output(result)

if __name__ == "__main__":
    app()