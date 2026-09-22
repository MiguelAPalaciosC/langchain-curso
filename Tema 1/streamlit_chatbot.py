from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

import streamlit as st

# Configurar la pagina de la aplicacion

# Configuracion meta de la pagina 
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖​")

#Informacion dentro de la pagina titulo y descripción
st.title("🤖​ Chatbot Básico con LangChaing")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar")


with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])
    
    # ¿Cómo recrearías el modelo con los nuevos parámetros?
    chat_model = ChatOpenAI(model=model_name, temperature=temperature)
    # chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Memoria del chat bot
# Inicializar el historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro. 
 
Historial de conversación:
{historial}
 
Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)

# En lugar de usar cadenas tradicionales, ahora puedes hacer:
cadena = prompt_template | chat_model

# Mostrar mensajes previos
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        # No muestra el mensaje por pantalla
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.markdown(msg.content)

# Iniciar nueva conversacion
if st.button("♻️ Nueva conversación"):
    st.session_state.mensajes = []
    st.rerun()

# cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if pregunta:
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty() #Contenedor vacio que se va a actualizar en tiempo de ejecucion
            full_response = "" # Cadena de texto vacia
 
            # ¡Aquí está la magia del streaming!
            # Invocacion del metodo stream de la cadena
            # Devuelve las generaciones poco a poco y componiendo la respuesta
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")  # El cursor parpadeante
            
            response_placeholder.markdown(full_response)
        
        # No olvides almacenar los mensajes
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))
        
    except Exception as e:
        # ¿Qué tipo de errores podrían ocurrir aquí?
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key de OpenAI esté configurada correctamente.")