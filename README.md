# Bhagavad-Gita-Search-Engine-with-LLM


<img src="demo/image 1.png" alt="workflow" width="70%">

A large language model is a sophisticated artificial intelligence system designed to generate human-like text and understand natural language. It is trained on vast amounts of diverse data, including books, articles, websites, and other textual sources. These models employ deep learning techniques, particularly transformer architectures, to learn the statistical patterns and relationships in the language data.

One notable characteristic of large language models is their ability to generate text that often exhibits remarkable fluency, demonstrating an understanding of grammar, syntax, and semantic structures. They can produce lengthy and detailed responses, offering relevant and informative information based on the input provided.

These models have the potential to revolutionize various fields, including content creation, customer support, language translation, and academic research. They can assist users in generating written content, provide insights and answers to complex queries, and even facilitate natural and engaging conversations.

## The Da Vinci model :

The Da Vinci model is a highly advanced language model developed by OpenAI, named after the legendary artist and polymath Leonardo da Vinci. Building upon the success of previous models like GPT-3, the Da Vinci model represents a significant leap forward in natural language processing capabilities.

With a vast number of parameters and an enhanced understanding of context, the Da Vinci model aims to produce even more coherent, contextually accurate, and nuanced responses. It leverages state-of-the-art techniques, including the transformer architecture and unsupervised learning, to generate human-like text that can mimic the style and tone of specific prompts.

The Da Vinci model has been trained on a diverse range of internet text, covering an extensive array of topics and domains. This comprehensive training allows it to provide in-depth and accurate information on various subjects, answer complex questions, assist with creative writing, and engage in more interactive and dynamic conversations.



# Demo:

<img src="demo/image 2.png" alt="workflow" width="70%">
<br>

<img src="demo/image 3.png" alt="workflow" width="70%">
<br>

<img src="demo/image 4.png" alt="workflow" width="70%">

# Dataset has been used:

- [Dataset link](https://libgen.is/book/index.php?md5=8B7A20960F8B81D3BAF6A2E64E24FF37)


# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/aibi10/Bhagavad-Gita-Search-Engine-with-LLM
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n Gita python=3.7.10 -y
```

```bash
conda activate Gita
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### STEP 03- add Open AI API key in line 12 of app.py

```bash
os.environ["OPENAI_API_KEY"] = "xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### STEP 04 - add path to pdf book in line 19

```bash
reader = PdfReader(r"C:\Users\XXXXX\Downloads\Eknath Easwaran - The Bhagavad Gita  -Nilgiri Press (2007).pdf")
```

### STEP 05 - run this command to run the app in your browser

```bash
python run app.py
```

```bash
Author: Abhishek Singh
Data Scientist
Email: isingh.abhishek10@gmail.com
```
