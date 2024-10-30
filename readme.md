# Projeto EasyOCR Docker

Este projeto usa EasyOCR em um contêiner Docker para ler texto de arquivos de imagem localizados na pasta `input` e gerar arquivos de texto correspondente na pasta `output`. Isso permite a digitalização e reconhecimento de texto de imagens de forma automatizada e portável, com o processamento feito totalmente dentro do contêiner Docker.

## Estrutura do Projeto

- **input**: Diretório onde você coloca as imagens para processamento OCR.
- **output**: Diretório onde o contêiner salvará os arquivos de texto gerados, com o mesmo nome das imagens de entrada.
- **Dockerfile**: Arquivo de configuração para criação do contêiner Docker com EasyOCR.
- **run.py**: Script Python que realiza o OCR nas imagens do diretório `input` e salva os resultados em `output`.

## Configuração e Execução

1. **Construa a imagem Docker:**

    ```bash
    docker build -t easyocr .
    ```

2. **Execute o contêiner para processar as imagens:**

    ```bash
    docker run --rm -v $(pwd):/app easyocr python /app/run.py
    ```

> Esse comando monta o diretório atual no contêiner, para que o `run.py` acesse as pastas `input` e `output` corretamente.

### Observações
- **Modelo OCR**: EasyOCR esta configurado para o idioma português e inglês. Você pode adicionar outros idiomas modificando o argumento da função `easyocr.Reader`.

## Documentação Relevante

- [EasyOCR no GitHub](https://github.com/JaidedAI/EasyOCR): Repositório oficial do EasyOCR.
- [Documentação EasyOCR](https://www.jaided.ai/easyocr/documentation/): Guia completo para configuração e uso do EasyOCR, opções de configuração e exemplos de uso.

## Exemplo de Uso

Para realizar OCR em arquivos de imagem, basta colocar as imagens na pasta `input` e rodar o contêiner. Os resultados serão gerados em `output` com o mesmo nome da imagem de entrada (por exemplo, `imagem.png` gerará `imagem.png.txt`).
