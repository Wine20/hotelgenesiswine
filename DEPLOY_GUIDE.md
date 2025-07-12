# 🚀 Guia de Deploy - Génesis Wine Hotel Virtual

Este guia fornece instruções detalhadas para fazer o deploy da aplicação em produção.

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL (recomendado para produção)
- Nginx ou Apache
- Servidor Linux (Ubuntu/CentOS recomendado)
- Domínio configurado

## 🔧 Configuração do Servidor

### 1. Preparar o Servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install python3 python3-pip python3-venv postgresql postgresql-contrib nginx git -y

# Criar usuário para a aplicação
sudo adduser genesis
sudo usermod -aG sudo genesis
```

### 2. Configurar PostgreSQL

```bash
# Acessar PostgreSQL
sudo -u postgres psql

# Criar banco e usuário
CREATE DATABASE genesis_wine_db;
CREATE USER genesis_user WITH PASSWORD 'sua_senha_segura';
ALTER ROLE genesis_user SET client_encoding TO 'utf8';
ALTER ROLE genesis_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE genesis_user SET timezone TO 'Africa/Maputo';
GRANT ALL PRIVILEGES ON DATABASE genesis_wine_db TO genesis_user;
\q
```

### 3. Configurar a Aplicação

```bash
# Mudar para usuário genesis
su - genesis

# Clonar repositório
git clone <seu-repositorio> genesis_wine_hotel
cd genesis_wine_hotel

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Configurar variáveis de ambiente
cp .env.example .env
nano .env
```

### 4. Configurar Variáveis de Ambiente

Criar arquivo `.env`:

```bash
# .env
SECRET_KEY=sua_chave_secreta_muito_segura_aqui
DEBUG=False
ALLOWED_HOSTS=seudominio.com,www.seudominio.com

# Database
DB_NAME=genesis_wine_db
DB_USER=genesis_user
DB_PASSWORD=sua_senha_segura
DB_HOST=localhost
DB_PORT=5432

# Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_app
```

### 5. Configurar Django para Produção

```bash
# Aplicar migrações
python manage.py migrate --settings=genesis_wine.settings_production

# Coletar arquivos estáticos
python manage.py collectstatic --noinput --settings=genesis_wine.settings_production

# Popular banco de dados
python populate_db.py

# Criar superusuário
python manage.py createsuperuser --settings=genesis_wine.settings_production
```

## 🌐 Configuração do Nginx

### 1. Configurar Nginx

```bash
sudo nano /etc/nginx/sites-available/genesis_wine
```

Conteúdo do arquivo:

```nginx
server {
    listen 80;
    server_name seudominio.com www.seudominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/genesis/genesis_wine_hotel;
    }
    
    location /media/ {
        root /home/genesis/genesis_wine_hotel;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/genesis/genesis_wine_hotel/genesis_wine.sock;
    }
}
```

```bash
# Ativar site
sudo ln -s /etc/nginx/sites-available/genesis_wine /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 🔄 Configurar Gunicorn

### 1. Criar arquivo de configuração do Gunicorn

```bash
nano /home/genesis/genesis_wine_hotel/gunicorn_config.py
```

```python
# gunicorn_config.py
bind = "unix:/home/genesis/genesis_wine_hotel/genesis_wine.sock"
workers = 3
user = "genesis"
group = "genesis"
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
preload_app = True
```

### 2. Criar serviço systemd

```bash
sudo nano /etc/systemd/system/genesis_wine.service
```

```ini
[Unit]
Description=Genesis Wine Hotel Virtual
After=network.target

[Service]
User=genesis
Group=www-data
WorkingDirectory=/home/genesis/genesis_wine_hotel
Environment="DJANGO_SETTINGS_MODULE=genesis_wine.settings_production"
ExecStart=/home/genesis/genesis_wine_hotel/venv/bin/gunicorn \
          --config /home/genesis/genesis_wine_hotel/gunicorn_config.py \
          genesis_wine.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
# Ativar e iniciar serviço
sudo systemctl daemon-reload
sudo systemctl start genesis_wine
sudo systemctl enable genesis_wine
sudo systemctl status genesis_wine
```

## 🔒 Configurar HTTPS (SSL)

### 1. Instalar Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Obter certificado SSL

```bash
sudo certbot --nginx -d seudominio.com -d www.seudominio.com
```

### 3. Configurar renovação automática

```bash
sudo crontab -e
```

Adicionar linha:

```bash
0 12 * * * /usr/bin/certbot renew --quiet
```

## 📊 Monitoramento e Manutenção

### 1. Scripts de Manutenção

Criar arquivo `/home/genesis/scripts/maintenance.sh`:

```bash
#!/bin/bash
cd /home/genesis/genesis_wine_hotel
source venv/bin/activate

# Limpeza de reservas expiradas
python manage.py cleanup_expired_reservations --settings=genesis_wine.settings_production

# Gerar relatório
python manage.py generate_report --settings=genesis_wine.settings_production

# Backup do banco
pg_dump genesis_wine_db > /home/genesis/backups/db_$(date +%Y%m%d_%H%M%S).sql
```

### 2. Configurar Cron para Manutenção

```bash
crontab -e
```

```bash
# Limpeza diária às 2:00
0 2 * * * /home/genesis/scripts/maintenance.sh

# Backup semanal aos domingos às 3:00
0 3 * * 0 /home/genesis/scripts/backup.sh
```

## 🔄 Atualizações

### Script de Atualização

```bash
#!/bin/bash
cd /home/genesis/genesis_wine_hotel
source venv/bin/activate

# Backup antes da atualização
python manage.py generate_report --settings=genesis_wine.settings_production > /tmp/pre_update_report.txt

# Atualizar código
git pull origin main

# Instalar novas dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate --settings=genesis_wine.settings_production

# Coletar arquivos estáticos
python manage.py collectstatic --noinput --settings=genesis_wine.settings_production

# Reiniciar serviços
sudo systemctl restart genesis_wine
sudo systemctl reload nginx

echo "✅ Atualização concluída!"
```

## 📈 Monitoramento

### 1. Logs Importantes

```bash
# Logs da aplicação
tail -f /home/genesis/genesis_wine_hotel/logs/django.log

# Logs do Gunicorn
sudo journalctl -u genesis_wine -f

# Logs do Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### 2. Comandos Úteis

```bash
# Status dos serviços
sudo systemctl status genesis_wine
sudo systemctl status nginx
sudo systemctl status postgresql

# Reiniciar serviços
sudo systemctl restart genesis_wine
sudo systemctl restart nginx

# Verificar configuração do Nginx
sudo nginx -t

# Gerar relatório do sistema
python manage.py generate_report --settings=genesis_wine.settings_production
```

## 🚨 Troubleshooting

### Problemas Comuns

1. **Erro 502 Bad Gateway**
   - Verificar se Gunicorn está rodando
   - Verificar logs do Gunicorn
   - Verificar permissões do socket

2. **Arquivos estáticos não carregam**
   - Executar `collectstatic` novamente
   - Verificar configuração do Nginx
   - Verificar permissões dos arquivos

3. **Erro de banco de dados**
   - Verificar se PostgreSQL está rodando
   - Verificar credenciais no `.env`
   - Verificar se as migrações foram aplicadas

### Comandos de Diagnóstico

```bash
# Verificar conectividade do banco
python manage.py dbshell --settings=genesis_wine.settings_production

# Verificar configuração Django
python manage.py check --settings=genesis_wine.settings_production

# Testar Gunicorn manualmente
/home/genesis/genesis_wine_hotel/venv/bin/gunicorn --bind 0.0.0.0:8000 genesis_wine.wsgi:application
```

## 📞 Suporte

Para suporte adicional:
- Verificar logs detalhados
- Consultar documentação do Django
- Contatar equipe de desenvolvimento

---

🍷 **Génesis Wine Hotel Virtual** - Deploy Guide v1.0