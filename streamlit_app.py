import streamlit as st

st.title("ToDoリストアプリ")

if "todos" not in st.session_state:
    st.session_state.todos = []

with st.form("add_todo"):
    new_todo = st.text_input("新しいタスクを入力")
    submitted = st.form_submit_button("追加")
    if submitted and new_todo:
        st.session_state.todos.append(
            {"task": new_todo, "done": False}
        )

st.divider()
st.subheader("タスク一覧")

if len(st.session_state.todos) == 0:
    st.write("タスクはまだありません。")
else:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        with col1:
            todo["done"] = st.checkbox(
                "",
                value=todo["done"],
                key=f"done_{i}"
            )

        with col2:
            if todo["done"]:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.write(todo["task"])

        with col3:
            if st.button("削除", key=f"delete_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()
