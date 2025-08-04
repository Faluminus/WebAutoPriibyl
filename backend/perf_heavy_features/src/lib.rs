use pyo3::prelude::*;
use std::cmp::min;

// This can be implemented and added into autocomplete if performance improvement is needed.
// THIS WILL AFFECT THE QUALITY OF AUTOCOMPLETE NEGATIVELY BUT SPEED IT UP
#[allow(dead_code)]
fn prefix_filtering() -> Vec<String> {
    return vec!["None".to_string()];
}

fn damerau_levenshtein_distance(query: &str, target: &str) -> u16 {
    //Created matrix
    let mut dp: Vec<Vec<u16>> = vec![vec![0; target.len()]; query.len()];

    //Initialized the matrix
    for i in 0..query.len() + 1 {
        dp[i][0] = i as u16;
    }
    for j in 0..target.len() + 1 {
        dp[0][j] = j as u16;
    }

    //Table population using damerau levenshtein alg
    for i in 1..query.len() {
        for j in 1..target.len() {
            if query.as_bytes()[i - 1] == target.as_bytes()[j - 1] {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min(dp[i - 1][j],min(dp[i][j - 1], dp[i-1][j-1]));
            }
        }
    }

    //Returns the final distance
    return dp[query.len()][target.len()];
}

#[pyfunction]
fn search_autocomplete(
    query: &str,
    listings: Vec<String>,
    num_of_best_matches: u16,
    max_distance: u16,
) -> Vec<String> {
    let mut match_vec: Vec<(String, u16)> = Vec::new();
    for item in listings.iter() {
        let item_distance: u16 = damerau_levenshtein_distance(&item, query);
        if item_distance >= max_distance {
            continue;
        }
        for (i, (_, distance)) in match_vec.iter().enumerate() {
            if item_distance <= *distance {
                match_vec.insert(i, (item.clone(), item_distance));
                break;
            }
        }
    }
    match_vec = match_vec[0..num_of_best_matches as usize].to_vec();
    let mut final_vec: Vec<String> = Vec::new();
    for (item, _) in match_vec.iter() {
        final_vec.push(item.clone());
    }
    return final_vec;
}

#[pymodule]
fn perf_heavy_features(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(search_autocomplete, m)?)?;
    Ok(())
}
