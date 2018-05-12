# Introduction

This is a library to emulate text being typed on the screen.

## Installation

1. From the repo: Download and extract somewhere first.

```bash
pip install -e <path-to-repo>
```

## Usage

#### 1. From code

```python
from sentient_typer import typer 

text = "I am awake now!"
typer(text)

```

#### 2. From cmd line

```bash
# Note running this without any args might incite AI fears

sentient [--inp-file] some_file.txt
```