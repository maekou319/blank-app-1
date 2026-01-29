import streamlit as st
from supabase import create_client

# --------------------
# Supabase 接続
# --------------------
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("📝 Todoアプリ")

# --------------------
# タスク追加
# --------------------
new_task = st.text_input("新しいタスクを入力")

if st.button("追加"):
    if new_task.strip() != "":
        supabase.table("todos").insert({
            "title": new_task,
            "is_done": False
        }).execute()
        st.rerun()

# --------------------
# タスク取得
# --------------------
todos = supabase.table("todos").select("*").order("created_at").execute().data

# --------------------
# 未完了タスク
# --------------------
st.subheader("📌 未完了タスク")

for todo in todos:
    if not todo["is_done"]:
        col1, col2 = st.columns([4, 1])

        with col1:
            if st.checkbox(todo["title"], key=f"todo_{todo['id']}"):
                supabase.table("todos").update(
                    {"is_done": True}
                ).eq("id", todo["id"]).execute()
                st.rerun()

        with col2:
            if st.button("🗑️", key=f"delete_{todo['id']}"):
                supabase.table("todos").delete().eq(
                    "id", todo["id"]
                ).execute()
                st.rerun()

# --------------------
# 完了タスク
# --------------------
st.subheader("✅ 完了タスク")

for todo in todos:
    if todo["is_done"]:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"~~{todo['title']}~~")

        with col2:
            if st.button("🗑️", key=f"delete_done_{todo['id']}"):
                supabase.table("todos").delete().eq(
                    "id", todo["id"]
                ).execute()
                st.rerun()
