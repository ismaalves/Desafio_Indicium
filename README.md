# Desafio Técnico - Ciência de Dados - Indicium

Este repositório contém a solução para o desafio técnico do processo seletivo do programa LIGHTHOUSE da Indicium Tech. O desafio consiste em desenvolver uma estratégia de precificação para uma plataforma de aluguéis temporários em Nova York. A descrição completa pode ser encontrada [aqui](Descrição.md).  

Para abordar o problema, foi realizada uma [análise exploratória de dados](EDA.ipynb) (EDA) com o objetivo de compreender as principais características do [dataset](Data/teste_indicium_precificacao.csv). Em seguida, foram testados diversos modelos preditivos, e o mais eficiente foi selecionado como a solução final.

## Como executar

Para a execução do código será necessário ter o Python instalado em sua máquina. A versão utilizada para o desenvolvimento foi a 3.12.8.

### Clonar o repositório

Abra o terminal na pasta que quiser clonar o repositório e execute:

```
git clone https://github.com/ismaalves/Desafio_Indicium.git
```

### Cirar e ativar um ambiente virtual

Excute no terminal:

```
python -m venv venv
```

Para ativar o ambiente virtual:

* No Windows:

    ```
    venv\Scripts\activate
    ```

* No macOS/Linux::

    ```
    source venv/bin/activate
    ```

### Instalar as bibliotecas necessárias

Com o ambiente virtual ativado, digite no terminal e aguarde a instalação:

```
pip install -r requirements.txt
```

### Executar o script Python

No terminal digite:

```
python X.py
```
