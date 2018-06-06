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

1. **Commit**: Commits somente devem ser realizados em casos de correção de bugs, adição de novas funçoes ao programa, aprimoramento de funcionalidades ou criação de arquivos necessários ao projeto. Cada commit deve possuir uma mensagem objetiva e clara, especificando qual foi a alteração para o restante da equipe de desenvolvimento.Nesse contexnto, a mensagem deve ser composta pela descrição de qual é objetivo do commit aliado a funcionalidade alvo em concordancia ao backlog, exemplos: 'Incluindo funcionalidades RF-X e/ou RF-Y', 'Aprimorando funcionalidades RF-X e/ou RF-Y' e 'Fix das funcionalidades RF-X e/ou RF-Y'.Tags devem ser utilizadas em commits que descrevem uma finalização completa de funcionalidades, objetivando melhor organização do projeto sobre o que foi feito. Logo, tags devem ser descritas em relação as funcionalidades descritas.

2. **Branch**: Existem dois tipos de branches sem citar a master. Branch de teste, que representa a branch em que as funcionalidades commitadas passam por testes, formalizando conclusões sobre a necessidade de correções,  se a funcionalidade desenvolvida acrescenta algo ao sistema ou se está de acordo com os requesistos documentados no backlog. Branch da iteracão, que possui um backup da master, é nela em que as funcionalidades criadas e testadas são integradas ao restante do sistema, observando qualquer incoerência ou conflito com o que já foi desenvolvido e suficientemente testado. 

3. **Master**: Na master estará localizado a ultima versão estável do sistema. A merge é protegida, portanto, com exceção do dono do projeto, commits diretamente na merge são bloqueados e devem passar por uma revisão de código por parte do dono do projeto. A master armazena o código que será referenciando na baseline do sistema.
