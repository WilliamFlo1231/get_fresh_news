import logging
import pandas as pd
from AP.process import AP
from datetime import datetime
from robocorp.tasks import task
from utils.config import load_config
from RPA.Robocorp.WorkItems import WorkItems

@task
def main():
    CONFIG = load_config('config.yaml')
    library = WorkItems()
    library.get_input_work_item()
    parameters = library.get_work_item_variables()
    print(parameters)
    CURRENT_DATE = datetime.today()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    retries = 0
    while retries < CONFIG.max_retries:
        try:
            ap_process = AP(CONFIG, CURRENT_DATE)
            ap_process.start()
            logging.info('Saving News Report')
            output_data = pd.DataFrame(ap_process.news)
            output_data['date'] = output_data['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            output_data.to_excel(f'{CONFIG.paths.output}/{CONFIG.search_phrase}.xlsx', index=False)
            break
        except Exception as e:
            logging.error(e)
            retries += 1