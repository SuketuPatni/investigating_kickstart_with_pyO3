#  investigating_kickstart_with_pyO3

A simple Google Kickstart question solved using Python-wrapped Rust.<br> 
The solutions are also checked and corrected with the model solutions.

# What is pyO3?

pyO3 consists of the **Rust bindings for Python, including tools for creating native Python extension modules.**

Resources:-
1. [Github](https://github.com/PyO3/pyo3)
2. [Docs and User Guide](https://pyo3.rs/v0.14.4/)

# The question

[Arithmetic Square](https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813)

# Features

1. All of the logic is written in src/lib.rs and wrapped as a Python function using pyO3.
2. lib.rs is exported as a Python module, which is imported in the input.py file.
3. The input.py file serves only to take inputs (from text files), display the output and run the 2 tests.
4. No significant decrease in benchmarks is noticed as compared to writing it in pure Rust/pure Python.
5. A very primitive and simple test is used to check if the algorithm works correctly for all given test cases.

# Requirements

1. cargo, rustc and rustup.rs version (1.41 or higher)
2. Python (3.6 or higher)
3. A virtual Python environment is required in the working directory. This must have [maturin](https://github.com/PyO3/maturin) installed on it.

# Running the code

Clone and cd <br>
`git clone https://github.com/SuketuPatni/investigating_kickstart_with_pyO3.git ks_d1_2021`  <br>
`cd ks_d1_2021` <br>
and then run the following:-

## Setting up the Python virtual environment

`python3 -m venv .env` <br/>
followed by
1. `source .env/bin/activate` for Linux
2. `activate` for Windows

## Installing maturin

`pip install maturin`<br/>
`maturin develop`

## Running the file

`python input.py`<br/>

## Deactivating the venv
`deactivate`<br/>