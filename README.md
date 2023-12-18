Análise Exploratória das Aeronaves Registradas pela ICAO
==============================

<img src="icao_photo.png" alt="ICAO Logo" width = 500>

O registro de aeronaves é um código alfanumérico de dois, três ou quatro caracteres que designa cada tipo de aeronave (e alguns subtipos) que pode aparecer no planejamento de voo. Esses códigos são definidos pela Organização da Aviação Civil Internacional (ICAO) e pela Associação Internacional de Transporte Aéreo (IATA). Os códigos ICAO são publicados no documento ICAO 8643 Aircraft Type Designators e são usados ​​pelo controle de tráfego aéreo e operações aéreas, como planejamento de voo. Embora os registros ICAO sejam usados ​​para distinguir entre tipos e variantes de aeronaves que possuem diferentes características de desempenho que afetam o ATC, os códigos não diferenciam entre características de serviço (variantes de passageiros e de carga do mesmo tipo/série terão o mesmo código ICAO).

Apesar de não se tratar de uma amostra da população de aeronaves, muitas informações relevantes do cenário aeronáutico podem ser extraídas deste banco de dados, pois o registro é um passo essencial ao se produzir uma aeronave, revelando tendências de mercado.

### Bibliotecas e Softwares Utilizados:
**Raspagem de dados:** *Selenium* <br> 
**Banco de Dados:** *MySQL* <br> 
**Visualização e Análise de Dados:** *Pandas*, *PowerBI* <br>



Organização do Projeto
------------

    ├── LICENSE
    ├── README.md   
    ├── data
    │   └── raw.csv        <- Dados Raspados.
    │
    ├── references         <- Dicionários, Manuais e Referências Utilizadas.
    │
    ├── reports            <- Relatório.
    │
    ├── requirements.txt   <- Requerimento
    │
    └── src                <- Código Fonte.
       │
       ├── data           
       │   └── make_dataset.py    <- Raspagem de dados
       │
       ├── db_connection      
       |   ├── create_database.py <- Criar Banco de Dados.
       │   └── create_tables.py   <- Criar e Manipular Tabelas.
       │
       └── visualization 
           └── dashboard.pbix     <- Dashboard em Power BI.
    


--------

<p><small>Projeto baseado no <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
