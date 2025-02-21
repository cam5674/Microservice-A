from rich.console import Console
from rich.table import Table


def create_columns():
    table = Table("Departure", style="magenta")
    table.add_column("Destination", justify="right", style="white")
    table.add_column("Departure time", justify="right", style="white")
    table.add_column("Arrival time", justify="right", style="white")
    return table


def create_table(data):
    table = create_columns()
    for dic in data:
        table.add_row(dic["departure"], dic["destination"],
                  dic["departure time"], dic["arrival time"])
    console = Console(color_system="windows")
    console.print(table)