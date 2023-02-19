from src.logging.log import PabLog
from src.input_processing import InputProcessing, ElectriciyInput
import pandas as pd


lg = PabLog(
    log_filepath='./assets/logs/log_.log'
)

lg.add_title('Process Starts')

electricity_input = pd.read_csv('./assets/data/electricity/PJME_hourly.csv')
inp = ElectriciyInput(electricity_input)
inp.process_data()
inp.display_data()
data = inp.get_processed_data()