# https://ewerton.com.br
## Clonando o projeto
Reposit�rio com os arquivos utilizados para a constru��o do website. Para rod�-lo numa m�quina local:
 **1.** Clone o projeto:
```bash
git clone git@github.com:EwertonES/ewerton-com-br.git
```
 **2.** Instale as depend�ncias:
```bash
pip install -r requirements.txt
```
**3.** Abra o terminal na pasta do projeto e rode o arquivo main.py:
```bash
python main.py
```
## Arquivos
```bash
|   .dockerignore # Arquivos que n�o ser�o colocados na imagem
|   .env # Define se o webserver vai rodar como dev ou prod
|   .gitignore # Arquivos que n�o ser�o upados pro GitHub
|   Dockerfile # Instru��es para a cria��o da imagem
|   main.py # Arquivo principal, usado para iniciar o servidor
|   README.md # Esse arquivo que voc� est� lendo agora
|   requirements.txt # Depend�ncias no Python para rodar o c�digo
|   
+---static # Arquivos que s�o servidos ao cliente
|   |   favicon.ico # �cone do site
|   |   robots.txt # Instru��es para indexadores
|   |   sitemap.xml # Links para indexadores
|   |   
|   +---documents # Documentos armazenados
|   |       cv_ewerton_en.pdf # Curr�culo em ingl�s
|   |       cv_ewerton_pt.pdf # Curr�culo em portugu�s
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
\---templates # P�ginas do site
        about.html # Sobre mim
        contact.html # Contato
        home.html # P�gina Inicial
        jobs.html # Vagas
        layout.html # Base para todas as p�ginas
        raw.html # Endpoint para enviar emails
        services.html # Servi�os que oferto
```