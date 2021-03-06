#![allow(unused)]
use pyo3::prelude::*;
use std::collections::HashMap;

fn mode(numbers: &[i64]) -> i64 {
    let mut occurrences = HashMap::new();

    for &value in numbers {
        *occurrences.entry(value).or_insert(0) += 1;
    }

    occurrences
        .into_iter()
        .max_by_key(|&(_, count)| count)
        .map(|(val, _)| val)
        .expect("Cannot compute the mode of zero numbers")
}

#[pyfunction]
fn solve(row_01: Vec<i64>, row_02: Vec<i64>, row_03: Vec<i64>) -> PyResult<i64> {

    let mut num_aps: i64 = 0;

    if row_02[0] - row_01[0] == row_03[0] - row_02[0] {
        num_aps += 1;
    }

    if row_01[1] - row_01[0] == row_01[2] - row_01[1] {
        num_aps += 1;
    }

    if row_02[1] - row_01[2] == row_03[2] - row_02[1] {
        num_aps += 1;
    }

    if row_03[1] - row_03[0] == row_03[2] - row_03[1] {
        num_aps += 1;
    }

    let mut sum_vec: Vec<i64> = vec![];

    if (row_01[0] + row_03[2]) % 2 == 0 {
        sum_vec.push(row_01[0] + row_03[2]);
    }

    if (row_01[1] + row_03[1]) % 2 == 0 {
        sum_vec.push(row_01[1] + row_03[1]);
    }

    if (row_01[2] + row_03[0]) % 2 == 0 {
        sum_vec.push(row_01[2] + row_03[0]);
    }

    if (row_02[0] + row_02[1]) % 2 == 0 {
        sum_vec.push(row_02[0] + row_02[1]);
    }

    num_aps += match sum_vec.len() {
        0 => 0,
        1 => 1,
        2 => match sum_vec[0] == sum_vec[1] {
            true => 2,
            false => 1
        },
        _ => {
            let mode = mode(&sum_vec);
            // for i in sum_vec {
            //     if i == mode {
            //         num_aps += 1;
            //     }
            // }
            sum_vec.iter().filter(|&n| *n == mode).count()
        }
    } as i64;

    Ok(num_aps)
}

#[pymodule]
fn ks_d1_2021(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve, m)?)?;
    Ok(())
}
