# Desafio Nível 1 — PDV com Descontos

## 1. Descrição do projeto

Este projeto consiste em um sistema de Ponto de Venda (PDV) desenvolvido em Python. O programa calcula descontos nas compras de acordo com a idade do cliente e o valor da compra.

## 2. Regras de desconto

- Clientes com 65 anos ou mais recebem 20% de desconto.
- Quando o valor da compra, após o desconto por idade, fica acima de R$ 100,00, é aplicado mais 10% de desconto sobre esse valor.
- O programa permite registrar várias compras até que o usuário digite 0.
- Valores negativos para a compra ou para a idade são considerados inválidos.
- Ao finalizar, o programa apresenta a quantidade de compras, o total bruto, o total de descontos e o total final.

## 3. Como executar o programa

1. Instale o Python no computador.
2. Abra a pasta do projeto no VS Code.
3. Abra o terminal do VS Code.
4. Execute o seguinte comando:

```bash
python pdv.py
```

5. Digite o valor da compra e a idade do cliente conforme solicitado.
6. Para encerrar o registro de compras, digite 0 no campo do valor da compra.

## 4. Casos de teste

A tabela apresenta os dez casos de teste previstos para verificar os cálculos do sistema.

| Nº | Valor da compra | Idade | Valor final esperado |
|---:|---:|---:|---:|
| 1 | R$ 50,00 | 30 | R$ 50,00 |
| 2 | R$ 100,00 | 30 | R$ 100,00 |
| 3 | R$ 80,00 | 65 | R$ 64,00 |
| 4 | R$ 100,00 | 70 | R$ 80,00 |
| 5 | R$ 125,00 | 70 | R$ 100,00 |
| 6 | R$ 200,00 | 30 | R$ 180,00 |
| 7 | R$ 101,00 | 30 | R$ 90,90 |
| 8 | R$ 200,00 | 65 | R$ 144,00 |
| 9 | R$ 1.000,00 | 80 | R$ 720,00 |
| 10 | R$ 200,00 | 64 | R$ 180,00 |

**Observação:** os valores da tabela são os resultados esperados conforme as regras de desconto do sistema.

## 5. Tecnologias utilizadas

- Linguagem de programação Python.
- Editor de código Visual Studio Code.
- Git e GitHub para controle de versão e armazenamento do projeto.

## 6. Autor

Marlon Andre

Projeto desenvolvido para o Desafio Nível 1 — PDV com Descontos.