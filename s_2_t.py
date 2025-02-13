import whisper

model = whisper.load_model("base")
result = model.transcribe("Voice 001 (1).m4a")
print(result["text"])
