#  investigating_kickstart_with_pyO3

A simple Google Kickstart question solved using Python-wrapped Rust. Further, a testing mechanism is also included. <br/>
Not only does this project focus on solving the problem, it also focuses on simulating checking the correctness <br/>
of the solution as observed in real-time Google Kickstart rounds.

# What is pyO3?

pyO3 consists of the **Rust bindings for Python, including tools for creating native Python extension modules.**

Resources:-
1. [Github](https://github.com/PyO3/pyo3)
2. [Docs and User Guide](https://pyo3.rs/v0.14.4/)

# The question

The question (as well as the test case text files) can be found here: [Arithmetic Square](https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813)

# Features

1. All of the logic is written in src/lib.rs and wrapped as a Python function using pyO3.
2. lib.rs is exported as a Python module, which is imported in the input.py file.
3. The input.py file serves only to take inputs, display the output and run the 2 tests.
4. No significant decrease in benchmarks is noticed as compared to writing it in pure Rust/pure Python.
5. A very primitive and simple test is used to check if the algorithm works correctly for all given test cases.

# Requirements

1. cargo, rustc and rustup.rs version (1.41 or higher)
2. Python (3.6 or higher)
3. A virtual Python environment is required in the working directory. This must have [maturin](https://github.com/PyO3/maturin) installed on it.

# Running the code

Download the code as a zip file and extract it in a working directory named "ks_d1_2021". <br/>
Giving any other name will lead to errors. Run the following code in it. 

## Setting up the Python virtual environment

`python3 -m venv .env` <br/>
Then, <br/>
1. `source .env/bin/activate` for Linux systems.
2. `activate` for Windows systems.

## Installing maturin

`pip install maturin`<br/>
`maturin develop`

## Running the file

`python input.py`<br/>

## Deactivating the venv
`deactivate`<br/>

# Why should I do this?

1. Input processing in Rust is a pain. In Python, it is incredibly easy.
2. Rather than spending time on formatting and getting the input properly, it is much easier and time-saving to focus on Rust by writing just the algorithm in it.
3. It allows for better debugging on what went wrong in a particular test case, unlike in competitions, where no specifics are mentioned.
   
# Why shouldn't I do this?

1. Competitive programming websites accept single files with a single language only. Reliance on mutliple files/languages is not allowed.
2. Although a pain, it is important to know how to parse inputs correctly in any language.
3. Testing, although beneficial to do locally, is overkill for competitive programming; websites/platforms generally perform it for you.
