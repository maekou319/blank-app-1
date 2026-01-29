# 📝 Supabase連携 ToDoアプリ

Streamlit と Supabase を活用した、シンプルで永続的なデータ管理ができるToDoリストアプリです。
ブラウザからタスクの追加・一覧表示ができ、アプリを閉じてもデータが保持されます。

## 🚀 アプリ試用URL
[https://webprograming01.streamlit.app/](https://webprograming01.streamlit.app/)

## ✨ 主な機能
- **タスク登録**: 入力フォームから新しいタスクを即座に追加できます。
- **タスク一覧表示**: 登録されたタスクを「未完了」「完了」の状態別に一覧表示します。
- **タスク削除**: 登録されたタスクをボタンを押すことで削除できます。
- **データ永続化**: Supabase（外部データベース）と連携しているため、アプリの再起動後もデータが消えません。
- **直感的なUI**: Streamlitによるシンプルで使いやすいインターフェースを採用しています。

## 🛠 使用技術
- **Frontend/Backend**: Streamlit
- **Database**: Supabase (PostgreSQL)
- **Language**: Python 3.x
- **Infrastructure**: GitHub / Streamlit Cloud

## 💡 開発における工夫と課題解決
今回の開発では、生成AIを活用しながら以下のトラブルシューティングを乗り越えました。

1. **環境構築と依存関係**: 
   - `ModuleNotFoundError: No module named 'supabase'` に対し、`pip install` の実行と `requirements.txt` の適切な設定を行い解決しました。
2. **セキュリティとSecrets管理**: 
   - APIキー等の機密情報をコードに直接書かず、`st.secrets` を利用して安全に管理する方法を学びました。
3. **Gitによるバージョン管理**: 
   - 手元のコードとGitHub上のコードで発生した「マージコンフリクト（衝突）」を、VS Codeのソース管理機能を用いて手動で解消しました。
4. **データの永続化**:
   - `sqlite3` 等の簡易DBではなく `Supabase` を採用することで、Streamlit Cloud上でもデータがリセットされない構成を実現しました。

## 📝 ライセンス
このプロジェクトは課題学習用として公開されています。