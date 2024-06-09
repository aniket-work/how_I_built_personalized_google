🔍 How I Built Personalized Google 🔍

In this project, we'll build a personalized search engine using AI agents, all running locally. Get ready for an exciting journey!

**Prerequisites:**

- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

**Steps:**

1. **Virtual Environment Setup:**

   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv how_I_built_personalized_google 
     ```

   - Activate the environment:
   
     - Windows:
        ```bash
        how_I_built_personalized_google\Scripts\activate
        ```
     - Unix/macOS:
        ```bash
        source how_I_built_personalized_google/bin/activate
        ```

2. **Install Project Dependencies:**

   - Install required packages using `pip`:
   
     ```bash
     pip install -r requirements.txt
     ```

3. **Setup Groq Key:**

   - Obtain your Groq API key from [Groq Console](https://console.groq.com/keys).
   - Set your key in the `.env` file as follows:
     ```plaintext
     GROQ_API_KEY=<YOUR_KEY>
     ```

4. **Install Ollama:**

   - Download and install Ollama from [Ollama website](https://ollama.com/download).

5. **Install Embedding Model:**

   - Pull the embedding model using Ollama:
     ```bash
     ollama pull nomic-embed-text
     ```

6. **Index Selector and Indexer:**

   - Ensure that you have active URLs listed in the `active_urls.json` file within the `indexer` directory.
   - Execute the `index_selector.py` script to index and retrieve documents from the active URLs:
     ```bash
     python index_selector.py
     ```
   - Execute the `indexer.py` script to perform additional indexing tasks:
     ```bash
     python indexer.py
     ```
7. **Run the Project:**

   - Run the main script to start the personalized search engine:
     ```bash
     python aoogle.py
     ```
These steps will guide you through setting up and running the personalized search engine locally. Enjoy exploring and discovering with your own personalized Google!
