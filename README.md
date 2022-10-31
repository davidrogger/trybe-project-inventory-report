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
- O maior desafio dessa seção, nem do projeto em si foi entender melhor o uso dos padrões, por falta de experiencia.O uso de alguns padrões ainda soa confuso.

# Conclusão

- Por ja ter uma pouco mais de experiência com orientações a objetos em seções anteriores usando o typescript, foi bem interassante, coisas que não fazia sentido no typescript, agora soavam bem mais naturais que no primeiro contato na época.
- Agora é mais ter paciência e sempre que cabivel, tentar adotar o uso de orientação a objetos e o uso de projeto, por questão de treinamento mesmo, assim como o solid, tenho uma jornada para aplicar no meu código o uso desses conceitos.

# Iniciando o Projeto Report Inventory.

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
Após o container "levantar" basta acessar a url: `http://localhost:5000/`

</details>

</details>
