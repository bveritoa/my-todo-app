import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo app")
st.subheader("This is my toto app")
st.write("this is a <b>simple text</b>",
         unsafe_allow_html=True)

# st.checkbox("Todo1")
# st.checkbox("Todo2")
# st.checkbox("Todo3")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:",label_visibility="hidden",placeholder="Add new todo...",
              on_change=add_todo,key='new_todo')

# print("hello")
#
# st.session_state