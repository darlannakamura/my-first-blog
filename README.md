# Curso Welcome to The Django

##Sobre
Aplicação desenvolvida no Curso **Welcome to The Django** ministrado por [Darlan Nakamura](https://github.com/darlannakamura) e [Robson Cruz](https://github.com/deadpyxel) na **Semana da Computação de Presidente Prudente (SECOMPP)** no ano de 2018.
O curso foi elaborado com a intenção de demonstrar a arquitetura do framework de desenvolvimento Python [Django](https://www.djangoproject.com),  demonstrando sua arquitetura, abordando suas principais vantagens, e como desenvolver na prática uma aplicação web em Django do zero.

### Cronograma
O curso teve a duração de oito horas e seguiu o seguinte cronograma:

1. Quem somos
2. O que é o Django
3. Mercado de Trabalho para um Desenvolvedor Django
4. Setup e Settings
5. Introdução ao Framework e explicação da teoria (arquitetura da ferramenta e conceitos importantes)
6. Desenvolvimento da aplicação
	- Comandos:  Start project + estrutura + runserver + create app
	- Utilizando o Jinja para criação dos templates e trabalhando com as rotas - first view + url
	- Models: makemigrate e migrate 
	- Django-admin
	- Construindo as views através dos models
	- CBV - Class Based Views 
	- Modelform
	- Templates e static
	- Autenticação (segurança e processo de autenticação)
7. Conceituação e teoria por trás de uma API Restful
8. Desenvolvimento de uma API RESTFul utilizando o Django Rest Framework

### Material
Você pode acessar o **slide** utilizado no curso clicando [aqui](https://slides.com/robsoncruz/secompp2018-mc11/#/).

## Configuração

### Pré-requisitos
Estamos assumindo que você tenha instalado as seguintes tecnologias:
- [Python](https://www.python.org) versão 3.6 ou superior.
- Ambiente Virtual: podendo ser o próprio `virtualenv` do Python 3 ou o [Anaconda](https://www.anaconda.com).

### Instalação

#### Clonando o Projeto
Para obter o projeto, é necessário cloná-lo em sua máquina através do comando:

	git clone https://github.com/darlannakamura/secompp-2018.git

#### Navegando Para o Diretório
Antes de instalar as dependências, é necessário navegar para o diretório clonado com o comando:

	cd secompp-2018

#### Instalando as Dependências
Para instalar as dependências, digite o comando abaixo:
	
	pip install -r requirements.txt

#### Iniciando o Projeto
Para rodar o projeto em sua máquina, execute o comando abaixo:

	python manage.py runserver

Caso ocorra tudo bem, você poderá acessar a aplicação pelo seu browser através do endereço: [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Autores

- [Darlan Nakamura](https://github.com/darlannakamura)
- [Robson Cruz](https://github.com/deadpyxel)

## Licença

The MIT License (MIT)

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

