
import os
import pandas as pd
from pysus import SIH

output_directory = "/pysus_extract/raw_data"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

ano = [2019, 2020, 2021, 2022, 2023, 2024]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
estado = ['SP']
grupo = ['RD']
diagnosticos = ('F31', 'F32', 'F19', 'F2')


sih = SIH().load() # Loads the files from DATASUS
files = sih.get_files(group=grupo, uf=estado, year=ano, month=mes)
print(files)

def load_data(files, output_diretory):
  for file in files:
    parquet = sih.download(file)
    df = parquet.to_dataframe()
    df = df[df.apply(get_cid, axis=1)]
    file_name = str(file).split('.dbc')[0]
    output_file = os.path.join(output_diretory, f'{file_name}.parquet')
    df.to_parquet(output_file)

def get_cid(lancamento):
    cid_principal = str(lancamento['DIAG_PRINC'])
    if pd.notna(cid_principal) and cid_principal.startswith(diagnosticos):
        return True
    return False
load_data(files, output_directory)
