
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /pysus_extract

# Instalar as dependências
RUN pip install --no-cache-dir pysus==0.15.0 pyarrow

# Comando padrão (opcional, pode ser ajustado conforme a necessidade)
CMD ["python", "script.py"]
