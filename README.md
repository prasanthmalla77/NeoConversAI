# NeoConversAI

**NeoConversAI** is a conversational AI project leveraging the power of Neo4j graph databases and OpenAI's language models. This project aims to create an intelligent chatbot that can understand and interact with complex data structures, providing insightful and context-aware responses.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Graph-Powered Conversations**: Utilizes Neo4j to handle and query relational data, making conversations contextually rich.
- **AI-Driven Responses**: Integrates OpenAI's language models to generate natural language responses.
- **Extensible**: Modular architecture allowing easy integration of new features and data sources.

## Installation

### Prerequisites
- Python 3.x
- Neo4j Database
- OpenAI API Key

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/prasanthmalla77/NeoConversAI.git
    cd NeoConversAI
    ```

2. **Set up the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API key and Neo4j credentials.
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    NEO4J_URI=bolt://localhost:7687
    NEO4J_USER=your_neo4j_username
    NEO4J_PASSWORD=your_neo4j_password
    ```

5. **Run the application:**
    ```bash
    python app.py
    ```

## Usage
Once the application is running, you can interact with the chatbot through a command-line interface (CLI) or web interface (if available). The chatbot will respond to your queries by leveraging the data stored in the Neo4j graph database.

## Project Structure
```plaintext
NeoConversAI/
│
├── app.py                   # Main application file
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables file
├── README.md                # Project documentation
├── /data/                   # Directory for data files
└── /modules/                # Custom modules and utilities
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Make sure to follow the existing code style and include tests for any new features.


## Contact
For any questions or feedback, please reach out to [Prasanth Malla](https://github.com/prasanthmalla77).

---

You can customize this template according to the specific details of your project.
