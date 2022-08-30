# UMA APLICAÇÃO MOBILE PARA CLASSIFICAÇÃO DE TIPOS DE LESÃO DE PELE UTILIZANDO REDES NEURAIS CONVOLUCIONAIS

Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em Engenharia de Computação da Universidade Federal de Santa Maria (UFSM, RS), como requisito parcial para obtenção do grau de Bacharel em Engenharia de Computação.

Autor: Felipe de Morais Soares 

Orientador: Dr. Daniel Welfer

### Resumo 

O câncer de pele é o tipo de câncer de maior incidência no Brasil, correspondendo cerca de 30% dos tumores malignos registrados no país, no entanto, apresenta um alto índice de cura quando detectado precocemente. Com o avanço da tecnologia, novas ferramentas são apresentadas na literatura para auxiliar na detecção precoce da doença. O presente trabalho apresenta uma aplicação mobile para classificação de tipos de câncer de pele utilizando redes neurais convolucionais (CNN). O objetivo é implementar de forma funcional uma aplicação, onde a parte mobile capta imagens e envia para um algoritmo de classificação, que através de redes neurais convolucionais indica o tipo de lesão de pele e retorna essa informação para usuário em seu smartphone. As arquiteturas de redes neurais convolucionais estudadas ao longo do projeto foram VGG11, ResNet50 e DenseNet121, realizando o treinamento das mesmas e comparando em sua fase de validação qual modelo obteve melhor desempenho. A rede DenseNet121 alcançou melhores resultados sobre as demais, com uma precisão de 91,24% na fase de validação. Uma vez estabelecida qual rede neural será aplicada no sistema, foi desenvolvida a aplicação mobile, para a captação de imagens, utilizando a ferramenta Kivy na linguagem Python e API Rest para realizar a troca de informações entre as partes frontend e backend. O aplicativo se mostrou funcional, após testes realizados correspondendo a performance da rede já treinada e se mostrando útil para o fomento da discussão sobre o tema proposto.

### Ambiente de Desenvolvimento 

#### Parte de Deep Learning 

• Ambiente de desenvolvimento [Google Colaboratory](https://colab.research.google.com/)
	Sistema Operacional Linux Ubuntu versão 18.04
	Dois Processadores Intel(R) Xeon(R) CPU @ 2.20GHz
	Placa de Vídeo NVIDEA Tesla T4
	13GB de Memória RAM
• Linguagem de Programação [Python](https://www.python.org/) versão 3.7.13
	Biblioteca [Numpy](https://numpy.org/) versão 1.21.6 utilizada para cálculos matemáticos
	Biblioteca [Pandas](https://pandas.pydata.org/) versão 1.3.5 utilizada para manipulação e visualização de listas e tabelas
	Biblioteca [MatplotLib](https://matplotlib.org/) versão 3.2.2 utilizada para plotar imagens e gráficos
	Biblioteca [Glob](https://docs.python.org/3/library/glob.html) utilizada para o acesso e manipulação de pastas e arquivos no sistema operacional
	Biblioteca [Pillow](https://pillow.readthedocs.io/en/stable/) versão 7.1.2 utilizada para manipulação vetorial das imagens
	Biblioteca [Pytorch](https://pytorch.org/) versão 1.11.0 e todas as suas dependências, utilizada para o trabalho com Deep Learning
	Biblioteca [Scikit-learn](https://scikit-learn.org/stable/) versão 1.1 utilizado para a separação dos dados em treino e validação  

#### Parte de Depoy do Software 

• Ferramenta utilizada para desenvolvimento notebook Dell G7 7588
	Sistema Operacional Windows 11
	Processador Intel i7-8750H
	Placa de Vídeo NVIDEA GTX 1050 TI
	8GB de Memória RAM DDR4
• Linguagem de Programação Python versão 3.7.13
	Biblioteca [JSON](https://docs.python.org/3/library/json.html) versão 1.6.1 formato utilizado para a troca de dados através de API REST
	Biblioteca [Requests](https://requests.readthedocs.io/en/latest/) versão 2.9.1 utilizada para realização de requisições entre servidor e cliente
	Biblioteca [Pillow](https://pillow.readthedocs.io/en/stable/) versão 7.1.2 utilizada para manipulação vetorial das imagens
	Biblioteca [Pytorch](https://pytorch.org/) versão 1.11.0 utilizada para o carregamento do modelo de CNN treinado para classificação
	Biblioteca [Flask](https://flask.palletsprojects.com/en/2.2.x/) versão 2.1.2 utilizada para a criação da API REST
	Biblioteca [Kivy](https://kivy.org/) 2.1.0 utilizada para a criação do aplicativo Android
	Biblioteca [Kivymd](https://kivymd.readthedocs.io/en/latest/) 0.104.2 utilizada para a modelagem gráfica do aplicativo Android
• Ambiente de Desenvolvimento [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) Community Edition 2021.3.3  



### Redes Neurais Convolucionais Utilizadas 

Neste projeto, foram utilizadas as arquiteturas de redes convolucionais VGG11, ResNet50 e Densenet121. Estas arquiteturas foram estabelecidas através da biblioteca Pytorch na linguagem de programação Python e adaptadas de acordo com as necessidades apresentadas.  

O código do treinamento e teste das CNN's pode ser econtrado em <link>

### Dataset Utilizado

O conjunto de dados ou dataset utilizado para o desenvolvimento do projeto é o Human Against Machine with 10000 training images (HAM10000), coletado e disponibilizado para acesso público pela International Skin Imaging Collaboration (ISIC).

 Este dataset consiste em 10015 imagens de lesões pigmentadas de pele catalogadas através de metadados também disponibilizados para acesso. e pode ser encontrado em  https://doi.org/10.7910/DVN/DBW86T.

Os tipos de lesões de pele abordados no projeto foram:   

• Melanoma 

• Carcinoma

• Nevos Melanócitos  

• Queratose Seborreíca 

• Queratose Actínica 

• Dermatofibroma 

• Lesões Vasculares

### Deploy 

O deploy do Software foi realizado através de uma aplicação mobile e a comunicação entre as partes de classificação e aquisição de imagens foi feita através de métodos de API REST. A seguir um modelo de representação do funcionamento do sistema como um todo. 



<img align=center
	src='https://ik.imagekit.io/eogtlka8vuq/API_5YwLuStbC.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1661804276046' style="zoom:70%;" >



Os códigos para aplicação mobile e deploy da CNN podem ser econtrados em <link>. 

### Resultados

#### Desempenho das Redes Neurais

A realização da comparação dos resultados obtidos de cada modelo tem o intuito de definir qual rede teve o melhor desempenho para o problema de classificações de lesão de pele utilizando o conjunto de dados HAM10000. A Tabela mostra este comparativo entre as três abordagens realizadas no projeto . 

| Modelo      | Acurácia Treino | Acurácia Teste |
| ----------- | --------------- | -------------- |
| VGG11       | 87,31%          | 87,40%         |
| ResNet50    | 88,95%          | 88,19%         |
| DenseNet121 | 98,22%          | 91,24%         |

#### Layout da Aplicação Mobile 

As Figuras a seguir mostram a interface gráfica inicial do aplicativo, onde o usuário deve inserir suas credenciais de acesso para obter as funcionalidades do sistema. Uma vez que o acesso é permitido o menu principal é mostrado ao utilizador, onde o mesmo tem a opção de tirar uma foto de alguma lesão de pele ou carregar fotos que se encontram sistema de arquivos do Android. 

<img align=center
	src='https://ik.imagekit.io/eogtlka8vuq/app_rlRFhUvea.JPG?ik-sdk-version=javascript-1.4.3&updatedAt=1661805222395' style="zoom:70%;" >

Com a Imagem Carregada, basta clicar no botão de Classificar para aplicação enviar essa imagem pelo método HTTP POST através da API Rest e receber retorno do resultado da classificação do tipo de lesão de pele para a imagem fornecida pelo usuário, apresentando na interface gráfica qual classe a rede entendeu que a lesão informada pertence. 

<img align=center
	src='https://ik.imagekit.io/eogtlka8vuq/result_1AIJbSx-s.JPG?ik-sdk-version=javascript-1.4.3&updatedAt=1661805222193' style="zoom:70%;" >

### Material Final

O Material final apresentado para a obtenção do grau de Bacharel em Engenharia de Computação pode ser visualizado em:

:clapper: [Apresentação do Trabalho de Conclusão](https://youtu.be/NPBdcE4Zmck)

:books: Parte escrita do Trabalho de Conclusão

