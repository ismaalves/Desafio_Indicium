# Desafio

## Drescição

Você foi alocado(a) em um time da Indicium que está trabalhando atualmente junto a um cliente no processo de criação de uma plataforma de aluguéis temporários na cidade de Nova York. Para o desenvolvimento de sua estratégia de precificação, pediu para que a Indicium fizesse uma análise exploratória dos dados de seu maior concorrente, assim como um teste de validação de um modelo preditivo.

**Seu objetivo é desenvolver um modelo de previsão de preços a partir do dataset oferecido, e avaliar tal modelo utilizando as métricas de avaliação que mais fazem sentido para o problema.** O uso de outras fontes de dados além do dataset é permitido (e encorajado). Você poderá encontrar em anexo um dicionário dos dados.


## Entregas

1. Faça uma análise exploratória dos dados (EDA), demonstrando as principais características entre as variáveis e apresentando algumas hipóteses de negócio relacionadas. Seja criativo!
2. Responda também às seguintes perguntas:
    * Supondo que uma pessoa esteja pensando em investir em um apartamento para alugar na plataforma, onde seria mais indicada a compra?
    * O número mínimo de noites e a disponibilidade ao longo do ano interferem no preço?
    * Existe algum padrão no texto do nome do local para lugares de mais alto valor?
3. Explique como você faria a previsão do preço a partir dos dados. Quais variáveis e/ou suas transformações você utilizou e por quê? Qual tipo de problema estamos resolvendo (regressão, classificação)? Qual modelo melhor se aproxima dos dados e quais seus prós e contras? Qual medida de performance do modelo foi escolhida e por quê?
4. Supondo um apartamento com as seguintes características: Qual seria a sua sugestão de preço?

```
{'id': 2595,
 'nome': 'Skylit Midtown Castle',
 'host_id': 2845,
 'host_name': 'Jennifer',
 'bairro_group': 'Manhattan',
 'bairro': 'Midtown',
 'latitude': 40.75362,
 'longitude': -73.98377,
 'room_type': 'Entire home/apt',
 'minimo_noites': 1,
 'numero_de_reviews': 45,
 'ultima_review': '2019-05-21',
 'reviews_por_mes': 0.38,
 'calculado_host_listings_count': 2,
 'disponibilidade_365': 355}
```

5. Salve o modelo desenvolvido no formato .pkl. 
6. A entrega deve ser feita através de um repositório de código público que contenha:
    * README explicando como instalar e executar o projeto
    * Arquivo de requisitos com todos os pacotes utilizados e suas versões
    * Relatórios das análises estatísticas e EDA em PDF, Jupyter Notebook ou semelhante conforme passo 1 e 2.
    * Códigos de modelagem utilizados no passo 3 (pode ser entregue no mesmo Jupyter Notebook).
    * Arquivo .pkl conforme passo 5 acima.
7. Um vídeo curto explicando o desenvolvimento de suas entregas deste desafio, como você planejou e executou as atividades propostas. O vídeo deverá ser entregue via link via Google Drive. Lembre-se de autorizar o acesso para "qualquer pessoa com o link".

Todos os códigos produzidos devem seguir as boas práticas de codificação.

## Prazo

* Você tem até 7 dias corridos para a entrega, contados a partir do recebimento deste desafio. O não cumprimento deste prazo implica na desclassificação do processo seletivo.
* A Indicium possui ferramentas avançadas de detecção de plágio e inteligência artificial. A utilização de IA implica na desclassificação do processo seletivo.
* Envie o seu relatório dentro da sua data limite para o email: selecao.lighthouse@indicium.tech
* O arquivo de entrega deve ser nomeado como: LH_CD_SEUNOME

Bom trabalho!

## Dicionário dos dados

A base de dados de treinamento contém 16 colunas. Seus nomes são auto-explicativos, mas, caso haja alguma dúvida, a descrição das colunas é:

`id` – Atua como uma chave exclusiva para cada anúncio nos dados do aplicativo

`nome` - Representa o nome do anúncio

`host_id` - Representa o id do usuário que hospedou o anúncio

`host_name` – Contém o nome do usuário que hospedou o anúncio

`bairro_group` - Contém o nome do bairro onde o anúncio está localizado

`bairro` - Contém o nome da área onde o anúncio está localizado

`latitude` - Contém a latitude do local

`longitude` - Contém a longitude do local

`room_type` – Contém o tipo de espaço de cada anúncio

`price` - Contém o preço por noite em dólares listado pelo anfitrião

`minimo_noites` - Contém o número mínimo de noites que o usuário deve reservar

`numero_de_reviews` - Contém o número de comentários dados a cada listagem

`ultima_review` - Contém a data da última revisão dada à listagem

`reviews_por_mes` - Contém o número de avaliações fornecidas por mês

`calculado_host_listings_count` - Contém a quantidade de listagem por host

`disponibilidade_365` - Contém o número de dias em que o anúncio está disponível para reserva
