import streamlit as st
import functions as fu

todos = fu.get_todo()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fu.get_todo_w(todos)
st.title("odo App")
st.subheader("This is Mjd Todo App")
st.write("Your Todo List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        completed = todos.pop(index)
        fu.get_todo_w(todos)
        completed_todos = fu.completed_list()
        completed_todos.append(completed)
        fu.save_completed(completed_todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", on_change=add_todo, placeholder="Add a todo", key="new_todo")
