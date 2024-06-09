
🏢 How I Built Personalized Google 🏢

In this project, we'll build a one-person business using AI agents, all running locally. Get ready for an exciting journey!

**Prerequisites:**

* Python installed on your system.
* A basic understanding of virtual environments and command-line tools.

**Steps:**

1. **Virtual Environment Setup:**

   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv how_I_built_personalized_google 
     ```

   - Activate the environment:
   
     * Windows:
        ```bash
        how_I_built_personalized_google\Scripts\activate
        ```
     * Unix/macOS:
        ```bash
        source how_I_built_personalized_google/bin/activate
        ```

2. **Install Project Dependencies:**

   - Grab the necessary packages with the help of `pip`:
   
     ```bash
     pip install -r requirements.txt
     ```

3. **Setup Groq key:**

   - get your groq key from https://console.groq.com/keys
   - set your key in .env file as : GROQ_API_KEY=<YOUR_KEY>
    ```
   
4. install embedding model
    ollama pull nomic-embed-text

4. Run 
```python
(how_I_built_personalized_google) ~\PycharmProjects\how_I_built_personalized_google>python -m streamlit run main.py
```




