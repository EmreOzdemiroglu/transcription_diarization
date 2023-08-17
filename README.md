# Türkçe Ses Transkripsiyonu Flask API

## Usage Options


This project can be utilized in three different ways, each catering to different needs and environments. Below, you'll find a brief overview of these methods:

1. Google Colab: Ideal for those who prefer a cloud-based environment, Google Colab offers an accessible platform to run the code without any local setup. You can simply upload the notebook containing the project code to Colab and execute it there. Colab also provides access to GPU resources, which can accelerate computations.

2. Docker: If you prefer containerized deployment, you can use Docker to build and run the project. By encapsulating the project and its dependencies in a Docker container, you ensure a consistent and reproducible environment across different machines. This is particularly useful for managing dependencies and avoiding conflicts.

3. Direct Installation on Your Computer: For those who want to run the project directly on their local machine, a direct installation can be done. This involves cloning the project repository, installing the required dependencies as specified in the requirements.txt file, and executing the code in your preferred development environment.

### Colab

**:rocket: Try transcription_diarization live in 60s** [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EmreOzdemiroglu/Turkish-Speech-To-Text/blob/main/Transcription_Diarization.ipynb)

### Docker

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](link) 

### Installation

1. **Installing Required Libraries**: The project utilizes Python libraries specified in the `requirements.txt` file. You can install these libraries using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Starting the API**: In the terminal, navigate to the main directory of the project and run the following command:

   ```bash
   python app.py
   ```

   This will start the API at the address `http://127.0.0.1:5000/`.

2. **Sending a Transcription Request**: To obtain the transcription of an audio file, you can use the following `curl` command:

   ```bash
   curl -X POST -F "files=@file_path1.mp3" -F "files=@file_path2.mp3" http://localhost:5000/transcribe
   ```

   This command sends the `voice.mp3` file to the API and returns the transcription result as JSON.


###

## Lisans

MIT License

Copyright (c) [2023] [EmreOzdemiroglu]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

