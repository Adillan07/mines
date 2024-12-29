# Mines Game

## Descrição do Projeto

Mines Game é um jogo simples inspirado no clássico Campo Minado, desenvolvido como projeto de aprendizado por estudantes do curso técnico de Análise e Desenvolvimento de Sistemas da escola SENAI. Este projeto tem como objetivo explorar a biblioteca Tkinter para criação de interfaces gráficas e a manipulação de arquivos externos usando Python.

## Tecnologias Utilizadas

- **Python 3.12.1**
- **Tkinter** para criação da interface gráfica
- **Biblioteca** `os` **para manipulação de diretórios e arquivos**
- **Biblioteca** `random` **para seleção aleatória de elementos**

## Funcionamento do Software

1. **Objetivo do Jogo**:

   - Clique nos botões para revelar os diamantes (💎) e evitar as bombas (💣).
   - Acumule pontos ao encontrar diamantes. O jogo termina quando você encontra uma bomba ou acumula 15 pontos.

2. **Funcionalidades**:

   - O jogo salva a maior pontuação automaticamente em um arquivo `pontuacao.txt`.
   - A interface gráfica organiza os botões em uma grade de 5x4, cobrindo cada botão com um botão "cobertura" que só é removido após o clique.
   - Mensagens informativas aparecem ao final do jogo para indicar vitória ou derrota.

3. **Regras do Jogo**:

   - Existem bombas aleatoriamente posicionadas na grade, e cada clique pode revelar um diamante ou uma bomba.
   - A maior pontuação é exibida na interface principal do jogo.

## Configuração do Ambiente

1. **Pré-requisitos**:

   - Python 3.8 ou superior instalado na sua máquina.
   - Editor de texto ou IDE (opcional, mas recomendado).

2. **Instruções de Configuração**:

   1. Clone este repositório ou copie os arquivos do projeto para o seu computador.
   2. Certifique-se de que o arquivo `pontuacao.txt` está no mesmo diretório do script principal. Caso ele não exista, o programa o criará automaticamente na primeira execução.
   3. Navegue até o diretório do projeto no terminal.
   4. Execute o jogo com o comando:
      ```bash
      python main.py
      ```

3. **Geração de Executável** (opcional):

   - Certifique-se de que a biblioteca cx\_Freeze está instalada na sua máquina. Caso não esteja, utilize o comando:
     ```bash
     pip install cx_freeze
     ```
   - Em seguida, utilize o comando abaixo para criar a pasta 'build', que contém o executável do jogo:
     ```bash
     python setup.py build
     ```

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Contato

- **Ádillan Wasilewski Soares**\
  Email: [adill07ws@outlook.com](mailto\:adill07ws@outlook.com)
- **Otávio Ribeiro Leite Neto**\
  Email: [netootavio223@outlook.com](mailto\:netootavio223@outlook.com)

Instrutores: Rafael Ribas e João Paulo Lepinsk

