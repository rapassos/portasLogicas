# 🔌 Portas Lógicas em Python

> Implementação das principais portas lógicas digitais em Python, com saída via terminal — projeto educacional focado em fundamentos de lógica booleana e programação.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

---

## 🎯 Sobre o Projeto

Implementação em Python das sete portas lógicas fundamentais da eletrônica digital, com exibição dos resultados e tabelas verdade diretamente no terminal.

Desenvolvido para consolidar o entendimento de **lógica booleana** — base essencial para quem trabalha com infraestrutura, sistemas embarcados, redes e arquitetura de computadores.

---

## 🧮 Portas Implementadas

| Porta | Símbolo | Descrição |
|-------|---------|-----------|
| **AND** | A · B | Saída `1` somente se **todas** as entradas forem `1` |
| **OR** | A + B | Saída `1` se **pelo menos uma** entrada for `1` |
| **NOT** | Ā | **Inverte** o valor da entrada |
| **NAND** | A ⊼ B | Inverso do AND — saída `0` somente se todas as entradas forem `1` |
| **NOR** | A ⊽ B | Inverso do OR — saída `1` somente se todas as entradas forem `0` |
| **XOR** | A ⊕ B | Saída `1` se as entradas forem **diferentes** |
| **XNOR** | A ⊙ B | Saída `1` se as entradas forem **iguais** |

---

## 📸 Exemplo de Saída

```
Porta AND
a =  0  b =  0  => a AND b = 0
a =  0  b =  1  => a AND b = 0
a =  1  b =  0  => a AND b = 0
a =  1  b =  1  => a AND b = 1

Porta OR
a =  0  b =  0  => a OR b = 0
a =  0  b =  1  => a OR b = 1
a =  1  b =  0  => a OR b = 1
a =  1  b =  1  => a OR b = 1

Porta NOT
a = 0 => a NOT =  1
a = 1 => a NOT =  0

Porta NAND
a =  0  b =  0  => a NAND b = 1
a =  0  b =  1  => a NAND b = 1
a =  1  b =  0  => a NAND b = 1
a =  1  b =  1  => a NAND b = 0

... [demais portas]
```

> **Nota:** A tabela verdade completa ainda não está implementada no código — atualmente `testaPortas.py` executa testes individuais para cada combinação de entradas.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado

### Execução

```bash
# Clone o repositório
git clone https://github.com/rapassos/portasLogicas.git

# Entre na pasta
cd portasLogicas

# Execute o script de testes
python testaPortas.py
```

> O script `testaPortas.py` importa as funções de `portas.py` e executa uma bateria de testes para validar cada porta lógica.

---

## 📂 Estrutura do Projeto

```
portasLogicas/
├── portas.py         # Implementação das 7 portas lógicas (funções)
├── testaPortas.py    # Script de testes para validar cada porta
└── README.md
```

**Arquitetura:**
- `portas.py` — contém as funções puras de cada porta lógica
- `testaPortas.py` — importa `portas.py` e executa testes para cada operação

---

## 🧠 Tabela Verdade (Referência)

> Esta é a tabela verdade **teórica** das portas lógicas implementadas. A geração automática desta tabela é uma funcionalidade planejada para versões futuras.

| A | B | AND | OR | NOT A | NAND | NOR | XOR | XNOR |
|---|---|:---:|:--:|:-----:|:----:|:---:|:---:|:----:|
| 0 | 0 |  0  | 0  |   1   |  1   |  1  |  0  |  1   |
| 0 | 1 |  0  | 1  |   1   |  1   |  0  |  1  |  0   |
| 1 | 0 |  0  | 1  |   0   |  1   |  0  |  1  |  0   |
| 1 | 1 |  1  | 1  |   0   |  0   |  0  |  0  |  1   |

---

## 📚 Conceitos Aplicados

- **Lógica Booleana** — álgebra de Boole aplicada a código
- **Funções em Python** — organização modular por responsabilidade
- **Separação de código** — lógica (`portas.py`) separada de testes (`testaPortas.py`)
- **Importação de módulos** — `import portas` para reutilização de código
- **Operadores lógicos** — `and`, `or`, `not` nativos do Python
- **Saída formatada** — exibição clara dos resultados no terminal

---

## 🔮 Implementações Futuras

- [ ] **Gerar tabela verdade automaticamente** — função para exibir tabela completa de qualquer porta
- [ ] Refatorar para Programação Orientada a Objetos (uma classe por porta)
- [ ] Interface CLI interativa com `argparse`
- [ ] Combinação de portas para simular circuitos (ex: Half Adder, Full Adder)
- [ ] Visualização gráfica com `matplotlib` ou `tkinter`
- [ ] Testes unitários com `pytest` ou `unittest`

---

## 🔗 Contexto Profissional

> Portas lógicas são a base de **toda arquitetura de computadores** — CPUs, memórias, controladores de rede. Como profissional de infraestrutura com 15+ anos de experiência, entender esse nível de abstração ajuda a diagnosticar comportamentos de hardware e sistemas a um nível mais profundo.

---

## 👤 Autor

**Rafael Passos Guimarães**

Analista de Infraestrutura | 15+ anos em TI | Transição para Cloud & DevOps

- 💼 LinkedIn: [@rapassos](https://linkedin.com/in/rapassos)
- 🐙 GitHub: [@rapassos](https://github.com/rapassos)
- 🦊 GitLab: [@rapassos](https://gitlab.com/rapassos)

---

## 📄 Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.

---

> 💡 **Próximos passos planejados:** 
> 1. Implementar geração automática de tabela verdade
> 2. Refatorar para OOP com classe base `PortaLogica` e subclasses
> 3. Adicionar testes unitários com `pytest`
