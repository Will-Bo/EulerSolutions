use std::env;

fn main() {

    let args: Vec<String> = env::args().collect();
    let max:i32 = args[1].parse().unwrap();
    println!("Max is {}", max);

//    let nums: [i32; max] = [0; max];

    let mut nums: Vec<i32> = vec![Default::default(); max as usize];
    for element in nums.iter_mut() {
        *element = 0;
    }

    let mut i:i32 = 2;
    let mut n:i32;
    while (i < max){
        n = 1;
        while (n*i < max){
            println!("{} ", n*i);
            n+=1;
        }
        i+=1;
    }
}
