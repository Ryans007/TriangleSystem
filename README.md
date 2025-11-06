# Sistema de Classificação de Triângulos

## Descrição da Atividade

Este projeto foi desenvolvido para a disciplina de **Testes de Software** da faculdade e tem como objetivo implementar e testar um sistema de classificação de triângulos. O sistema recebe três valores representando os lados de um triângulo e determina:

- Se os valores formam um triângulo válido
- O tipo do triângulo (Equilátero, Isósceles ou Escaleno)
- Validações de entrada (valores inteiros e positivos)

## Membros da Equipe

1. **Ryan Soares**
2. **Kevin Ryan**
3. **Luiz Neto**
4. **Gabriel Domingos**
5. **Thiago Barbosa**

## Estrutura do Projeto

```
├── requirements.txt          # Dependências do projeto
├── src/                     # Código fonte
│   ├── main.py             # Arquivo principal para execução
│   ├── tests.py            # Testes unitários
│   └── _class/             # Módulo da classe Triangle
│       ├── __init__.py     # Arquivo de inicialização do módulo
│       └── class_triangle.py # Implementação da classe Triangle
```

## Funcionalidades do Sistema

### Classe Triangle

A classe `Triangle` possui os seguintes métodos:

- **`__init__(side_a, side_b, side_c)`**: Construtor que recebe os três lados do triângulo
- **`triangle_type()`**: Método principal que retorna o tipo do triângulo ou mensagem de erro

### Validações Implementadas

1. **Verificação de tipo**: Os valores devem ser inteiros
2. **Verificação de positividade**: Os valores devem ser positivos
3. **Verificação de triângulo válido**: Os valores devem satisfazer a desigualdade triangular

### Tipos de Triângulo

- **Equilátero**: Todos os três lados são iguais
- **Isósceles**: Dois lados são iguais
- **Escaleno**: Todos os lados são diferentes

## Como Executar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes do Python)

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Executar o Programa Principal

```bash
cd src
python main.py
```

### Executar os Testes

```bash
cd src
pytest tests.py -v
```

## Casos de Teste Implementados

O arquivo `tests.py` contém os seguintes casos de teste:

1. **`test_value_not_integer()`**: Testa entrada com valor não inteiro
2. **`test_value_not_positive()`**: Testa entrada com valor negativo
3. **`test_triangle_invalid()`**: Testa valores que não formam um triângulo
4. **`test_is_quilateral()`**: Testa triângulo equilátero
5. **`test_is_isosceles()`**: Testa triângulo isósceles
6. **`test_is_scalene()`**: Testa triângulo escaleno

## Exemplo de Uso

```python
from _class import Triangle

# Criar um triângulo
triangle = Triangle(3, 4, 5)

# Obter o tipo do triângulo
result = triangle.triangle_type()
print(result)  # Output: "Escaleno"
```

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **pytest**: Framework de testes unitários

---

**Disciplina**: Testes de Software  
**Objetivo**: Implementação e teste de sistema de classificação de triângulos
