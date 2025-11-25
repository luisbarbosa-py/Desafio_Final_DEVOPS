# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências para dentro do container
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos da API para o container
COPY . .

# Expor a porta que o Flask usa
EXPOSE 1313

# Comando padrão para rodar a aplicação
CMD ["python", "app.py"]
