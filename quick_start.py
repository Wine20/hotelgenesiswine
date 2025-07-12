#!/usr/bin/env python3
"""
Script de inicialização rápida para o Génesis Wine Hotel Virtual
"""

import os
import sys
import subprocess
import platform

def run_command(command, description, check=True):
    """Execute um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        else:
            result = subprocess.run(command.split(), check=check, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ {description} - Concluído")
            if result.stdout.strip():
                print(result.stdout)
        else:
            print(f"⚠️ {description} - Aviso:")
            if result.stderr:
                print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"❌ {description} - Erro inesperado: {e}")
        return False

def check_python():
    """Verifica se Python está instalado"""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
            return True
        else:
            print(f"❌ Python {version.major}.{version.minor} detectado. Necessário Python 3.8+")
            return False
    except Exception:
        print("❌ Erro ao verificar versão do Python")
        return False

def main():
    print("🏨 Génesis Wine Hotel Virtual - Inicialização Rápida")
    print("=" * 60)
    
    # Verificar Python
    if not check_python():
        print("\n❌ Por favor, instale Python 3.8+ e tente novamente.")
        sys.exit(1)
    
    # Detectar sistema operacional
    system = platform.system()
    print(f"🖥️ Sistema detectado: {system}")
    
    # Comandos baseados no sistema
    if system == "Windows":
        # Tentar encontrar o Python correto no Windows
        python_paths = [
            "python",
            "C:\\Users\\dazik\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
            "py",
            "python3"
        ]
        python_cmd = "python"
        for path in python_paths:
            try:
                result = subprocess.run([path, "--version"], capture_output=True, text=True)
                if result.returncode == 0:
                    python_cmd = path
                    break
            except:
                continue
        pip_cmd = "pip"
    else:
        python_cmd = "python3"
        pip_cmd = "pip3"
    
    print("\n🚀 Iniciando configuração...")
    
    # Lista de comandos para setup
    setup_commands = [
        (f"{pip_cmd} install -r requirements.txt", "Instalando dependências Python"),
        (f"{python_cmd} manage.py makemigrations", "Criando migrações"),
        (f"{python_cmd} manage.py migrate", "Aplicando migrações ao banco de dados"),
        (f"{python_cmd} populate_db.py", "Populando banco com dados iniciais"),
    ]
    
    # Executar comandos de setup
    for command, description in setup_commands:
        if not run_command(command, description):
            print(f"\n❌ Falha durante: {description}")
            print("💡 Tente executar os comandos manualmente:")
            for cmd, desc in setup_commands:
                print(f"   {cmd}")
            sys.exit(1)
    
    # Perguntar se quer criar superusuário
    print("\n👤 Deseja criar um superusuário para acessar o admin? (s/n): ", end="")
    try:
        create_superuser = input().lower().strip()
        if create_superuser in ['s', 'sim', 'y', 'yes']:
            print("\n🔑 Criando superusuário...")
            print("📝 Siga as instruções abaixo:")
            os.system(f"{python_cmd} manage.py createsuperuser")
    except KeyboardInterrupt:
        print("\n⏭️ Pulando criação de superusuário...")
    
    # Gerar relatório inicial
    run_command(
        f"{python_cmd} manage.py generate_report", 
        "Gerando relatório inicial do sistema",
        check=False
    )
    
    print("\n🎉 Configuração concluída com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Execute o servidor: python manage.py runserver")
    print("2. Acesse: http://127.0.0.1:8000/")
    print("3. Admin: http://127.0.0.1:8000/admin/")
    
    print("\n🛏️ Tipos de quartos disponíveis:")
    print("• Suíte Estudante: 500 MT/semana")
    print("• Suíte Académica: 1000 MT/mês")
    print("• Suíte Génesis Wine: 2000 MT/3 meses")
    
    print("\n🤖 Recursos disponíveis:")
    print("• Chat com NALDA (IA)")
    print("• Sistema de pontos e níveis")
    print("• Gestão de reservas")
    print("• Dashboard personalizado")
    
    print("\n💡 Comandos úteis:")
    print(f"• Relatório do sistema: {python_cmd} manage.py generate_report")
    print(f"• Limpeza de reservas: {python_cmd} manage.py cleanup_expired_reservations")
    print(f"• Adicionar créditos: {python_cmd} manage.py add_credits --username=admin --credits=1000")
    
    print("\n🍷 Génesis Wine Hotel Virtual está pronto!")
    print("\"Onde o Conhecimento Encontra a Excelência\" ✨")
    
    # Perguntar se quer iniciar o servidor
    print("\n🚀 Deseja iniciar o servidor agora? (s/n): ", end="")
    try:
        start_server = input().lower().strip()
        if start_server in ['s', 'sim', 'y', 'yes']:
            print("\n🌐 Iniciando servidor Django...")
            print("📍 Acesse: http://127.0.0.1:8000/")
            print("⏹️ Para parar: Ctrl+C")
            os.system(f"{python_cmd} manage.py runserver")
    except KeyboardInterrupt:
        print("\n👋 Até logo!")

if __name__ == "__main__":
    main()