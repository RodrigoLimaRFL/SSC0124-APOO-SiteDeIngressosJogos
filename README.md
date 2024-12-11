<!DOCTYPE html>
<html lang="en">
<body>
    <h1>SSC0124-APOO-SiteDeIngressosJogos</h1>
    <p>
        Projeto feito para disciplina SSC0124 - Análise e Projeto Orientado a Objetos, ministrada pela professora Lina Garcés.
    </p>
    <p>
        Este repositório consiste na aplicação prática do projeto desenvolvido em aula. Devido ao seu design baseado no padrão de arquitetura MVC, foi utilizado o framework Django na linguagem Python.
    </p>

    <h2>Integrantes</h2>
    <ul>
        <li>Arthur Ramos</li>
        <li>Henrique Drago</li>
        <li>Henrique Sekido</li>
        <li>Rodrigo Lima</li>
    </ul>

  <h2>Passo a passo para compilar o código:</h2>
  <ol>
      <li>
          <strong>Instalar Python</strong><br>
          Instale Python a partir deste link: 
          <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>
      </li>
      <li>
          <strong>Criar ambiente virtual</strong><br>
          Se necessário: 
          <pre><code>sudo apt-get install python3-venv</code></pre>
          Depois, criar de fato o venv: 
          <pre><code>python3 -m venv .venv</code></pre>
          Para ativar: 
          <pre><code>source .venv/bin/activate</code></pre>
          Por fim, selecione na paleta de comandos o interpretador Python <code>./venv</code>.
      </li>
      <li>
          <strong>Instalar Django</strong><br>
          Rode no terminal: 
          <pre><code>python -m pip install --upgrade pip
          python -m pip install django</code></pre>
      </li>
      <li>
          <strong>Clonar o Repositório</strong><br>
          <pre><code>git clone https://github.com/RodrigoLimaRFL/SSC0124-APOO-SiteDeIngressosJogos
          cd SSC0124-APOO-SiteDeIngressosJogos</code></pre>
        </li>
        <li>
            <strong>Instalar o setuptools</strong><br>
            <pre><code>pip install setuptools</code></pre>
        </li>
        <li>
            <strong>Rodar o Servidor</strong><br>
            <pre><code>python manage.py runserver</code></pre>
        </li>
    </ol>
</body>
</html>
