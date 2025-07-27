# LangChain-ThreatDetector
Threat Detector is a chat/textual threat analysis tool built using LangChain, Groq API, and FastAPI (currently a WIP project)

## Usage

Start the development server: ```fastapi dev main.py```

The default host port is: ```localhost:8000```

### Endpoints
```POST <host>/detect-threat``` 

with request body format ```{"text": "text to be analyzed here"}```