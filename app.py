import streamlit as st
from supabase import create_client

# Supabase 接続
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("📝 Supabase Todo アプリ（INSERTテスト）")

# -------------------------
# Todo 追加
# -------------------------
todo_title = st.text_input("新しいTodoを入力")

if st.button("追加"):
    if todo_title:
        supabase.table("todos").insert({
            "title": todo_title
        }).execute()
        st.success("Todoを追加しました")
    else:
        st.warning("Todoを入力してください")

st.divider()

# -------------------------
# Todo 一覧表示
# -------------------------
res = supabase.table("todos").select("*").order("created_at").execute()

for todo in res.data:
    st.write(f"- {todo['title']}（完了：{todo['is_done']}）")

