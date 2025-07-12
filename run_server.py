#!/usr/bin/env python3
"""
Script para executar o servidor de desenvolvimento do Génesis Wine Hotel Virtual
"""

import os
import sys
import subprocess
import platform
import webbrowser
import time

def find_python_command():
    """Encontra o comando Python correto para o sistema"""
    if platform.system() == "Windows":
        python_paths = [
            "C:\\Users\\dazik\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
            "python",
            "py",
            "python3"
        ]
        for path in python_paths:
            try:
                result = subprocess.run([path, "--version"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return path
            except:
                continue
        return "python"
    else:
        return "python3"

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import django
        print(f"✅ Django {django.get_version()} instalado")
        return True
    except ImportError:
        print("❌ Django não encontrado. Execute: pip install -r requirements.txt")
        return False

def check_database():
    """Verifica se o banco de dados está configurado"""
    if os.path.exists("db.sqlite3"):
        print("✅ Banco de dados encontrado")
        return True
    else:
        print("⚠️ Banco de dados não encontrado. Será criado automaticamente.")
        return False

def run_migrations(python_cmd):
    """Executa as migrações do banco de dados"""
    print("\n🔄 Verificando migrações...")
    try:
        # Criar migrações se necessário
        subprocess.run([python_cmd, "manage.py", "makemigrations"], check=True)
        # Aplicar migrações
        subprocess.run([python_cmd, "manage.py", "migrate"], check=True)
        print("✅ Migrações aplicadas com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao aplicar migrações")
        return False

def populate_database(python_cmd):
    """Popula o banco de dados com dados iniciais"""
    try:
        result = subprocess.run([python_cmd, "populate_db.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Banco de dados populado com dados iniciais")
        else:
            print("⚠️ Dados iniciais já existem ou erro ao popular")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao popular banco de dados")
        return False

def main():
    print("🏨 Génesis Wine Hotel Virtual - Servidor de Desenvolvimento")
    print("=" * 65)
    
    # Encontrar comando Python
    python_cmd = find_python_command()
    print(f"🐍 Usando Python: {python_cmd}")
    
    # Verificar dependências
    if not check_dependencies():
        print("\n💡 Para instalar dependências:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Verificar banco de dados
    db_exists = check_database()
    
    # Executar migrações se necessário
    if not db_exists or not os.path.exists("hotel/migrations/0001_initial.py"):
        if not run_migrations(python_cmd):
            sys.exit(1)
    
    # Popular banco se necessário
    if not db_exists:
        populate_database(python_cmd)
    
    print("\n🚀 Iniciando servidor Django...")
    print("📍 URL: http://127.0.0.1:8000/")
    print("🔑 Admin: http://127.0.0.1:8000/admin/")
    print("⏹️ Para parar: Ctrl+C")
    print("\n" + "=" * 65)
    
    try:
        # Aguardar um pouco e abrir navegador
        def open_browser():
            time.sleep(2)
            try:
                webbrowser.open('http://127.0.0.1:8000/')
                print("🌐 Navegador aberto automaticamente")
            except:
                pass
        
        import threading
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Executar servidor
        subprocess.run([python_cmd, "manage.py", "runserver"], check=True)
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Servidor parado pelo usuário")
        print("👋 Obrigado por usar o Génesis Wine Hotel Virtual!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro ao executar servidor: {e}")
        print("\n💡 Tente executar manualmente:")
        print(f"   {python_cmd} manage.py runserver")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()