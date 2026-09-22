# Libreria de openai, y plantillas prompt
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
# Inicializar variable en el terminal
# Windows:
# setx OPENAI_API_KEY "#################"

# Inicializar modelo de lenguaje, la temperatura es un parámetro que controla la aleatoriedad de las respuestas generadas por el modelo. 
# Un valor más bajo (cercano a 0) hará que las respuestas sean más determinísticas y coherentes, mientras que un valor más alto (cercano a 1) 
# permitirá respuestas más creativas y variadas.
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre\n Nombre del usuario {nombre}\nAsistente:"
)

# Cadena moderna con LCEL (LangChain Expression Language)
chain = plantilla | chat

# Ejecución
resultado = chain.invoke({"nombre": "Miguel"})
print(resultado.content)