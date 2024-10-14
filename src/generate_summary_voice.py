import os
import google.generativeai as genai
from elevenlabs import ElevenLabs, VoiceSettings

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def generate_summary_voice(audio_file_path: str, output_path: str) -> str:
    gemini_client = genai.GenerativeModel("gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    prompt = "ポッドキャストの内容を要約したナレーション文を書いてください"
    print("generating narration text...")
    response = gemini_client.generate_content([prompt, audio_file])

    print("generating voice...")
    elevenlabs_client = ElevenLabs(
        api_key=ELEVENLABS_API_KEY,
    )
    narration_audio = elevenlabs_client.text_to_speech.convert(
        voice_id="pMsXgVXv3BLzUgSXRplE",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=response.text,
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=0.3,
            style=0.2,
        ),
    )

    with open(output_path, "wb") as f:
        for chunk in narration_audio:
            if chunk:
                f.write(chunk)

    print(f"{output_path}: A new audio file was saved successfully!")

    return response.text


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ポッドキャストの内容を要約するスクリプト")
    parser.add_argument("--audio_file_path", help="入力オーディオファイルのパス")
    parser.add_argument("--output_path", help="出力オーディオファイルのパス")
    args = parser.parse_args()

    audio_file_path = args.audio_file_path
    output_path = args.output_path
    print(generate_summary_voice(audio_file_path, output_path))