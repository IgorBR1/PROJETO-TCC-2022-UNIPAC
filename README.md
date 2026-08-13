# Detecção de Vagas em Estacionamento

Projeto desenvolvido em 2022 como Trabalho de Conclusão de Curso de Ciência da Computação.

O sistema utiliza **visão computacional** para identificar vagas disponíveis em um estacionamento através de uma câmera, utilizando processamento de imagens para analisar cada vaga.

## Tecnologias

* Python
* OpenCV
* NumPy
* CVZone
* Pickle

## Como funciona

O sistema utiliza uma sequência de filtros para analisar a imagem:

```text
Imagem / Webcam
      ↓
Grayscale
      ↓
Blur
      ↓
Threshold
      ↓
Análise das vagas
      ↓
Vaga livre / ocupada
```

As posições das vagas são previamente delimitadas e armazenadas em um arquivo utilizando Pickle. Durante a execução, cada região é analisada para verificar a quantidade de pixels detectados.

## Execução

Instale as dependências:

```bash
pip install opencv-python cvzone numpy
```

Execute o programa:

```bash
python main.py
```

## Estrutura

```text
├── main.py
├── car_detect.py
├── TESTE2
└── car_park_test.png
```

## Contexto

O projeto foi desenvolvido e testado utilizando uma webcam no estacionamento da UNIPAC Barbacena. O trabalho buscou apresentar uma abordagem de baixo custo para auxiliar na identificação de vagas disponíveis.

## Limitações

A abordagem baseada em filtros pode sofrer influência de iluminação, ruídos e diferentes condições do ambiente. Durante os testes realizados no projeto original, foram observadas falhas de detecção em alguns cenários.

## Autor

**Igor Brasil de Oliveira**

Projeto acadêmico desenvolvido no curso de Ciência da Computação — UNIPAC.
