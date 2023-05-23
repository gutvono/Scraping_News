# Boas-vindas ao repositório do projeto `Scraping News`!

🌱 O projeto tem como principal objetivo estudar raspagem de dados, utilizando Python e algumas bibliotecas como Selenium, Beautiful Soup e Parsel. Neste mini-projeto em específico, foi utilizada uma página de notícias para a realização do scraping, e o banco MongoDB para armazenamento das informações encontradas.

<img alt="work" src="https://miro.medium.com/v2/resize:fit:640/1*nHfayfdmxAApbg84iMrJqQ.gif" width="300px">

# Contexto geral:

<details>
    <summary>🗃️ <strong>Arquivos e pastas feitas por mim</strong></summary><br />
    <li> 📁 Tudo que está dentro de: <strong>/tech_news</strong>.</li>
    <li> Os demais arquivos foram feitos pela escola que elaborou o projeto.</li>
</details>

<details>
    <summary>🧰 <strong>Ferramentas</strong>, <strong>linguagens</strong> e respectivas <strong>funções</strong> utilizadas:</summary>
    <li> <i>Python</i> (linguagem);</li>
    <li> <i>PyMongo / MongoDB</i> (banco de dados);</li>
    <li> <i>venv e Docker</i> (ambiente);</li>
    <li> <i>Parsel</i> (raspagem de dados);</li>
</details>

<details>
    <summary>🚀 <strong>Como rodar o projeto</strong></summary>
    Neste projeto foi utilizado o <i>Docker</i> e o <i>venv</i>, para que não haja problemas com os softwares locais da máquina, além de ter um <i>ambiente isolado</i> para trabalhar.
    <br>

  1. **Criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **Ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **Instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  4. **Criar o container para o banco de dados**

  ```bash
  $ docker-compose up -d mongodb
  ```

Quando precisar desativar o ambiente virtual, execute o comando "_deactivate_".
</details>

# Observações
Como sempre, um projeto nunca termina de fato. Sempre haverão **melhorias** para serem aplicadas.

<details>
    <summary><strong>Futuro potencial/melhorias</strong></summary>
    <li>Melhorias estruturais seguindo alguns design de software como SOLID, POO, DDD, etc;</li>
    <li>Implementar testes unitários;</li>
    <li>Expandir alguns trechos de codigos para uma melhor manutenção e entendimento.</li>
<br>
    Essas são apenas algumas ideias de melhorias e adição de novas features!
</details>

Deixe seu [Feedback](https://53tqbjd4mxw.typeform.com/to/gmWFoZYZ)!