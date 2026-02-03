import streamlit as st
from supabase import create_client

# ======================
# Supabase 接続
# ======================
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("📝 Todoリスト")

# ======================
# タスク追加
# ======================
st.subheader("➕ タスク追加")

with st.form("add_todo"):
    title = st.text_input("タスク内容")
    priority = st.selectbox("優先度", ["高", "中", "低"], index=1)
    submitted = st.form_submit_button("追加")

    if submitted and title:
        supabase.table("todos").insert({
            "title": title,
            "priority": priority,
            "completed": False
        }).execute()
        st.success("タスクを追加しました")
        st.rerun()

# ======================
# タスク取得（優先度順）
# ======================
priority_order = {
    "高": 1,
    "中": 2,
    "低": 3
}

todos = supabase.table("todos").select("*").execute().data
todos = sorted(todos, key=lambda x: priority_order.get(x["priority"], 2))

# ======================
# 色設定
# ======================
def priority_color(p):
    if p == "高":
        return "🔴"
    if p == "中":
        return "🟡"
    if p == "低":
        return "🔵"
    return "⚪"

# ======================
# 未完了タスク
# ======================
st.subheader("📌 未完了タスク")

for todo in todos:
    if not todo["completed"]:
        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:
            st.markdown(
                f"{priority_color(todo['priority'])} **{todo['title']}**（{todo['priority']}）"
            )

        with col2:
            if st.checkbox("完了", key=f"done_{todo['id']}"):
                supabase.table("todos").update(
                    {"completed": True}
                ).eq("id", todo["id"]).execute()
                st.rerun()

        with col3:
            if st.button("🗑", key=f"del_{todo['id']}"):
                supabase.table("todos").delete().eq("id", todo["id"]).execute()
                st.rerun()

# ======================
# 完了タスク
# ======================
st.subheader("✅ 完了タスク")

for todo in todos:
    if todo["completed"]:
        col1, col2 = st.columns([6, 1])

        with col1:
            st.markdown(
                f"~~{priority_color(todo['priority'])} {todo['title']}（{todo['priority']}）~~"
            )

        with col2:
            if st.button("削除", key=f"del_done_{todo['id']}"):
                supabase.table("todos").delete().eq("id", todo["id"]).execute()
                st.rerun()
