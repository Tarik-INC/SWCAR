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
  
* Pasta **documentos** onde ficarão armazenados documentos criados durante a iteração do desenvolvimento de software.
  * Subpasta **requesitos**, onde é organizados os arquivos referente aos requesitos levantados do projeto.
   
##  Política de uso do git

1. **Commit**: Commits somente devem ser realizados em casos de correção de bugs, adição de novas funçoes ao programa, ou criação de arquivos necessários ao projeto.

2. **Branch**: Branches devem ser criadas objetivando o densenvolvimento de uma nova funcionalidade experimental do sistema, logo o desenvolvimento deve ser realizado em uma branch separada e seu código suficientemente testado antes de realizar a merge. Convencionalmente, branches devem possuir o número do desenvolvedor seguido por um hífen de qual funcionalidade está sendo testada.

3. **Merge**: Merge entres branches ou a merge entre uma branch e a master devem ocorrer apenas em situaçoes em que a nova funcionalidade está satisfatoriamente testada e pode ser integrada ao fluxo em que a branch foi ramificada.

4. **Master**: Na merge estará localizado a ultima versão funcional do sistema. A merge é protegida, portanto, com exceção do dono do projeto, commits diretamente na merge são bloqueados e devem passar por uma revisão de código por parte do dono do projeto.
