# 💳 Sistema Bancário em Python (POO) - Luizalabs Python

Bootcamp da dio com o objetivo introdutorio do Python no backend, fundamentos de estrutura de dados em Python.

Este projeto foi desenvolvido como parte de um desafio técnico com o objetivo de aplicar conceitos de **Programação Orientada a Objetos (POO)** em Python, simulando operações de um sistema bancário com foco em organização, reutilização de código e regras de negócio.

---

## 🚀 Funcionalidades

* ✔️ Cadastro de clientes (Pessoa Física)
* ✔️ Estrutura preparada para Pessoa Jurídica
* ✔️ Criação de contas correntes
* ✔️ Seleção de contas por cliente
* ✔️ Depósitos
* ✔️ Saques com regras de limite
* ✔️ Exibição de extrato detalhado
* ✔️ Listagem de contas

---

## 🧠 Conceitos aplicados

* Programação Orientada a Objetos (POO)

  * Herança (Cliente → PessoaFisica / PessoaJuridica)
  * Encapsulamento (uso de atributos privados e @property)
  * Polimorfismo (uso de classes base como Cliente e Transacao)
* Classes abstratas (`ABC`)
* Métodos especiais (`__init__`, `__str__`)
* Uso de propriedades (`@property`)
* Tipagem com type hints
* Separação entre lógica de negócio e interação com usuário

---

## 🏗️ Estrutura do sistema

O sistema foi modelado utilizando classes que representam entidades reais de um banco:

* **Cliente**

  * Classe base para clientes
  * Responsável por gerenciar contas e transações

* **PessoaFisica**

  * Cliente com CPF, nome e data de nascimento

* **PessoaJuridica**

  * Estrutura preparada para suportar clientes empresariais

* **Conta**

  * Classe base para contas bancárias
  * Gerencia saldo e histórico

* **ContaCorrente**

  * Implementa regras como limite de saque e quantidade máxima de saques

* **Transacao (abstrata)**

  * Base para operações financeiras

* **Saque / Deposito**

  * Implementações concretas de transações

* **Historico**

  * Armazena todas as operações realizadas com data, tipo e valor

---

## ⚙️ Regras de negócio

* Saques possuem limite de valor por operação
* Existe limite de quantidade de saques por conta
* Apenas valores positivos são aceitos
* Todas as transações são registradas no histórico
* Cada cliente pode possuir múltiplas contas
* O usuário pode selecionar qual conta deseja utilizar

---

## ▶️ Como executar

1.Clone o repositório:

```bash
git clone https://github.com/CaioSilvaCsv/Luizalabs_Backend_python/tree/desafio
```

2.Acesse a pasta:

```bash
cd Luizalabs_Backend_python
```

3.Execute o programa:

```bash
python desafio.py
```

---

## 🖥️ Interface

O sistema funciona via terminal com menu interativo:

```bash
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo usuário
[0] Sair
```

---

## 🔮 Melhorias futuras

* Persistência de dados (arquivo ou banco de dados)
* Implementação completa de Pessoa Jurídica
* Criação de API REST (Flask ou FastAPI)
* Interface gráfica
* Validação de CPF/CNPJ

---

## 📌 Observações

O projeto foi estruturado visando evolução futura para uma arquitetura mais robusta, como APIs REST, mantendo separação de responsabilidades e uso de abstrações.

---

## 👨‍💻 Autor

Desenvolvido por Caio da Silva
