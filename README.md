# 📝 Supabase連携 ToDoアプリ

本アプリは Streamlit と Supabase（PostgreSQL） を用いて開発した、
ブラウザ上で操作可能な 永続化対応 ToDoリストアプリ です。
タスクの追加・完了管理・削除・優先度管理が可能で、
アプリを再起動してもデータが保持されます。

## 🚀 アプリ試用URL
[https://webprograming01.streamlit.app/](https://webprograming01.streamlit.app/)

## ✨ 主な機能
- **タスクの登録**: 入力フォームから新しいタスクを即座に追加できます。
- **タスクの一覧表示**: タスクを「未完了」「完了」に分けて表示します。
- **タスクの削除**: チェックボックス操作により、未完了 ↔ 完了を切り替えられます。
- **タスクの分類**: 不要になったタスクをボタン操作で削除できます。
- **タスクの優先順位づけ**: 各タスクに「高・中・低」の3段階で優先度を設定可能です。
- **優先度順ソートと色分け表示**: 優先度に応じてタスクを自動ソートし、視覚的に分かりやすく表示します。


## 🛠 使用技術
- **Frontend/Backend**: Streamlit
- **Database**: Supabase (PostgreSQL)
- **Language**: Python
- **Infrastructure**: GitHub / Streamlit Cloud

## 💡 開発における工夫と課題解決
今回の開発では、生成AIを活用しながら以下のトラブルシューティングを乗り越えました。

1. **環境構築と依存関係**: 
   - ModuleNotFoundError: No module named 'supabase' が発生
   - pip install の実行および requirements.txt の適切な設定により解決
2. **Secrets（APIキー）の安全な管理**: 
   - Supabase の API Key や URL をコードに直接記述せず、st.secrets を利用して安全に管理
3. **Gitによるバージョン管理**: 
   - ローカル環境とGitHub間で発生したマージコンフリクトをVS Code のソース管理機能を用いて手動で解消
4. **データの永続化**:
   - sqlite3 のようなローカルDBではなく Supabase を採用
   - Streamlit Cloud 上でもデータがリセットされない構成を実現
