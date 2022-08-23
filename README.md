# Data - Gerenciador e manipulador de datas

<div style="display:flex; flex-wrap:wrap">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat" alt="License Shield" style="padding:2px">
  <img src="https://img.shields.io/badge/python-v.310-blue?style=flat&logo=" alt="Language and version" style="padding:2px">
</div>

## 🎯 Propósito
O objetivo aqui é desenvolver um script com funções de gerenciamento e manipulação de datas. _Ainda em desenvolvimento_

## 🧠 Experiência/Motivação
Como o Python é muito dinâmico e possui recursos que auxiliam a reduzir linhas de código na construção de iterações, busquei testar meus conhecimentos e aplicar a lógica para desenvolver um código enxuto. 

Inicialmente, esse projeto começou como uma reflexão durante o verificador de CPF (outro projeto meu). Além disso esse script pode ser utilizado como recurso em aplicações futuras, por se tratar de algo muito comum no dia-a-dia.

## ✍ Como começar
Ainda em desenvolvimento, o script apresenta as funções ```gerar_data()```, ```verificar_ano_bissexto()``` e ```verificar_data()``` com propósitos literais, as funções realizam:

* ```gerar_data()``` - retorna uma data válida com valores do tipo _int_ para  **dia, mês** e **ano**.
* ```verificar_ano_bissexto()``` - retorna um texto informando se o ano  é bissexto ou não.
* ```verificar_data()``` - retorna um texto informando se a data é válida ou não e, dependendo da data passada como parâmetro, identifica onde está o erro.
* ```verificador_dia_semana()``` - **_em desenvolvimento_** - carrega o calendário gregoriano para memória e a partir dele verifica onde se encaixa a data informada como parâmetro, retornando o dia da semana.