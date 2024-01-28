import streamlit as st
import functions

todo_list = functions.get_todo_list()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo.capitalize())
    functions.write_todo_list(todo_list)


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

