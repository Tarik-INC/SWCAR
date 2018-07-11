# SWCAR
### Sistema Web de Controle de Atividades e Recompensas
Um projeto apresentado como parte integrante a disicplina GCC188 - Engenharia de software ofertada pelo Departamento de Ciência da Computação localizado na Universidade Federal de Lavras.

## Tecnologias utilizadas
- Back-end: framework Django. Django é uma ferramenta open-source, sendo a escolha do grupo por possir uma comunidade influente e ativa, possuindo vários tutorias e exemplos, e ser de fácil aprendizado e manuseio e para programadores python, ajudando a abstrair vários detalhes no desenvolvimento web. 
- Front-end: Bootstrap, html, css e javascript.O Boostrap é uma ferramenta web caracterizada como um framework front-end, que possui padronizações que auxiliam no desenvolvimento de sites esteticamente agradáveis e de boa usabilidade, além de contar com recursos visuais pré-construídos que podem ser facilmente integrado ao projeto e de auxiliar na estrutura dos layouts. Junto ao bootstrap poderão ser utilizados as três linguaguens web principais, o html, css e o javascript, na criação e aprimoramento de  recursos visuais. 

## Estrutura do Projeto

A estrutura do projeto se apresenta como a seguinte:

```
documentos/
  requesitos/
src/
  manage.py
  swcar/
    __init__.py
    settings.py
    urls.py
    wsgi.py
public/
      index.html
      pages/ 
```
Essas pastas representam:
* Pasta **src** onde serão inseridos arquivos integrantes do back-end.
  * Subpasta **swcar** de arquivos criados pelo framework Django na inicialização do projeto.
  
* Pasta **public** onde são armazenadoas as arquivos de interface gráfica disponível ao usuário.
  * Subpasta **pages**, onde são colocadas as páginas html, com exceção da primeira, e arquivos css e javascript. Index é a primeira página presentada pelo sistema.
  
* Pasta **documentos** onde ficarão armazenados as documentações criadas durante o desenvolvimento de software.
  * Subpasta **requesitos**, onde é organizados os arquivos referente aos requesitos levantados do projeto.
   
##  Política de uso do git

1. **Commit**: Commits devem representar funcionalidades descritas através dos *issues* organizadas no backlog. Cada commit pode ser divido em tres subgrupos de forma a padronizar seu uso: 
* **Conclusão de uma *issue***: A mensagem do commit deve possuir  uma das seguintes  palavras chaves *close*, *closes*, *closed*, *resolve*, *resolves*, *resolved*  seguido do hastag e número da issue correspondente. 
* **Fix de uma funcionalidade**: A mensagem  do commit deve possuir uma das seguintes palavras chaves *fix*, *fixes*, *fixed* seguido do hastag e número da issue correspondente.
* **Conclusão parcial de uma *issue***: A mensagem  do commit deve ser constituida da plavra chave *parcial* seguida do hastag e o número da issue correspondente.

2. **Branch**: Existem dois tipos de branches sem citar a master. Branch de teste, que representa a branch em que as funcionalidades commitadas passam por testes, formalizando conclusões sobre a necessidade de correções,  se a funcionalidade desenvolvida acrescenta algo ao sistema ou se está de acordo com os requesistos documentados no backlog. Branch da iteracão, que possui um backup da master, é nela em que as funcionalidades criadas e testadas são integradas ao restante do sistema, observando qualquer incoerência ou conflito com o que já foi desenvolvido e suficientemente testado. 

3. **Master**: Na master estará localizado a ultima versão estável do sistema. A merge é protegida, portanto, com exceção do dono do projeto, commits diretamente na merge são bloqueados e devem passar por uma revisão de código por parte do dono do projeto. A master armazena o código que será referenciando na baseline do sistema.

## Padrões de codificação

**Python-Django**:
* Todo código deverá ser escrito em português.
* Documentação(Docstrings) criados por menbros da equipe devem estar em português, salvo a documentação criada pelo django, que auxilia o densevolvimento, que se apresenta em inglês.
* Todos os nomes de classes devem começar por maiúsculo, seguindo o padrão CamelCase e representar um                           substantivo.
* Todos os nomes de variáveis e metódos devem começar por minúsculo, seguir o padrao snake_case, com as variáveis               representando um susbtantivo e metódos uma ação verbal.
* O código deve ser idententado utilizando uma tab segundo a recomendação do [pylint](https://www.pylint.org/).

**HTML**:
* Todos os documentos HTML devem usar um tab  para recuo e não deve haver nenhum espaço em branco à direita.
* Toda tag de fechamento devem possuir o mesmo recuo da tag  de abertura, facilitando a organização de código.
* todos os atributos devem  ser descritos com aspas duplas.
* Todos os documentos devem estar usando o tipo de documento HTML5 e o elemento <html> deve ter um atributo "lang". O <head>   também deve incluir, no mínimo, meta tags "viewport" e "charset".
* As classes devem idealmente ser usadas apenas como meios de estilo(CSS). Se você precisar incluir dados adicionais no documento HTML, por exemplo, para passar dados para JavaScript, os atributos do tipo "data"  deverão ser usados
  


