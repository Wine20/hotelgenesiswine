#!/usr/bin/env python3
"""
Script de deploy para o Génesis Wine Hotel Virtual
"""

import os
import sys
import subprocess
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genesis_wine.settings_production')
django.setup()

def run_command(command, description):
    """Execute um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Concluído")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro:")
        print(e.stderr)
        return False

def main():
    print("🏨 Genesis Wine Hotel Virtual - Script de Deploy")
    print("=" * 50)
    
    # Lista de comandos para deploy
    commands = [
        ("python manage.py collectstatic --noinput", "Coletando arquivos estáticos"),
        ("python manage.py makemigrations", "Criando migrações"),
        ("python manage.py migrate", "Aplicando migrações"),
        ("python manage.py cleanup_expired_reservations", "Limpando reservas expiradas"),
    ]
    
    # Executar comandos
    for command, description in commands:
        if not run_command(command, description):
            print(f"\n❌ Deploy falhou em: {description}")
            sys.exit(1)
    
    # Verificar se precisa popular o banco
    try:
        from hotel.models import RoomType
        if RoomType.objects.count() == 0:
            print("\n🔄 Banco vazio detectado. Populando com dados iniciais...")
            if run_command("python populate_db.py", "Populando banco de dados"):
                print("✅ Dados iniciais adicionados")
            else:
                print("⚠️ Aviso: Falha ao popular dados iniciais")
    except Exception as e:
        print(f"⚠️ Aviso: Não foi possível verificar dados iniciais: {e}")
    
    print("\n🎉 Deploy concluído com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Configure seu servidor web (Nginx/Apache)")
    print("2. Configure o WSGI (Gunicorn/uWSGI)")
    print("3. Configure HTTPS")
    print("4. Configure backup automático")
    print("5. Configure monitoramento")
    
    print("\n🔗 URLs importantes:")
    print("- Aplicação: https://seudominio.com/")
    print("- Admin: https://seudominio.com/admin/")
    
    print("\n🍷 Génesis Wine Hotel Virtual está pronto para produção!")

if __name__ == "__main__":
    main()