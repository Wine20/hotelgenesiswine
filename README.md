# 🏨 Génesis Wine Hotel Virtual

O primeiro hotel virtual universitário de Moçambique! Uma plataforma inovadora que combina hospedagem virtual com educação gamificada.

## 🌟 Características Principais

- **🏨 Hotel Virtual**: Experiência única de hospedagem digital
- **🎓 Foco Educacional**: Ambiente pensado para estudantes universitários
- **🤖 NALDA AI**: Assistente virtual inteligente 24/7
- **📚 Biblioteca Digital**: Recursos académicos exclusivos
- **🏆 Gamificação**: Sistema de pontos, níveis e conquistas
- **💼 Mentoria**: Orientação profissional especializada
- **🎪 Eventos VIP**: Acesso a palestras e workshops exclusivos

## 🛏️ Tipos de Suítes

### 🎓 Suíte Estudante (500 MT/semana)
- Wi-Fi Premium
- Biblioteca Digital Básica
- Chat com NALDA
- Sistema de Gamificação
- Suporte 24/7

### 🏛️ Suíte Académica (1000 MT/mês)
- Wi-Fi Premium
- Biblioteca Digital Completa
- Chat Avançado com NALDA
- Mentoria Semanal
- Eventos VIP
- Sistema de Gamificação Avançado
- Certificados Básicos
- Networking Estudantil

### 👑 Suíte Génesis Wine (2000 MT/3 meses)
- Tudo Incluído Premium
- Biblioteca Digital VIP
- NALDA Personalizada
- Mentoria 1:1 Semanal
- Acesso Exclusivo a Eventos
- Certificados Oficiais
- Networking Executivo
- Suporte Prioritário
- Recursos Exclusivos Génesis Wine
- Gamificação VIP

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone <repository-url>
cd "Genesis Wine/Nova Vida"
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Popule o banco com dados iniciais**
```bash
python populate_db.py
```

5. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor**
```bash
python manage.py runserver
```

7. **Acesse a aplicação**
- Aplicação: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 🎯 Funcionalidades

### Para Usuários
- ✅ Registro e autenticação
- ✅ Dashboard personalizado
- ✅ Sistema de reservas
- ✅ Chat com NALDA (IA)
- ✅ Sistema de pontos e níveis
- ✅ Gestão de créditos
- ✅ Histórico de reservas

### Para Administradores
- ✅ Painel administrativo Django
- ✅ Gestão de usuários e perfis
- ✅ Gestão de tipos de quartos
- ✅ Monitoramento de reservas
- ✅ Histórico de conversas com NALDA
- ✅ Comando de limpeza automática

## 🤖 NALDA - Assistente Virtual

A NALDA é nossa assistente virtual inteligente que pode ajudar com:

- 🛏️ Informações sobre quartos e preços
- 📅 Como fazer reservas
- 🎁 Serviços incluídos em cada plano
- 🏆 Sistema de pontos e gamificação
- ❓ Dúvidas gerais sobre o hotel
- 🔧 Suporte técnico básico

## 🏆 Sistema de Gamificação

### Níveis de Usuário
1. **Caloiro** (Nível 1) - Iniciante
2. **Estudante** (Nível 2) - 1000+ pontos
3. **Académico** (Nível 3) - 2500+ pontos
4. **Especialista** (Nível 4) - 5000+ pontos
5. **Mestre Génesis** (Nível 5) - 10000+ pontos

### Como Ganhar Pontos
- 🎯 Fazer reservas (1 ponto por 10 créditos gastos)
- 📅 Login diário (+10 pontos)
- 🎪 Participar de eventos (+50 pontos)
- ✅ Completar tarefas (+25 pontos)
- 🤝 Interagir com outros usuários

## 🛠️ Comandos de Gestão

### Limpeza de Reservas Expiradas
```bash
python manage.py cleanup_expired_reservations
```

## 📁 Estrutura do Projeto

```
Genesis Wine/Nova Vida/
├── genesis_wine/          # Configurações do projeto Django
├── hotel/                 # App principal
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Lógica de visualização
│   ├── urls.py           # Rotas da aplicação
│   ├── admin.py          # Configuração do admin
│   ├── signals.py        # Sinais Django
│   └── management/       # Comandos personalizados
├── templates/            # Templates HTML
│   ├── base.html        # Template base
│   ├── hotel/           # Templates do hotel
│   └── registration/    # Templates de autenticação
├── manage.py            # Utilitário Django
├── populate_db.py       # Script de população inicial
├── requirements.txt     # Dependências Python
└── README.md           # Este arquivo
```

## 🔒 Segurança

- ✅ Proteção CSRF
- ✅ Validação de entrada
- ✅ Rate limiting para chat
- ✅ Sanitização de dados
- ✅ Sessões seguras
- ✅ Transações atômicas

## 🌐 Deploy para Produção

### Configurações Importantes

1. **Altere a SECRET_KEY** em `settings.py`
2. **Configure DEBUG = False**
3. **Configure ALLOWED_HOSTS** adequadamente
4. **Configure banco de dados de produção**
5. **Configure HTTPS** (SESSION_COOKIE_SECURE = True)
6. **Configure arquivos estáticos**

### Exemplo de Configuração para Produção

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']

# Banco de dados PostgreSQL (recomendado)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'genesis_wine_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Segurança HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 📞 Suporte

Para suporte técnico ou dúvidas:
- 🤖 Use a NALDA dentro da aplicação
- 📧 Entre em contato com a equipe de desenvolvimento

## 📄 Licença

Este projeto é propriedade do Génesis Wine Hotel Virtual.

## 🍷 Sobre o Génesis Wine

O Génesis Wine Hotel Virtual é uma iniciativa inovadora para transformar a educação em Moçambique, oferecendo uma experiência única que combina tecnologia, educação e hospitalidade virtual.

**"Onde o Conhecimento Encontra a Excelência"** ✨