# 🚀 Deploy Gratuito - Génesis Wine Hotel

## 📋 Resumo
Este guia mostra como publicar o Génesis Wine Hotel **gratuitamente** com domínio incluído.

## ✅ Bugs Corrigidos
- ✅ Créditos iniciais corrigidos (5.000 MT)
- ✅ Configuração de produção otimizada
- ✅ Whitenoise para arquivos estáticos
- ✅ Settings específicos para deploy gratuito
- ✅ Configurações para múltiplas plataformas

## 🌐 Opções de Hosting Gratuito

### 🚂 Railway (Recomendado) ⭐
**Por que escolher:** Mais fácil, rápido e confiável

1. **Acesse:** https://railway.app
2. **Conecte GitHub:** Faça login com sua conta GitHub
3. **Novo Projeto:** Clique em "New Project" → "Deploy from GitHub repo"
4. **Selecione Repositório:** Escolha este projeto
5. **Deploy Automático:** Railway detecta Django automaticamente
6. **Pronto!** Seu site estará online em 2-3 minutos

**Domínio:** `seu-app.railway.app`

### 🎨 Render
**Por que escolher:** Interface amigável, boa documentação

1. **Acesse:** https://render.com
2. **Conecte GitHub:** Faça login com GitHub
3. **Web Service:** Clique em "New" → "Web Service"
4. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn genesis_wine.wsgi:application`
   - **Environment:** `DJANGO_SETTINGS_MODULE=genesis_wine.settings_free_deploy`

**Domínio:** `seu-app.onrender.com`

### 🟣 Heroku
**Por que escolher:** Tradicional, muita documentação

1. **Instale Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli
2. **Login:** `heroku login`
3. **Criar App:** `heroku create genesis-wine-hotel`
4. **Deploy:** `git push heroku main`

**Domínio:** `seu-app.herokuapp.com`

## 🌐 Domínio Personalizado Gratuito

### 🆓 Freenom (Domínios Gratuitos)
- **Site:** https://freenom.com
- **Extensões:** .tk, .ml, .ga, .cf
- **Duração:** 12 meses (renovável)
- **Exemplo:** `genesiswine.tk`

### 🔗 No-IP (Subdomínio)
- **Site:** https://noip.com
- **Formato:** `genesiswine.ddns.net`
- **Gratuito:** Sim, com renovação mensal

### ☁️ Cloudflare (DNS Gratuito)
- **Site:** https://cloudflare.com
- **Benefícios:** CDN, SSL, proteção DDoS
- **Custo:** Gratuito

## 📦 Preparação para Deploy

### 1. Subir para GitHub
```bash
git init
git add .
git commit -m "Genesis Wine Hotel - Ready for deployment"
git branch -M main
git remote add origin https://github.com/seu-usuario/genesis-wine-hotel.git
git push -u origin main
```

### 2. Configurar Variáveis de Ambiente
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
DJANGO_SETTINGS_MODULE=genesis_wine.settings_free_deploy
```

## 🚀 Deploy em 5 Minutos (Railway)

### Passo a Passo Detalhado:

1. **GitHub:** Suba o código para GitHub
2. **Railway:** Acesse railway.app e faça login
3. **Deploy:** Clique em "Deploy from GitHub repo"
4. **Selecione:** Escolha o repositório genesis-wine-hotel
5. **Aguarde:** Railway fará o build automaticamente
6. **Acesse:** Clique no link gerado (ex: genesis-wine-hotel.railway.app)

### ⚡ Deploy Automático
Railway detecta automaticamente:
- ✅ Python/Django
- ✅ Requirements.txt
- ✅ Procfile
- ✅ Configurações de produção

## 🔧 Configurações Automáticas

### Arquivos Criados:
- `Procfile` - Comandos de inicialização
- `railway.json` - Configuração Railway
- `render.yaml` - Configuração Render
- `settings_free_deploy.py` - Settings otimizados
- `requirements.txt` - Dependências atualizadas

### Recursos Incluídos:
- ✅ Whitenoise para arquivos estáticos
- ✅ SQLite para banco (sem configuração extra)
- ✅ Migrações automáticas
- ✅ Coleta de arquivos estáticos
- ✅ Configurações de segurança

## 🎯 Após o Deploy

### 1. Acessar Admin
- URL: `https://seu-dominio.com/admin/`
- Criar superusuário: `python manage.py createsuperuser`

### 2. Popular Dados
- Os tipos de quartos são criados automaticamente
- Usuários ganham 5.000 créditos iniciais
- Sistema de gamificação ativo

### 3. Testar Funcionalidades
- ✅ Registro de usuários
- ✅ Sistema de reservas
- ✅ Chat NALDA
- ✅ Dashboard
- ✅ Gamificação

## 💡 Dicas de Otimização

### Performance:
- ✅ Whitenoise para arquivos estáticos
- ✅ Compressão automática
- ✅ Cache de templates
- ✅ Configurações otimizadas

### Segurança:
- ✅ HTTPS automático
- ✅ Headers de segurança
- ✅ CSRF protection
- ✅ XSS protection

### Monitoramento:
- ✅ Logs estruturados
- ✅ Error tracking
- ✅ Performance monitoring

## 🆘 Solução de Problemas

### Build Falhou?
1. Verifique `requirements.txt`
2. Confirme Python 3.8+
3. Verifique logs de build

### Site não Carrega?
1. Verifique variáveis de ambiente
2. Confirme `ALLOWED_HOSTS`
3. Verifique logs da aplicação

### Banco de Dados?
1. Execute migrações: `python manage.py migrate`
2. Crie superusuário: `python manage.py createsuperuser`
3. Popule dados: `python populate_db.py`

## 🎉 Resultado Final

Após seguir este guia, você terá:

- 🌐 **Site Online:** Acessível 24/7
- 🆓 **Custo Zero:** Hosting e domínio gratuitos
- ⚡ **Performance:** Otimizado para produção
- 🔒 **Seguro:** HTTPS e proteções ativas
- 📱 **Responsivo:** Funciona em todos dispositivos

## 🔗 Links Úteis

- **Railway:** https://railway.app
- **Render:** https://render.com
- **Heroku:** https://heroku.com
- **Freenom:** https://freenom.com
- **Cloudflare:** https://cloudflare.com

---

## 🏆 Sucesso!

**Parabéns!** Seu Génesis Wine Hotel Virtual está agora online e acessível para estudantes de todo Moçambique! 🇲🇿

**🍷 "Transformando a educação em Moçambique, uma reserva virtual por vez!"** ✨