# SWCAR
### Sistema Web de Controle de Atividades e Recompensas
Um projeto apresentado como parte integrante a disicplina GCC188 - Engenharia de software ofertada pelo Departamento de Ciência da Computação localizado na Universidade Federal de Lavras.

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
  
* Pasta **documentos** onde ficarão armazenados as documentações criados durante o desenvolvimento de software.
  * Subpasta **requesitos**, onde é organizados os arquivos referente aos requesitos levantados do projeto.
   
##  Política de uso do git

1. **Commit**: Commits somente devem ser realizados em casos de correção de bugs, adição de novas funçoes ao programa, ou criação de arquivos necessários ao projeto. Cada commit deve possuir uma mensagem objetiva e clara, especificando qual foi a alteração para o restante da equipe de desenvolvimento. Commits realizados na master devem possuir um funcionalidade já completa e totalmente testada.

# Em construção

2. **Branch**: Existem três tipos de branches. Branch da iterácão, que representa um backup da master, é nela que o merge de outras branches devem ser executados primeiramente para resolução de eventuais conflito, sendo depois realizados

3. **Merge**: Merge entres branches ou a merge entre uma branch e a master devem ocorrer apenas em situaçoes em que a nova funcionalidade está satisfatoriamente testada e pode ser integrada ao fluxo em que a branch foi ramificada.

4. **Master**: Na merge estará localizado a ultima versão estável do sistema. A merge é protegida, portanto, com exceção do dono do projeto, commits diretamente na merge são bloqueados e devem passar por uma revisão de código por parte do dono do projeto.
