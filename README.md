# Hindi–English Dictionary (Python + JSON)

A command-line Hindi–English dictionary application built using Python and JSON, with support for **bidirectional word lookup**, **dynamic word addition**, and **text-to-speech pronunciation**.

The dictionary persists data using a JSON file and allows users to extend it during runtime.

---

## Features
- Search words in **Hindi → English**
- Search words in **English → Hindi**
- JSON-based persistent dictionary storage
- Add new words dynamically to the dictionary
- Input validation for all yes/no and option-based prompts
- Pronounces the entire dictionary using **Google Text-to-Speech (gTTS)**
- Automatically plays generated audio files (Windows)

---

## How the Program Works
1. Loads the dictionary from `hindi_english_dict.json`
   - If the file does not exist, a default dictionary is created
2. User enters a word in **Hindi or English**
3. Program:
   - Displays the translation if found
   - Handles both Hindi and English lookups
4. If the word is not found:
   - User is prompted to add it to the dictionary
5. New words are saved permanently to the JSON file
6. User can choose to:
   - Continue searching
   - Add more words
   - Pronounce the entire dictionary aloud

---

## Technologies Used
- Python
- JSON (file-based storage)
- `gTTS` (Google Text-to-Speech)
- `os` module for audio playback

---

## How to Run

### 1. Install dependencies
```bash
pip install gtts
```
```bash
python hindi_eng_dict.py 
```
## Example Usage
### Searching a word
```bash
Enter the word in Hindi or English: paani
The meaning of your word in English is: Water
```
## Adding a new word
```bash
Word not found in dictionary.
Do you want to add the word? yes
What language is this word (H/E): h
Enter the meaning of the word in English: milk
New word added successfully!
```
## Input Validation

### Ensures valid input for:

- `yes / no`

- Language selection `(h / e)`

- #### Re-prompts user until valid input is entered

## Pronunciation Feature

- The program can pronounce all dictionary entries

- Generates an `mp3` file containing:

```bash
<hindi word> means <english word> in english
```


- Audio is automatically played after generation

## Code Structure Overview

- Dictionary loaded using `json.load()`

- Custom helper functions:

- `yesnocheck()` → validates yes/no input

- `optcheck()` → validates language selection

- JSON file updated using `json.dump()`

- `gTTS` used for speech synthesis

## Limitations

- Audio playback `(os.startfile)` is **Windows-only**

- No validation for incorrect spellings

- Pronunciation uses Hindi language setting for all output
