# gTTS - Text-to-Speech Conversion from Text Files

### What is gTTS?
gTTS is a tool that converts text files into MP3 audio files using Google Translate’s text-to-speech API, akin to the functionality found on [Google Translate](https://translate.google.com).

### Installation

```bash
pip install gTTS
gtts-cli --all # Test/check all available languages
```

### How to Use

1. **Prepare your input:**
    Create an `input.txt` file. Each sentence should be separated by a new line.

    **Example:**
    ```plaintext
    # Comments are ignored when generating the MP3 file.
    Speaking in public demands confidence, eloquence, and preparation.
    An orator captivates, inspires, persuades, impresses, and influences.
    The audience listens attentively, evaluates, criticizes, and appreciates.
    - Mastering the art of oration requires practice, patience, perseverance.
    - Delivering an impeccable speech demands precise diction, perfection.
    ```

2. **Run the script:**
    Use the following commands in your terminal.

    For line-by-line processing:
    ```sh
    python gtts_lines.py input.txt "en"
    ```

    For file-based processing:
    ```sh
    python gtts_file.py input.txt "en"
    ```
