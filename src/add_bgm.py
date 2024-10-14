from pydub import AudioSegment

def add_bgm(input_path: str, output_path: str, bgm_path: str, bgm_volume: float = -29) -> None:
    """
    入力オーディオファイルにBGMを追加し、新しいファイルとして保存する関数。

    Args:
        input_path (str): 入力オーディオファイルのパス
        output_path (str): 出力オーディオファイルのパス
        bgm_path (str): BGMオーディオファイルのパス
        bgm_volume (float, optional): BGMの音量（デシベル）。デフォルトは-29dB。

    Returns:
        None
    """
    # 入力オーディオとBGMを読み込む
    input_audio = AudioSegment.from_file(input_path)
    bgm = AudioSegment.from_file(bgm_path)

    # BGMの音量を調整
    bgm = bgm + bgm_volume

    # BGMをループして入力オーディオの長さに合わせる
    bgm_loop = bgm * (len(input_audio) // len(bgm) + 1)
    bgm_loop = bgm_loop[:len(input_audio)]

    # 入力オーディオとBGMをオーバーレイ
    output_audio = input_audio.overlay(bgm_loop)

    # 結果を保存
    output_audio.export(output_path, format="mp3")


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="BGMを追加するスクリプト")
    parser.add_argument("--input_path", help="入力オーディオファイルのパス")
    parser.add_argument("--output_path", help="出力オーディオファイルのパス")
    parser.add_argument("--bgm_path", help="BGMオーディオファイルのパス")

    args = parser.parse_args()

    add_bgm(args.input_path, args.output_path, args.bgm_path)