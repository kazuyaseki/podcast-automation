import google.generativeai as genai

def generate_summary_voice(audio_file_path: str) -> str:
    client = genai.GenerativeModel("gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    prompt = "ポッドキャストの内容を要約してください"
    response = client.generate_content([prompt, audio_file])
    return response.text


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ポッドキャストの内容を要約するスクリプト")
    parser.add_argument("--audio_file_path", help="入力オーディオファイルのパス")
    args = parser.parse_args()

    audio_file_path = args.audio_file_path
    print(audio_file_path)
    print(generate_summary_voice(audio_file_path))