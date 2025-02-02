#!/usr/bin/env python3

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI


class State(TypeDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)


llm = ChatOpenAI(model="gpt-4o")

def chatbot(state: State):
    return { "messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

graph = graph_builder.compile()
