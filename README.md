# Votos Deputados Federais 📩
Scraper de votos dos deputados federais, criado durante o Workshop: Os Primeiros Passos na Raspagem de Dados.

## Para acessar o código localmente 🏠

É possivel ter uma cópia do código como ele está atualmente fazendo o seguinte comando no terminal:
```
    git clone https://github.com/emys-alb/votos-deputados.git
```

Caso você queira fazer algum acrescimo ou alteração no código, é necessário fazer um fork (explicação sobre o que isso significa nesse [link](https://pt.stackoverflow.com/questions/143458/o-que-essas-palavras-significam-no-git-github-fork-clone-track)).

## Para rodar o projeto 💿
Primeiro passo é entrar na pasta do projeto:
```
cd votos-deputados/
```
### Criar uma venv do python 📦🐍
- Por que fazer isso? 😕
    
    Ao criar um ambiente virtual dentro do seu projeto, você isola as dependencias do seu projeto para um único lugar, e assim evita problemas com versionamento. 

    Mais informações nesse [link](https://docs.python.org/pt-br/3/tutorial/venv.html).

### Instalar as dependencias ⬇️

```
pip install requirements.txt
```

## Para gerar um csv:
```python
cd {estado do deputado}/
scrapy runspider {nome do arquivo python}
```

# Recomendações para contribuir
- Em caso de dúvida, abra uma issue.
- A estrutura do projeto é:
    - Estados > Nome-Sobrenome.py (Do deputado desse estado)
- Se for sua primeira PR, [leia esse tutorial](https://www.digitalocean.com/community/tutorials/como-criar-um-pull-request-no-github-pt) e Good Hacking 😉