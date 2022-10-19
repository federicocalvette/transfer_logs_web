import pandas as pd
import uuid

def get_csv(json_list):
    df = pd.DataFrame(json_list)
    file_name = str(uuid.uuid4().hex)
    df.to_csv(f'./download_file/{file_name}.csv')

    return f'{file_name}.csv'