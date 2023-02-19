import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from datetime import datetime
import pandas as pd

import os 

class PabLog:
    """
    
    """
    def __init__(
        self,
        log_filepath:str = None,
        __format: str = "- %(message)s"
        )->None:

        self.avaliable_colors = []
        self.log_filepath = log_filepath
        self.rich_handler = RichHandler(rich_tracebacks=True)

        date_str = str(datetime.today()).replace(
            " ", "_"
        ).replace(':','_')[0:19]
        
        with open('./src/logging/avaliable_colors.txt', 'r') as f:
                self.avaliable_colors=f.read().splitlines()

        if self.log_filepath is not None:
            if self.log_filepath.__contains__('.log')==True:
                self.log_filepath = self.log_filepath.replace(
                    '.log', date_str + '.log'
                )
            else:
                raise Exception("log_filepath must contain a valid filename and a .log extenssion")

            __handlers = [
                logging.FileHandler(self.log_filepath),
                self.rich_handler
            ]

        else:
            __handlers = [self.rich_handler]

        logging.basicConfig(
            format = __format,
            handlers=__handlers,
            level = logging.DEBUG
        )

        self.log = logging.getLogger()
        self.console = Console()

    def add_table(self,df:pd.DataFrame, title:str = '', max_rows:int = 10)-> None:
        table = Table(title=title)
        color = 0
        for col in df.columns:
            if color >= len(self.avaliable_colors) -1:
                color = 0
            else:
                color += 1

            table.add_column(str(col),
                             style=self.avaliable_colors[color])
        
        for index, row in df.head(max_rows).iterrows():
            table.add_row(*[str(r) for r in row])

        self.console.print(table)

    def add_md(self, markdown: str):
        md = Markdown(markdown)
        self.console.print(md)

    def add_title(self, title:str):
        md = f" # **{title}** "
        md = Markdown(md)
        self.console.print(md)
