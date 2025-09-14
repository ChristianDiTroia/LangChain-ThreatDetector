# ThreatDetector

Threat Detector is a chat/textual threat analysis api built using LangChain, Groq API, and FastAPI (currently a WIP project)

This project leverages LLMs hosted on the Groq API to analyze the level of danger/threat posed in a given string of text.
For example, the phrase "you're killin me here" contains a violent word but is unlikely to actually be a threat. Threat detector aims to help distinguish between this kind of ambiguity, providing helpful information about true the intent behind the message that can be used to determine how suspicious/dangerous it is.

## Usage

Start the development server on default host port 8000: `fastapi dev main.py`

### Endpoints

`POST /threat-analysis`

`POST /sentiment-analysis`

`POST /danger-word-extraction`

Request body format: `{"text": "text to be analyzed here"}`

## Postman Examples

<img width="1426" height="864" alt="image" src="https://github.com/user-attachments/assets/de6ab1db-d51b-4daa-827e-03b29a4584e9" />

<img width="1901" height="1079" alt="image" src="https://github.com/user-attachments/assets/ae5c4065-b8a2-4e85-a476-56201baf5dce" />

<img width="1892" height="638" alt="image" src="https://github.com/user-attachments/assets/6d271a79-f003-4b37-9070-d88c06ad72c0" />
