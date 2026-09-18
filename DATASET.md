# Dataset

## Dataset Name

**CodeSearchNet**

## Overview

CodeSearchNet is a dataset and benchmark designed for research on understanding the relationship between **source code and natural language**.

The primary dataset contains approximately **2 million comment–code pairs** collected from open-source libraries. Each pair contains a natural-language comment or documentation string associated with a function or method.

## Programming Languages

The dataset includes code from:

* Python
* Java
* JavaScript
* Ruby
* Go
* PHP

## Dataset Contents

Each dataset record can contain information such as:

* Repository
* File path
* Function or method name
* Programming language
* Source code
* Code tokens
* Documentation/comment
* Documentation tokens

The data is provided in JSON Lines format in the original CodeSearchNet project.

## Relevance to CodeAI Assistant

CodeSearchNet is relevant to our **Generative AI-Based Code Explanation & Documentation Assistant** because it provides examples connecting **programming code with natural-language descriptions**.

These code–comment pairs are useful for understanding tasks such as:

* Code explanation
* Code documentation
* Code understanding
* Natural-language descriptions of source code
* Code-related AI research

Our current CodeAI Assistant uses **Generative AI through the Gemini API** to perform code analysis. The CodeSearchNet dataset is included as a relevant reference dataset for the project's code-understanding and documentation domain.

## Dataset Source

Official CodeSearchNet repository:

[CodeSearchNet – GitHub](https://github.com/github/CodeSearchNet?utm_source=chatgpt.com)

## Dataset Paper

**CodeSearchNet Challenge: Evaluating the State of Semantic Code Search**

Authors: Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc Brockschmidt.

Published as an arXiv preprint in 2019.

## Citation

```text
@article{husain2019codesearchnet,
  title={{CodeSearchNet} challenge: Evaluating the state of semantic code search},
  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet
          and Allamanis, Miltiadis and Brockschmidt, Marc},
  journal={arXiv preprint arXiv:1909.09436},
  year={2019}
}
```

## Note

The official CodeSearchNet GitHub repository is currently archived and read-only. The complete dataset is large, so this project does not include the full dataset inside the GitHub repository. Instead, this file documents the dataset and provides the official source for reference.
