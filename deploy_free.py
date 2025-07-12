#!/usr/bin/env python3
"""
Script para deploy gratuito do Génesis Wine Hotel
Suporta Railway, Render, Heroku e outras plataformas gratuitas
"""

import os
import sys
import subprocess
import json

def check_git():
    """Verifica se o Git está configurado"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git não encontrado. Instale o Git primeiro.")
        return False

def init_git_repo():
    """Inicializa repositório Git se necessário"""
    if not os.path.exists('.git'):
        print("📦 Inicializando repositório Git...")
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit - Genesis Wine Hotel'], check=True)
        print("✅ Repositório Git criado!")
    else:
        print("📦 Repositório Git já existe")

def create_railway_config():
    """Cria configuração para Railway"""
    railway_config = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "gunicorn genesis_wine.wsgi --bind 0.0.0.0:$PORT",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    with open('railway.json', 'w') as f:
        json.dump(railway_config, f, indent=2)
    
    print("✅ Configuração Railway criada!")

def create_render_config():
    """Cria configuração para Render"""
    render_config = {
        "services": [
            {
                "type": "web",
                "name": "genesis-wine-hotel",
                "env": "python",
                "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput --settings=genesis_wine.settings_free_deploy",
                "startCommand": "gunicorn genesis_wine.wsgi:application --bind 0.0.0.0:$PORT",
                "envVars": [
                    {
                        "key": "DJANGO_SETTINGS_MODULE",
                        "value": "genesis_wine.settings_free_deploy"
                    },
                    {
                        "key": "SECRET_KEY",
                        "generateValue": True
                    }
                ]
            }
        ]
    }
    
    with open('render.yaml', 'w') as f:
        import yaml
        yaml.dump(render_config, f, default_flow_style=False)
    
    print("✅ Configuração Render criada!")

def create_vercel_config():
    """Cria configuração para Vercel"""
    vercel_config = {
        "builds": [
            {
                "src": "genesis_wine/wsgi.py",
                "use": "@vercel/python"
            }
        ],
        "routes": [
            {
                "src": "/(.*)",
                "dest": "genesis_wine/wsgi.py"
            }
        ],
        "env": {
            "DJANGO_SETTINGS_MODULE": "genesis_wine.settings_free_deploy"
        }
    }
    
    with open('vercel.json', 'w') as f:
        json.dump(vercel_config, f, indent=2)
    
    print("✅ Configuração Vercel criada!")

def create_env_example():
    """Cria arquivo .env de exemplo para deploy"""
    env_content = """# Génesis Wine Hotel - Environment Variables for Free Deployment

# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=genesis_wine.settings_free_deploy

# Security Settings (enable for HTTPS)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Domain Configuration
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (SQLite for free deployment)
DATABASE_URL=sqlite:///db.sqlite3
"""
    
    with open('.env.deploy', 'w') as f:
        f.write(env_content)
    
    print("✅ Arquivo .env.deploy criado!")

def show_deployment_instructions():
    """Mostra instruções de deploy"""
    print("\n" + "="*60)
    print("🚀 INSTRUÇÕES DE DEPLOY GRATUITO")
    print("="*60)
    
    print("\n📋 OPÇÕES DE HOSTING GRATUITO:")
    print("1. 🚂 Railway (Recomendado)")
    print("2. 🎨 Render")
    print("3. 🟣 Heroku")
    print("4. ▲ Vercel")
    
    print("\n🚂 RAILWAY (Mais Fácil):")
    print("1. Acesse: https://railway.app")
    print("2. Conecte sua conta GitHub")
    print("3. Clique em 'New Project' > 'Deploy from GitHub repo'")
    print("4. Selecione este repositório")
    print("5. Railway detectará automaticamente o Django")
    print("6. Seu site estará online em minutos!")
    
    print("\n🎨 RENDER:")
    print("1. Acesse: https://render.com")
    print("2. Conecte sua conta GitHub")
    print("3. Clique em 'New' > 'Web Service'")
    print("4. Selecione este repositório")
    print("5. Configure:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn genesis_wine.wsgi:application")
    print("   - Environment: DJANGO_SETTINGS_MODULE=genesis_wine.settings_free_deploy")
    
    print("\n🟣 HEROKU:")
    print("1. Instale Heroku CLI")
    print("2. heroku login")
    print("3. heroku create genesis-wine-hotel")
    print("4. git push heroku main")
    
    print("\n🌐 DOMÍNIO GRATUITO:")
    print("• Railway: app-name.railway.app")
    print("• Render: app-name.onrender.com")
    print("• Heroku: app-name.herokuapp.com")
    print("• Vercel: app-name.vercel.app")
    
    print("\n🔗 DOMÍNIO PERSONALIZADO GRATUITO:")
    print("• Freenom: .tk, .ml, .ga, .cf")
    print("• No-IP: subdomínio gratuito")
    print("• Cloudflare: DNS gratuito")
    
    print("\n✅ PRÓXIMOS PASSOS:")
    print("1. Faça push do código para GitHub")
    print("2. Escolha uma plataforma de hosting")
    print("3. Configure as variáveis de ambiente")
    print("4. Seu hotel virtual estará online!")

def main():
    print("🏨 Génesis Wine Hotel - Deploy Gratuito")
    print("="*50)
    
    if not check_git():
        return
    
    print("📦 Preparando arquivos de deploy...")
    
    # Criar configurações para diferentes plataformas
    create_railway_config()
    create_render_config()
    create_vercel_config()
    create_env_example()
    
    # Inicializar Git se necessário
    init_git_repo()
    
    print("\n✅ Arquivos de deploy criados com sucesso!")
    
    # Mostrar instruções
    show_deployment_instructions()

if __name__ == "__main__":
    main()