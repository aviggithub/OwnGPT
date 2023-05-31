# OwnGPT
Create Own ChatGPT with your documents using streamlit UI on your own device using GPT models. No data leaves your device and 100% private.


This project was inspired by the original privateGPT (https://github.com/imartinez/privateGPT). Most of the description here is inspired by the original privateGPT. 

Ask questions to your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!

Built with LLM:[ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). 


# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
pip install -r requirements.txt
```


## Instructions for ingesting your own dataset

Put any and all your files into the `source_documents` directory

The supported extensions are:

   - `.csv`: CSV,
   - `.docx`: Word Document,
   - `.enex`: EverNote,
   - `.eml`: Email,
   - `.epub`: EPub,
   - `.html`: HTML File,
   - `.md`: Markdown,
   - `.msg`: Outlook Message,
   - `.odt`: Open Document Text,
   - `.pdf`: Portable Document Format (PDF),
   - `.pptx` : PowerPoint Document,
   - `.txt`: Text file (UTF-8),

Run the following command to ingest all the data.

```shell
python ingest.py
```

It will create an index containing the local vectorstore. Will take time, depending on the size of your documents.
You can ingest as many documents as you want, and all will be accumulated in the local embeddings database. 
If you want to start from an empty database, delete the `index`.

Note: When you run this for the first time, it will download take time as it has to download the embedding model. In the subseqeunt runs, no data will leave your local enviroment and can be run without internet connection.

## Ask questions to your documents, locally! using sreamlit UI
In order to ask a question, run a command like:

To run the Streamlit app, use the following command:
```
streamlit run owngpt.py --server.address localhost
```
This command launches the Streamlit app and connects it to the backend server running at `localhost`.

And wait for "http://localhost:8501/" web App running on local system.

Enter your Query in TextBox and Hit enter. Wait while the LLM model consumes the prompt and prepares the answer. show your query and answer below TextBox. as show in below figure.


![own private gpt](https://github.com/aviggithub/owngpt/assets/46967951/938e588e-5f7d-48e5-b63f-0db925071886)


# How does it work?
Selecting the right local models and the power of `LangChain` you can run the entire pipeline locally, without any data leaving your environment, and with reasonable performance.

- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `InstructorEmbeddings`. It then stores the result in a local vector database using `Chroma` vector store. 
- `streamlit run owngpt.py` uses a local LLM (ggml-gpt4all-j-v1.3-groovy.bin) to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- You can replace this local LLM with any other LLM from the HuggingFace. Make sure whatever LLM you select is in the HF format.

# System Requirements

## Python Version
To use this software, you must have Python 3.10.0 or later installed. Earlier versions of Python will not compile.

## C++ Compiler
If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

### For Windows 10/11
To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
   * Universal Windows Platform development
   * C++ CMake tools for Windows
3. Download the MinGW installer from the [MinGW website](https://sourceforge.net/projects/mingw/).
4. Run the installer and select the "gcc" component.



# Disclaimer
This is a test project to validate the feasibility of a fully local private solution for question answering using LLMs and Vector embeddings. It is not production ready, and it is not meant to be used in production. ggml-gpt4all-j-v1.3-groovy.bin is based on the GPT4all model so that has the original Gpt4all license. 

