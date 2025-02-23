import io

from rich.console import Console
from rich.table import Table


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
            table.add_row(dic["departure"], dic["destination"],
                      dic["departure time"], dic["arrival time"])\

    # save print as memory(string)
    console = Console(file=io.StringIO(), width=120)
    console.print(table)

    return console.file.getvalue()
