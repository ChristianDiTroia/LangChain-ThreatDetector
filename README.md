# LangChain-ThreatDetector
Threat Detector is a chat/textual threat analysis api built using LangChain, Groq API, and FastAPI (currently a WIP project)

This project leverages LLMs hosted on the Groq API to analyze the level of danger/threat in a given string of text.
For example, "you're killin me here" contains a dangerous phrase but is unlikely to actually be a threat. Threat detector aims to help distinguish between this kind of ambiguity, providing helpful information on what the intent behind the message really was and ultimately giving a rating on how suspicious/dangerous it is.

## Usage

Start the development server: ```fastapi dev main.py```

The default host port is: ```localhost:8000```

### Endpoints
```POST <host>/detect-threat``` 

with request body format ```{"text": "text to be analyzed here"}```

## Postman Examples

<img width="999" height="804" alt="Screenshot 2025-07-26 at 9 08 49 PM" src="https://github.com/user-attachments/assets/c74c7742-c9b3-476c-a6bb-e4aee759c456" />
