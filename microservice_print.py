import io

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
        print(dic)
        if "type" in dic:
            continue
        else:
            print("add row")
            table.add_row(dic["departure"], dic["destination"],
                      dic["departure time"], dic["arrival time"])\
    # save print as memory(string)
    console = Console(file=io.StringIO(), width=120)
    console.print(table)

    return console.file.getvalue()
