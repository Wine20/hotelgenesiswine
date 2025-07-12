#!/usr/bin/env python3
"""
Script para popular o banco de dados com dados iniciais
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genesis_wine.settings')
django.setup()

from hotel.models import RoomType

def populate_room_types():
    """Cria os tipos de quartos padrão"""
    
    room_types_data = [
        {
            'name': 'Suíte Estudante',
            'slug': 'suite-estudante',
            'price': 500,
            'duration_days': 7,
            'description': 'Perfeita para estudantes que estão começando sua jornada no hotel virtual. Inclui acesso básico a todos os recursos essenciais.',
            'features': [
                'Wi-Fi Premium',
                'Biblioteca Digital Básica',
                'Chat com NALDA',
                'Sistema de Gamificação',
                'Suporte 24/7'
            ]
        },
        {
            'name': 'Suíte Académica',
            'slug': 'suite-academica',
            'price': 1000,
            'duration_days': 30,
            'description': 'Ideal para estudantes regulares que querem aproveitar ao máximo a experiência educacional. Inclui recursos avançados e mentoria.',
            'features': [
                'Wi-Fi Premium',
                'Biblioteca Digital Completa',
                'Chat Avançado com NALDA',
                'Mentoria Semanal',
                'Eventos VIP',
                'Sistema de Gamificação Avançado',
                'Certificados Básicos',
                'Networking Estudantil'
            ]
        },
        {
            'name': 'Suíte Génesis Wine',
            'slug': 'suite-genesis-wine',
            'price': 2000,
            'duration_days': 90,
            'description': 'A experiência completa e premium do Génesis Wine Hotel. Tudo incluído com acesso exclusivo a recursos VIP e mentoria personalizada.',
            'features': [
                'Tudo Incluído Premium',
                'Biblioteca Digital VIP',
                'NALDA Personalizada',
                'Mentoria 1:1 Semanal',
                'Acesso Exclusivo a Eventos',
                'Certificados Oficiais',
                'Networking Executivo',
                'Suporte Prioritário',
                'Recursos Exclusivos Génesis Wine',
                'Gamificação VIP'
            ]
        }
    ]
    
    print("🏨 Criando tipos de quartos...")
    
    for room_data in room_types_data:
        room_type, created = RoomType.objects.get_or_create(
            slug=room_data['slug'],
            defaults=room_data
        )
        
        if created:
            print(f"✅ Criado: {room_type.name}")
        else:
            print(f"📋 Já existe: {room_type.name}")
    
    print(f"\n🎯 Total de tipos de quartos: {RoomType.objects.count()}")

def main():
    print("🏨 Genesis Wine Hotel - Populando Base de Dados")
    print("=" * 50)
    
    try:
        populate_room_types()
        print("\n✅ Base de dados populada com sucesso!")
        print("🚀 Agora você pode executar o servidor Django")
        
    except Exception as e:
        print(f"\n❌ Erro ao popular base de dados: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()