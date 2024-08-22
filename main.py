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