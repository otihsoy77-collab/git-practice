# ==============================
# じゃんけんゲーム
# ==============================
# コンソール（黒い画面）で遊べる、シンプルなじゃんけんゲームです。
# プレイヤーが「グー・チョキ・パー」のどれかを入力すると、
# コンピューターがランダムに手を選んで勝負します。

# ランダム（でたらめな数）を扱うために random モジュールを読み込む
import random

# ------------------------------
# じゃんけんの手のリストを用意する
# ------------------------------
# コンピューターの手をこの中からランダムに選ぶ
hands = ["グー", "チョキ", "パー"]


def get_computer_hand():
    """コンピューターの手をランダムに1つ選んで返す関数"""
    # random.choice はリストの中から1つをランダムに選んでくれる便利な機能
    return random.choice(hands)


def get_player_hand():
    """プレイヤーに手を入力してもらう関数"""
    while True:
        # input() でキーボードからの入力を受け取る
        player_hand = input("グー・チョキ・パーのどれかを入力してください: ")

        # 入力された文字が hands リストの中にあるかチェックする
        if player_hand in hands:
            # 正しい入力なら、その手を返して関数を終了する
            return player_hand
        else:
            # 正しくない入力なら、もう一度入力してもらう
            print("入力が正しくありません。「グー」「チョキ」「パー」のどれかを入力してください。")


def judge(player_hand, computer_hand):
    """プレイヤーとコンピューターの手を比べて、勝敗を判定する関数"""

    # 手が同じ場合は「あいこ」
    if player_hand == computer_hand:
        return "あいこ"

    # プレイヤーが勝つパターンを1つずつチェックする
    if player_hand == "グー" and computer_hand == "チョキ":
        return "勝ち"
    if player_hand == "チョキ" and computer_hand == "パー":
        return "勝ち"
    if player_hand == "パー" and computer_hand == "グー":
        return "勝ち"

    # 上の勝ちパターンに当てはまらなければ、プレイヤーの負け
    return "負け"


def main():
    """ゲーム全体の流れをまとめる関数"""

    print("=== じゃんけんゲームを始めます（全3回勝負）===")

    # 勝ち・負け・あいこの回数を数えるための変数
    win_count = 0
    lose_count = 0
    draw_count = 0

    # 3回だけ繰り返すためのループ
    # range(3) は 0, 1, 2 という3つの数字を順番に取り出してくれる
    for round_number in range(3):
        # 今が何回目の勝負かを表示する（round_number は 0 から始まるので +1 する）
        print(str(round_number + 1) + "回目の勝負")

        # プレイヤーの手を取得する
        player_hand = get_player_hand()

        # コンピューターの手を取得する
        computer_hand = get_computer_hand()

        # お互いの手を表示する
        print("あなた: " + player_hand)
        print("コンピューター: " + computer_hand)

        # 勝敗を判定する
        result = judge(player_hand, computer_hand)

        # 結果を表示して、回数を数える
        if result == "勝ち":
            print("あなたの勝ちです！")
            win_count += 1
        elif result == "負け":
            print("あなたの負けです。")
            lose_count += 1
        else:
            print("あいこです。")
            draw_count += 1

        print("------------------------------")

    # 3回すべて終わったら、結果をまとめて表示する
    print("=== 3回勝負の結果 ===")
    print("勝ち: " + str(win_count) + "回")
    print("負け: " + str(lose_count) + "回")
    print("あいこ: " + str(draw_count) + "回")


# このファイルが直接実行されたときだけ main() を呼び出す
if __name__ == "__main__":
    main()
