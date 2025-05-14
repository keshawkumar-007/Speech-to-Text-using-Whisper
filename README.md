# 🎙️ Whisper Speech-to-Text Transcription

This project is a simple and effective demo using OpenAI's Whisper model to convert MP3 audio files into text. It runs locally in your terminal or Jupyter Notebook using Python and the Hugging Face interface.

---

## 📂 Features

- 🎧 Converts MP3 audio files to text  
- 🧠 Uses OpenAI’s pre-trained Whisper model (`tiny`, `base`, `small`, etc.)  
- 💬 Prints transcription in the terminal or notebook  
- 📄 Saves transcription to `transcription.txt`  
- 🧪 Works in both terminal and Jupyter Notebook environments  

---

## 🛠️ Requirements

- Python 3.7+  
- `ffmpeg` installed and accessible via system path  

### 📦 Python Packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
openai-whisper
torch
ffmpeg-python
```

Or install manually:

```bash
pip install openai-whisper torch ffmpeg-python
```

---

## 🧪 Set Up & Run (Local Terminal)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/whisper-speech-to-text.git
cd whisper-speech-to-text
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the transcription script

```bash
python whisper_transcribe.py
```

---

## 💻 Run in Jupyter Notebook

1. Start Jupyter:

```bash
jupyter notebook
```

2. Open `whisper_transcription.ipynb`  
3. Run the cells and provide your MP3 file path when prompted.

---

## 🔧 Sample Output

```text
Enter path to your audio file (e.g., 'audio.mp3'): my_audio.mp3
Transcribing using Whisper base model...

Transcription Output:
Hello, this is a test of OpenAI's Whisper speech recognition system.

Transcription saved to 'transcription.txt'
```

---

## 📌 Notes

- Whisper automatically detects the spoken language.  
- For longer or complex audio files, use the `small` or `medium` models  
  (Note: Larger models require more memory).

---

## 📄 License

This project is open-source and uses the [MIT License](LICENSE).
