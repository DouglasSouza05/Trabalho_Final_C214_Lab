[![CI de Testes](https://github.com/DouglasSouza05/Trabalho_Final_C214_Lab/actions/workflows/workflow.yml/badge.svg)](https://github.com/DouglasSouza05/Trabalho_Final_C214_Lab/actions/workflows/workflow.yml)

# Trabalho_Final_C214_Lab - Projeto Agenda

## Descrição

Este Projeto consiste em uma Agenda de Contatos com Interface Gráfica de Usuário (GUI) desenvolvida usando a Biblioteca Python PyQt5. Oferece funcionalidades para Adicionar, Listar, Pesquisar e Remover Contatos e, também, Deletar a própria Agenda do Usuário.

<img src = "agenda.png" />

## Instalação

Certifique-se de ter o Python instalado. Em seguida, instale as Dependências e rode o Projeto. Passo a Passo abaixo.

Instalação do pip como Gerenciador de Dependências:

```
python -m pip install -U pip
```

Inclusão de todas as Dependências do Projeto:

```
pip freeze > requirements.txt
```

Instalação das Dependências:

```
pip install -r requirements.txt
```

Certifique-se de ter as Bibliotecas instaladas com os seguintes Comandos:

```
pip install PyQt5
pip install xmlrunner
pip install unittest-xml-reporting
```

## Executando o Projeto

Entre na pasta da Interface Gráfica PyQt5:

```
cd .\ProjetoAgenda\InterfacePyQt\
```

Execute o seguinte Comando no Terminal:

```
python agendaApp.py
```

Uma janela da Interface Gráfica será aberta, permitindo as interações do Usuário com as funcionalidades da Agenda de Contatos.

## Testes

Entre na pasta de Testes criados com a Framework unittest:

```
cd .\ProjetoAgenda\Testes\
```

Os Testes podem ser rodados todos de uma vez pelo seguinte Comando:

```
python -m unittest -v
```

Também é possível rodá-los individualmente, na própria IDE utilizada ou por Linha de Comando:
Exemplo: `python nome_do_teste.py `

## Resultados

Temos como resultado dos Testes:

```
test_formatar_contato (test_config.TestConfig.test_formatar_contato)
 Testa se a função formatar_contato da classe Config formata corretamente um objeto Contato. ... ok
 test_formatar_contato_diferente (test_config.TestConfig.test_formatar_contato_diferente)
 Testa se a função formatar_contato da classe Config gera resultados diferentes para contatos distintos. ... ok
 test_formatar_json (test_config.TestConfig.test_formatar_json)
 Testa se a função formatar_json da classe Config gera corretamente um JSON a partir de um objeto Contato. ... ok
 test_formatar_json_diferente (test_config.TestConfig.test_formatar_json_diferente)
 Testa se a função formatar_json da classe Config gera resultados diferentes para contatos distintos. ... ok
 test_formatar_json_e_contato (test_config.TestConfig.test_formatar_json_e_contato)
 Testa se a função formatar_json e formatar_contato da classe Config geram resultados diferentes para o mesmo contato. ... ok
 test_getters (test_contatos.TestContato.test_getters) ... ok
 test_nome_diferente (test_contatos.TestContato.test_nome_diferente) ... ok
 test_setters (test_contatos.TestContato.test_setters) ... ok
 test_sobrenome_diferente (test_contatos.TestContato.test_sobrenome_diferente) ... ok
 test_telefone_diferente (test_contatos.TestContato.test_telefone_diferente) ... ok
 test_adicionar_contato (test_gerenciador.TestGerenciador.test_adicionar_contato) ... ok
 test_listar_contatos (test_gerenciador.TestGerenciador.test_listar_contatos) ... ok
 test_pesquisar_contato_existente (test_gerenciador.TestGerenciador.test_pesquisar_contato_existente) ... ok
 test_pesquisar_contato_inexistente (test_gerenciador.TestGerenciador.test_pesquisar_contato_inexistente) ... ok
 test_remover_contato_existente (test_gerenciador.TestGerenciador.test_remover_contato_existente) ... Nenhum contato para salvar.
 ok
 test_remover_contato_inexistente (test_gerenciador.TestGerenciador.test_remover_contato_inexistente) ... ok

Ran 16 tests in 0.004s

OK
```

Os Arquivos Artefatos dos resultados que são criados após os Testes são os de Extensão .xml:

> resultados_testes_config.xml

> resultados_testes_contatos.xml

> resultados_testes_gerenciador.xml

## DevOps

Pode ser verificado pelo Actions do repositório deste trabalho, identificando os Jobs de Build, Test e Notification. Além disso, também há o Badge do início deste README que confirma que os Testes estão passando com Sucesso e de que tudo está funcionando corretamente em nosso Pipeline.
Sendo responsáveis por tal operação os arquivos .github\workflows\workflow.yml e scripts\email.sh.

## Participantes do projeto:

Douglas Brandão de Souza - GEC - 1730

Eduardo Costa Resende - GES - 200

Lucas Brandão Costa - GES - 58

Lucas de Souza Resende - 01 - GES
