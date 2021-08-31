# working_with_pyO3

A simple Google Kickstart question solved using Python wrapped Rust.

# What is pyO3?

pyO3 consists of the **Rust bindings for Python, including tools for creating native Python extension modules.**

Resources:-
1. [Github](https://github.com/PyO3/pyo3)
2. [Docs and User Guide](https://pyo3.rs/v0.14.4/)

# The question

The question can be found here: [Arithmetic Square](https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813)

# Features

1. All of the logic is written in src/lib.rs and wrapped as a Python function using pyO3.
2. lib.rs is exported as a Python module, which is imported in the input.py file.
3. The input.py file serves only to take inputs and display the output.
4. No significant decrease in benchmarks is noticed as compared to writing it in pure Rust/pure Python.

# Requirements

1. cargo, rustc and rustup.rs version (1.41 or higher)
2. Python (3.6 or higher)
3. A virtual Python environment is required in the working directory. This must have [maturin](https://github.com/PyO3/maturin) installed on it.

# Why should I do this?

1. Input processing in Rust is a pain. In Python it is easy as pie.
2. Rather than spending time on formatting and getting the input properly, it is much easier and time-saving to focus on Rust by writing just the algorithm in it.
   
# Why shouldn't I do this?

1. Competitive programming websites accept single files with a single language only. Reliance on mutliple files/languages is not allowed.
2. Although a pain, it is important to know how to parse inputs properly in any language.
