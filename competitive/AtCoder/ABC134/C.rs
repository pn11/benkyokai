use std::io;
use std::collections::HashMap;

fn main()  {
    let mut line = String::new();
    io::stdin().read_line(&mut line).ok();
    let N = line.trim().parse::<i64>().unwrap();
    let mut A_hash: HashMap<i64, i64> = HashMap::new();
    for i in 0..N{
        let mut line = String::new();
        io::stdin().read_line(&mut line).ok();
        let a = line.trim().parse::<i64>().ok().unwrap(); 
        A_hash.insert(i, a);
    }

    let mut A_vec: Vec<_> = A_hash.iter().collect();
    A_vec.sort_by(|a, b| b.1.cmp(a.1));

    let max_index = A_vec[0].0;
    let max_num = A_vec[0].1;
    let second_max_num = A_vec[1].1;

    for i in 0..N{
        if i == *max_index{
            println!("{}", second_max_num);
        }
        else{
            println!("{}", max_num);
        }
    }
}
