use std::env;

// a brute-force solution to the problem
// Usage: cargo run -- `size of maze plus one`
fn main() {
    let args: Vec<String> = env::args().collect();

    // creating a 2D array that represents the maze
    let mut maze: Vec<Vec<u64>> = vec![vec![Default::default(); args[1].parse().unwrap()]; args[1].parse().unwrap()];

    for row in maze.iter_mut(){
        for el in row.iter_mut(){
            *el = 0;
        }
    }

    explore(0, 0, &mut maze);

    println!("The size of the maze is {}", maze.len()-1);
    println!("A maze of size {} has {} routes", maze.len()-1, maze[maze.len()-1][maze.len()-1]);
}

// The brute-force explore function
// each time we visit a corner in the maze, we mark it as having been visited one additional time. 
// We traverse the maze in every possible manner, then return the number of times the bottom corner
// has been visited
fn explore(x:i32, y:i32, maze: &mut Vec<Vec<u64>>){
    let ux:usize = x as usize;
    let uy:usize = y as usize;

    // This is the base case
    if ux==maze.len()-1 && uy == maze[0].len()-1 {
        maze[ux][uy] += 1;
        return;
    }
    // We have reached the maximum x, so we can only move downward to the end
    if ux == maze.len()-1 {
        maze[ux][uy] += 1;
        explore(x, y+1, maze);
        return;
    }
    // we have reached the maximum y, so we can only move right to the end
    if uy == maze[0].len()-1 {
        maze[ux][uy] += 1;
        explore(x+1, y, maze);
        return;
    }
    // We are at a vertex inside the maze, so we have to move both down and to the right separately
    maze[ux][uy] += 1;
    explore(x+1, y, maze);
    explore(x, y+1, maze);
}
