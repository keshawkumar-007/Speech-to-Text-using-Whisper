import whisper

# Load the pre-trained Whisper model (tiny/medium/base/large)
model = whisper.load_model("base")  # You can use "tiny" for faster results

# Load your audio file
result = model.transcribe("b.m4a")

# Print the transcribed text
print("\n📄 Transcription Output:")
print(result["text"])
