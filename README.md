# gtts-mp3
### Google Text-to-Speech Conversion from Text to MP3 Files

### What is gtts-mp3 ?
**This tool uses [gTTS](https://gtts.readthedocs.io/en/latest/cli.html)** to convert text files to **MP3 audio** files using Google's Text-to-Speech API Translate, which is the command line version for the [Google Translate](https://translate.google.com).

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
    Use one of the following commands in your terminal.

    For line-by-line processing:
    ```sh
    python gtts_lines.py input.txt "en"
    ```

    For file-based processing:
    ```sh
    python gtts_file.py input.txt "English"
    ```
