# Libreria de Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

# Inicializar variable en el terminal
# Windows:
# setx GOOGLE_API_KEY "#################"

# Inicializar modelo de lenguaje, la temperatura es un parámetro que controla la aleatoriedad de las respuestas generadas por el modelo. 
# Un valor más bajo (cercano a 0) hará que las respuestas sean más determinísticas y coherentes, mientras que un valor más alto (cercano a 1) 
# permitirá respuestas más creativas y variadas.
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.7)

pregunta = "¿En que año llegó el ser humano a la luna por primera vez?"
print("Pregunta: ", pregunta)

# Invocar el llm
respuesta = llm.invoke(pregunta)
print("Respuesta del modelo: ", respuesta.content)