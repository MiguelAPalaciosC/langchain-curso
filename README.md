# langchain-curso

Primeros pasos en LangChain y primer proyecto básico con Streamlit.

## 📚 Contenido

Curso introductorio de LangChain en el que se aprende a:

- Conectar modelos de lenguaje (OpenAI y Google Gemini) usando LangChain.
- Crear cadenas con plantillas de prompts (PromptTemplate + LCEL).
- Construir un chatbot interactivo con Streamlit.

## 🗂️ Estructura del proyecto

```
langchain-curso/
├── Tema 1/
│   ├── hello_world.py             # Primer chat con OpenAI (GPT-4o-mini)
│   ├── hello_world_gemini.py      # Primer chat con Google Gemini
│   ├── hello_world_avanzado.py    # Prompts con PromptTemplate y LCEL
│   ├── streamlit_chatbot.py       # Chatbot básico con Streamlit
│   └── streamlit.txt              # Lectura: ¿Qué es Streamlit?
├── venv/                          # Entorno virtual (no se versiona)
└── README.md
```

## 🛠️ Requisitos previos

- Python 3.9 o superior instalado en el sistema.
- Una API key de OpenAI y/o de Google AI Studio.

## ⚙️ Instalación

1. Crear el entorno virtual:

   ```bash
   py -m venv venv
   ```

2. Activar el entorno (Windows):

   ```bash
   .\venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install langchain==0.3.* langchain-openai langchain-google-genai streamlit
   ```

## 🔑 Configurar las claves de API

Las claves se declaran como variables de entorno del sistema (Windows):

```bash
setx OPENAI_API_KEY "tu_clave_aqui"
setx GOOGLE_API_KEY "tu_clave_aqui"
```

> ⚠️ Es necesario cerrar y reabrir la terminal después de usar `setx`.
> Nunca se deben exponer las claves en el código ni subirlas a un repositorio.

## ▶️ Ejecución

### Chat con OpenAI

```bash
python "Tema 1/hello_world.py"
```

### Chat con Google Gemini

```bash
python "Tema 1/hello_world_gemini.py"
```

### Ejemplo avanzado con PromptTemplate y LCEL

```bash
python "Tema 1/hello_world_avanzado.py"
```

### Chatbot con Streamlit

```bash
streamlit run "Tema 1/streamlit_chatbot.py"
```

## ✨ Características del chatbot

- Panel lateral con configuración de **temperatura** y **selección de modelo**.
- Historial de conversación persistente por sesión mediante `st.session_state`.
- Interfaz de chat moderna con `st.chat_message()` y `st.chat_input()`.

## 📖 Lecturas recomendadas

- `Tema 1/streamlit.txt`: guía introductoria sobre Streamlit (filosofía, ciclo reactivo, estado y secretos).