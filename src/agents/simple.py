from typing import TypedDict
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, SystemMessage
from langchain.chat_models import init_chat_model
import random

llm = init_chat_model("gemma:2b",
    model_provider="ollama")
class State(MessagesState):
    customer_name : str
    my_age: int




def node_1_(state: State): #Es mejor devolver solo lo que se actualice del estado
#es decir no return todo el state se ve mejor en el siguiente
    if state.get("customer_name") is None:
        state["customer_name"] = "Poelo"
        state["my_age"] = 20
        return state

        
def node_1(state: State):
    new_state: State = {}

    Sys_msg = [SystemMessage(content="Siempre en cada promtp responde con el nombre Juan en cada instrucción desde inicio hasta fin, ahora contesta al prompt:")]
     
    history = state.get("messages",[])

    history = Sys_msg + history
    




    if state.get("customer_name") is None:
        return{
            "customer_name": "John Doe"
        }
    else:
            new_state["my_age"] = random.randint(20, 30)
        
    

    ai_message = llm.invoke(history)
    
    new_state["messages"] = history + [ai_message]
    print(new_state)
    return new_state
     
    
    # importante: siempre devolver algo
    

def node_1__(state: State):
     
    customername = []
    hola = state.get("customer_name")
    customername.append(hola)




    if not state.get("customer_name"):
       

        

        return {
            "my_age": 20
        }

    return { 
        "customer_name": customername[0],
        "my_age":20
    }  # importante: siempre devolver algo
    

from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, 'node_1')
builder.add_edge('node_1', END)

agent = builder.compile()
