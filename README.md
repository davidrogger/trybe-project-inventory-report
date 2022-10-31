# Sobre o Projeto 

- Segundo projeto do modulo de Ciências da Computação da trybe.
- Desenvolvido classes usando o tema da seção 2, que aborda, orientação a objetos, e padrão de projetos(Strategy, iterator e decorator).
- Desenvolvido classes, com habilidade de leitura de arquivos CSV, JSON e XML, gerando uma relatório dinâmico, que podia ser simples ou completo.
- Ao finalizar o projeto é possível após a instalação dos módulos criados nele `pip install .`, chamar o metodo para gerar um relatório por linha de comando:

<details>
  <summary>
    <strong>
      :telescope: Amostra da linha de comando:
    </strong>
  </summary>

  ## Comando:
  ```
  inventory "caminho" "tipo de relatório
  ```

  ## Exemplo Relatório Simples:
  ```
  inventory_report "inventory_report/data/inventory.csv" "simples"
  ```
  ## Resultado:
  ```
  Data de fabricação mais antiga: 2020-09-06
  Data de validade mais próxima: 2023-09-17
  Empresa com mais produtos: Target Corporation
  ```

  ## Exemplo Relatório Completo
  ```
  inventory_report "inventory_report/data/inventory.csv" "completo"
  ```
  ## Resultado:
  ```
  Data de fabricação mais antiga: 2020-09-06
  Data de validade mais próxima: 2023-09-17
  Empresa com mais produtos: Target Corporation
  Produtos estocados por empresa:
  - Target Corporation: 4
  - Galena Biopharma: 2
  - Cantrell Drug Company: 2
  - Moore Medical LLC: 1
  - REMEDYREPACK: 1
  ```


</details>

#

# Tecnologias e ferramentas usadas 🛠

![Python](https://img.shields.io/badge/-Python-%23F7DF1C?style=flat-square&logo=python)
![Pytest](https://img.shields.io/badge/-Pytest-fff?style=flat-square&logo=pytest)
![Docker](https://img.shields.io/badge/-Docker-003f8c?style=flat-square&logo=docker&logoColor=fff)


# Desafios

- Foram de pesquisar as novas sintaxes e "ferramentas" para nova linguagem adotada e adaptalidade com algumas funcionalidades do python, como importação de modulos.
- O maior desafio dessa seção, nem do projeto em si, foi de entender melhor o uso dos padrões(Iterator), por falta de experiencia.O uso de alguns padrões ainda soa confuso.

# Conclusão

- Por ja ter uma pouco mais de experiência com orientações a objetos em seções anteriores usando o typescript, foi bem interassante, coisas que não fazia sentido no typescript, agora soavam bem mais naturais que no primeiro contato na época.
- Agora é mais ter paciência e sempre que cabivel, tentar adotar o uso de orientação a objetos e o uso de padrão de projetos, por questão de treinamento, assim como o solid, tenho uma jornada para aplicar e entender o uso no código.

# Iniciando o Projeto Inventory Report.

Importante: seguir a ordem apresentada a baixo, para o funcionamento.

<details>
  <summary>
    <strong>
      ⚠️ Configurações mínimas para execução do projeto
    </strong>
  </summary>

   - Sistema Operacional Distribuição Unix
 - Python versão >= 3.8.10 

</details>

<details>
  <summary>
    <strong>
      ⚠️ Inicie o docker-compose
    </strong>
  </summary>

Para ver a aplicação funcionando basta iniciar o docker compose, basta esta na pasta do repositório tendo o requisitos conforme informado na aba de requisitos, e iniciar o docker com `docker-compose up -d`

Após levantar o container para interagir com os comandos de linha, é necessário acessar o container usando o comando a seguir, `docker exec -it project-inventory-report bash`, dentro do terminal do container é necessário entrar no ambiente virtual do python com o comando, `source .venv/bin/activate`, após esse comando o inicio do termina deve aparecer com o `(.venv)` antes do root, deve-se usar o comando `pip install .` para instalar o inventory_report, após isso basta usar o comando apresentado na parte de amostra e determinar o arquivo que deseja importar, possuimos 3 arquivos padrões, csv, json e xml.



</details>

</details>

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos solicitados durante o desenvolvimento do projeto
    </strong>
  </summary>

 
### Resultado por requisito
*Nome* | *Avaliação*
--- | :---:
1 - Deve criar um teste para o novo produto com todos os atributos corretamente preenchidos | :heavy_check_mark:
2 - Criar um teste que garanta o retorno padrão de um objeto Product deve ser um relatório sobre ele | :heavy_check_mark:
3.1 - O método generate da classe SimpleReport deve retornar todas informações do relatório simples | :heavy_check_mark:
3.2 - O método generate da classe SimpleReport deve retornar o formato correto do relatório simples | :heavy_check_mark:
4 - O método generate da classe CompleteReport deve retornar todas informações do relatório completo | :heavy_check_mark:
5 - Ao importar um arquivo csv, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
6 - Ao importar um arquivo JSON, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
7 - Ao importar um arquivo XML, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
8 - As classes estratégicas CsvImporter, JsonImporter e CsvImporter devem retornar os dados dos produtos em uma lista | :heavy_check_mark:
9 - Deve criar um teste garantindo que retornar o relatório devidamente colorido | :heavy_check_mark:
10.1 - Será validado que a instancia de InventoryRefactor é iterável (Iterable) | :heavy_check_mark:
10.2 - Será validado que é possível iterar o primeiro item da lista usando csv | :heavy_check_mark:
10.3 - Será validado que é possível iterar o primeiro item da lista usando json | :heavy_check_mark:
10.4 - Será validado que é possível iterar o primeiro item da lista usando xml | :heavy_check_mark:
10.5 - Será validado que é possível receber duas fontes de dados sem sobrescrita | :heavy_check_mark:
10.6 - Será validado que não é possível enviar arquivo inválido | :heavy_check_mark:
11.1 - Será validado que o menu importa um arquivo csv e gera um report simples | :heavy_check_mark:
11.2 - Será validado que o menu importa um arquivo csv e gera um report completo | :heavy_check_mark:
11.3 - Será validado que o menu importa um arquivo json e gera um report simples | :heavy_check_mark:
11.4 - Será validado que o menu importa um arquivo json e gera um report completo | :heavy_check_mark:
11.5 - Será validado que o menu importa um arquivo xml e gera um report simples | :heavy_check_mark:
11.6 - Será validado que o menu importa um arquivo xml e gera um report completo | :heavy_check_mark:
11.7 - Será validado que enviar argumentos faltantes irá gerar um erro | :heavy_check_mark:


</details>
