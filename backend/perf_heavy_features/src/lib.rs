use pyo3::prelude::*;
use std::cmp::min;



// This will affect  the quality of autocomplete negatively if there is not enough data
#[allow(dead_code)]
fn prefix_filtering(query: &str, target: Vec<Vec<String>>) -> Vec<Vec<String>> {
    let mut result: Vec<Vec<String>> = Vec::new();
    for entry in target.iter() {
        for token in entry.iter() {
            let length: usize = min(query.len(), token.len());
            if query[0..length] == token[0..length] {
                result.push(entry.clone());
                break;
            }
        }
    }
    return result;
}

fn damerau_levenshtein_distance(query: &str, target: &str) -> u16 {
    //String size
    let length: usize = min(query.len(), target.len());

    //Created matrix
    let mut dp: Vec<Vec<u16>> = vec![vec![0; target.len() + 1]; query.len() + 1];

    //Initialized the matrix
    for i in 0..length + 1 {
        dp[i][0] = i as u16;
        dp[0][i] = i as u16;
    }

    //Table population using damerau levenshtein alg
    for i in 1..length + 1 {
        for j in 1..length + 1 {
            if query.as_bytes()[i - 1] == target.as_bytes()[j - 1] {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
            }
        }
    }

    //Returns the final distance
    return dp[length][length];
}

#[pyfunction]
fn search_autocomplete(
    query: &str,
    listings: Vec<String>,
    num_of_best_matches: u16,
    max_distance: u16,
) -> Vec<String> {
    let mut match_vec: Vec<(String, u16)> = Vec::new();
    for field in listings.iter() {

        let item_distance: u16 = damerau_levenshtein_distance(query, field);
        if item_distance > max_distance {
            continue;
        }
        if item_distance == query.len() as u16 {
            continue;
        }

        if match_vec.len() == 0 {
            match_vec.push((field.clone(), item_distance));
            continue;
        }
        let mut insert_index: usize = 0;
        let mut is_bigger: bool = false;
        for (i, (_, distance)) in match_vec.iter().enumerate() {
            if item_distance < *distance {
                insert_index = i;
                break;
            } else if i == match_vec.len() - 1 {
                is_bigger = true;
                insert_index = i;
            }
        }
        if insert_index == match_vec.len() - 1 && is_bigger {
            match_vec.push((field.clone(), item_distance));
        } else {
            match_vec.insert(insert_index, (field.clone(), item_distance));
        }
    }

    if num_of_best_matches <= match_vec.len() as u16 {
        match_vec = match_vec[0..num_of_best_matches as usize].to_vec();
    }

    let mut final_vec: Vec<String> = Vec::new();
    for (item, _) in match_vec.iter() {
        final_vec.push(item.clone());
    }
    return final_vec;
}

#[pymodule]
fn cpu_bound_features(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(search_autocomplete, m)?)?;
    Ok(())
}
