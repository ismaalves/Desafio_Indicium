# Desafio Técnico - Ciência de Dados - Indicium

Este repositório contém a solução para o desafio técnico do processo seletivo do programa LIGHTHOUSE da Indicium Tech. O desafio consiste em desenvolver uma estratégia de precificação para uma plataforma de aluguéis temporários em Nova York. A descrição completa pode ser encontrada [aqui](Descrição.md).  

Para abordar o problema, foi realizada uma [análise exploratória de dados](EDA.ipynb) (EDA) com o objetivo de compreender as principais características do [dataset](Data/teste_indicium_precificacao.csv). Em seguida na etapa de [modelagem preditiva](Predictive_Modeling.ipynb), foram testados diversos modelos preditivos, e o mais eficiente foi selecionado como solução final.  

A abordagem adotada consiste na construção de um modelo voltado para a precificação de aluguéis com valores mais próximos da média do mercado. Isso porque a precificação de aluguéis de alto valor apresenta características particulares que justificam seu tratamento como um problema à parte.  

## Como executar  

Para rodar o projeto, é necessário ter **Python 3.12.8** instalado em sua máquina.  

### 1. Clonar o repositório  

Abra o terminal e execute:  

```bash
git clone https://github.com/ismaalves/Desafio_Indicium.git
cd Desafio_Indicium
```

### 2. Criar e ativar um ambiente virtual  

Crie o ambiente virtual dentro da pasta do projeto:  

```bash
python -m venv venv
```

Ative o ambiente virtual:  

- **Windows (cmd/PowerShell)**:  

    ```powershell
    venv\Scripts\activate
    ```

    *Caso tenha problemas, tente:*  

    ```powershell
    Set-ExecutionPolicy Unrestricted -Scope Process
    venv\Scripts\Activate
    ```

- **macOS/Linux**:  

    ```bash
    source venv/bin/activate
    ```

### 3. Instalar dependências  

Com o ambiente virtual ativado, execute:  

```bash
pip install -r requirements.txt
```

### 4. Executar o script  

Execute o script principal:  

- **Windows (cmd/PowerShell)**:  

    ```powershell
    python .\Predict.py --data Data\test_data.csv
    ```

- **macOS/Linux**:  

    ```bash
    python ./Predict.py --data Data/test_data.csv
    ```
**Importante**: Ao executar o script com um arquivo de dados diferente, certifique-se de que ele tem as mesmas colunas de [teste_indicium_precificacao.csv](Data/teste_indicium_precificacao.csv).

## Como carregar o modelo:

Para uma execução alternativa, o modelo desenvolvido e o scaler utilizado podem ser carregados assim:

```
model = joblib.load('Saved_Models/LGBM_model.pkl')
scaler = joblib.load('Saved_Models/scaler.pkl')
```
---
