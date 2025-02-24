import io

from rich.console import Console
from rich.table import Table
from datetime import datetime

def create_columns():
    """
    Creates three columns for the table
    :return:
    """
    table = Table("Departure", style="magenta")
    table.add_column("Destination", justify="right", style="white")
    table.add_column("Departure time", justify="right", style="white")
    table.add_column("Arrival time", justify="right", style="white")
    return table


def create_table(data):
    """
    Loops through the list of dictionaries and adds rows to the table.
    :param data: list of dictionaries
    :return: a string of the table
    """

    table = create_columns()

    # add rows to the table
    for dic in data:
        if "type" in dic:
            continue
        else:
            # convert departure times into a readable string
            d_date_time = datetime.fromisoformat(dic["departure time"])
            d_readable_string = d_date_time.strftime("%Y-%m-%d %H:%M:%S UTC")

            # convert arrival times into a readable string
            a_date_time = datetime.fromisoformat(dic["arrival time"])
            a_readable_string = a_date_time.strftime("%Y-%m-%d %H:%M:%S UTC")
            table.add_row(dic["departure"], dic["destination"],
                          d_readable_string, a_readable_string)

    # save print as memory(string)
    console = Console(file=io.StringIO(), width=120)
    console.print(table)

    return console.file.getvalue()
