# Word Heat Generator

This Python program generates 5-letter words on a **realism scale from 0 to 5**, simulating how close a randomly generated string gets to being a real English word. It dynamically tightens constraints based on the chosen "heat" level and tracks how many iterations and how much time it takes to find a match.

##  Heat Levels

- **0** – Completely random 5-letter string. Always accepted.
- **1–4** – Gradually increasing realism:
  - Words must start with the first `n` letters of a real 5-letter English word.
  - Example: Heat 3 → Must match the first 3 letters of some real word.
- **5** – Only real 5-letter English words are accepted (from the NLTK corpus).

## Metrics

Each run will display:
- The valid word found
- Number of random attempts (tries)
- Elapsed time to find the valid word

### Example output:

|Generated Word | marge|
|--------------|----------------------|
|Tries| 189 |
|Time| 0.00 seconds|


##  Requirements

- Python 3.x
- `nltk` library

Install dependencies with:
```bash
pip install nltk
```

##  Installation

```bash
git clone https://github.com/cosminelulul/word-heat
cd word-heat
python main.py
