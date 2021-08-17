# https://ewerton.com.br
## Clonando o projeto
Repositório com os arquivos utilizados para a construção do website. Para rodá-lo numa máquina local:
 **1.** Clone o projeto:
```bash
git clone git@github.com:EwertonES/ewerton-com-br.git
```
 **2.** Instale as dependências:
```bash
pip install -r requirements.txt
```
**3.** Abra o terminal na pasta do projeto e rode o arquivo main.py:
```bash
python main.py
```
## Arquivos
```bash
|   .dockerignore # Arquivos que não serão colocados na imagem
|   .env # Define se o webserver vai rodar como dev ou prod
|   .gitignore # Arquivos que não serão upados pro GitHub
|   Dockerfile # Instruções para a criação da imagem
|   main.py # Arquivo principal, usado para iniciar o servidor
|   README.md # Esse arquivo que você está lendo agora
|   requirements.txt # Dependências no Python para rodar o código
|   
+---static # Arquivos que são servidos ao cliente
|   |   favicon.ico # Ícone do site
|   |   robots.txt # Instruções para indexadores
|   |   sitemap.xml # Links para indexadores
|   |   
|   +---documents # Documentos armazenados
|   |       cv_ewerton_en.pdf # Currículo em inglês
|   |       cv_ewerton_pt.pdf # Currículo em português
|   |       translation_flyer.pdf # Flyer que envio aos potenciais clientes
|   |       
|   +---icons # Emojis
|   |       brazil.svg
|   |       clock.svg
|   |       envelope.svg
|   |       
|   +---images # Fotos
|   |       cheese.webp # Eu no lab fazendo queijo
|   |       cmd.webm # Gif do cmd
|   |       logo.png # Logo do site maior
|   |       me.webp # Minha foto
|   |       translation_flyer.jpg # Flyer que envio aos clientes
|   |       translation_flyer.webp # Flyer que envio aos clientes
|   |       
|   +---js # JavaScript
|   |       jquery-3.6.0.min.js # Biblioteca jQuery
|   |       
|   \---styles # CSS
|           main.css
|           
\---templates # Páginas do site
        about.html # Sobre mim
        contact.html # Contato
        home.html # Página Inicial
        jobs.html # Vagas
        layout.html # Base para todas as páginas
        raw.html # Endpoint para enviar emails
        services.html # Serviços que oferto
```