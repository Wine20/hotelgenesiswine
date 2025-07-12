# Dockerfile para Génesis Wine Hotel Virtual
FROM python:3.11-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . /app/

# Criar diretório para logs
RUN mkdir -p /app/logs

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput --settings=genesis_wine.settings_production

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]