# todo.py
# ------------------------------------------------------
# コンソールで動く ToDo アプリ
#
# 今できること
#   1. 一覧表示
#   2. 追加
#   3. 終了
#
# ToDo はテキストファイル(todo.txt)に保存されるので、
# アプリを再起動しても内容が消えません。
#
# あとで「削除」「完了にする」などの機能を追加しやすいように、
# 処理をひとつずつ関数に分けています。
# ------------------------------------------------------

# ToDo を保存するファイルの名前
FILENAME = "todo.txt"


def load_todos():
    """
    ファイルから ToDo の一覧を読み込んで、リストとして返す関数。
    ファイルがまだ無い場合は、空のリストを返す。
    """
    todos = []

    try:
        # ファイルを読み込みモードで開く
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                # 行の最後にある改行(\n)を取り除く
                todo_text = line.strip()

                # 空行はリストに追加しない
                if todo_text != "":
                    todos.append(todo_text)

    except FileNotFoundError:
        # 初回起動時はファイルがまだ存在しないので、
        # 空のリストのまま返す(エラーにしない)
        pass

    return todos


def save_todos(todos):
    """
    ToDo のリストをファイルに保存する関数。
    追加のたびにこの関数を呼び出して、常に最新の状態を保存する。
    """
    # 書き込みモードでファイルを開く(中身は上書きされる)
    with open(FILENAME, "w", encoding="utf-8") as f:
        for todo_text in todos:
            f.write(todo_text + "\n")


def show_todos(todos):
    """
    ToDo の一覧を表示する関数。
    """
    print("\n----- ToDo 一覧 -----")

    if len(todos) == 0:
        print("(ToDo はまだ登録されていません)")
    else:
        # enumerate を使うと、番号付きで取り出せる
        # start=1 にすることで、1番から表示する
        for number, todo_text in enumerate(todos, start=1):
            print(f"{number}. {todo_text}")

    print("----------------------\n")


def add_todo(todos):
    """
    新しい ToDo を追加する関数。
    入力後、リストに追加してファイルにも保存する。
    """
    new_todo = input("追加する内容を入力してください: ")

    # 何も入力せずに Enter だけ押した場合は追加しない
    if new_todo.strip() == "":
        print("何も入力されなかったので、追加しませんでした。\n")
        return

    todos.append(new_todo)
    save_todos(todos)
    print(f"「{new_todo}」を追加しました。\n")


def show_menu():
    """
    メニューを表示する関数。
    """
    print("何をしますか?")
    print("1: 一覧表示")
    print("2: 追加")
    print("3: 終了")


def main():
    """
    プログラムの入口となる関数。
    ここで ToDo を読み込み、メニューを繰り返し表示する。
    """
    # 起動時にファイルから ToDo を読み込む
    todos = load_todos()

    print("ToDo アプリを起動しました。")

    # ユーザーが「終了」を選ぶまで、ずっとメニューを表示し続ける
    while True:
        show_menu()
        choice = input("番号を選んでください: ")

        if choice == "1":
            show_todos(todos)

        elif choice == "2":
            add_todo(todos)

        elif choice == "3":
            print("ToDo アプリを終了します。")
            break

        else:
            print("1〜3の番号を入力してください。\n")


# ------------------------------------------------------
# このファイルが直接実行されたときだけ main() を呼び出す
# (他のファイルから import されたときは実行されないようにするため)
# ------------------------------------------------------
if __name__ == "__main__":
    main()
