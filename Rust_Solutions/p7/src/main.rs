use std::env;

// Using the Sieve of Eratosthenes to find a large number of prime numbers and store them in an
// array, then use that array to answer the problem
// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
//
// Use: cargo run -- `num`
// Where `num` is an absurdly large number --- this can be arbitrary
// At the moment, I have no way of knowing how large of a number I need to generate before I find
// the necessary prime, so I like to use cargo run -- 100000000
fn main() {

    let args: Vec<String> = env::args().collect();
    let max:i64 = args[1].parse().unwrap();
    println!("Finding primes below {}", max);

    // initializing the vector of prime indicators
    let mut nums: Vec<i64> = vec![Default::default(); max as usize];
    for element in nums.iter_mut() {
        *element = 0;
    }

    // declaring an empty vector to hold the primes that we find
    let mut primes: Vec<i64> = vec![Default::default()];

    let mut i:i64 = 2;
    let mut n:i64;
    while i < max {
        n = 1;
        while n*i < max {
            nums[(n*i) as usize] = 1;
            n+=1;
        }
        // Adding this prime to the list
        primes.push(i);
        // Finding the next prime
        while i < max && nums[i as usize] != 0 {
            i += 1;
        }
    }


    // `primes` is our list of the prime numbers
    // primes[1] is the first prime number, which is 2
    // The list is prefixed with 0: primes[0] = 0

    // This is the answer to the problem
    let prime:i64 = 10001;
    println!("The {}st/nd/th prime is {}", prime, primes[prime as usize]);
}
