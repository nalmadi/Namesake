# ⚠️ Namesake
## _A Checker of Lexical Similarity in Identifier Names_
![GitHub top language](https://img.shields.io/github/languages/top/nalmadi/Namesake?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/nalmadi/Namesake?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/nalmadi/Namesake?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/nalmadi/Namesake?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/nalmadi/Namesake?style=for-the-badge)

Namesake is an open-source tool for assessing confusing naming combinations in Python programs.
Namesake flags confusing identifier naming combinations that are similar in:
* orthography (word form)
* phonology (pronunciation)
* or semantics (meaning).

## 💡 What is Lexical Similarity in Code?

Orthographic similarity focuses on the the similarity in word form on the level of letters. Not to be confused by editing distance or Levenshtein's distance, where one letter is replaced by another, orthographic similarity focuses on the similarities between letters shapes.  A good example is the confusion between `O' and `C' as individual letters or within words and sentences. Here's a common exmple in code:
![Orthographic similarity](/documentation/imgs/ortho_example.drawio.png)


Phonological similarity describes two words that share a similar or identical pronunciation, also known as homophones:
![Orthographic similarity](/documentation/imgs/ortho_example.drawio.png)


Orthographic similarity focuses on the the similarity in word form on the level of letters.
![Orthographic similarity](/documentation/imgs/ortho_example.drawio.png)


## ⚙️ Installing Namesake:
first, to install the requirements:

```sh
pip install -r /namesake/requirements.txt
```

## 🚀 Running Namesake:
To run Namesake on the file test1.py

```sh
python namesake.py test1.py
```

## 👀 Example Running Namesake:
![Namesake Example](/documentation/imgs/demo-Namesake.png)

## 📝 Citation:
[Naser Al Madi. 2022. Namesake: A Checker of Lexical Similarity in Identifier
Names. In Proceedings of The 37th IEEE/ACM International Conference on
Automated Software Engineering Workshops (ASEW 2022).](https://www.researchgate.net/publication/362932462_How_Readable_is_Model-generated_Code_Examining_Readability_and_Visual_Inspection_of_GitHub_Copilot)


## ⚖️ License:

MIT **Free Software, Hell Yeah!**
