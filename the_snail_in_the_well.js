// GitHub: dark-teal-coder 
// First Published Date: 2022-02-07
// Program Input(s): 
/// (1) an integer representing the well's depth  
// Program Process(es): 
/// (1) using the while loop to calculate the number of days it takes for the snail to climb up the well of an input depth
// Program Output(s): 
/// (1) an integer representing the number of days it takes for the snail to reach the depth 
// Program Description: This program is a solution to the problem "The Snail in the Well" in 23 Code Project in the JavaScript course on SoloLearn. 

////////////////////////////////////////////////////////////////////////////////////////////////////

/*
PROBLEM: The Snail in the Well

The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail to get out of a well with the given depth?

Sample Input: 
31

Sample Output:
6

Explanation: Let's break down the distance the snail covers each day:
Day 1: 7-2=5
Day 2: 5+7-2=10
Day 3: 10+7-2=15
Day 4: 15+7-2=20
Day 5: 20+7-2=25
Day 6: 25+7=32
So, on Day 6 the snail will reach 32 feet and get out of the well at day, without slipping back that night.

Hint: You can use a loop to calculate the distance the snail covers each day, and break the loop when it reaches the desired distance.
*/ 

function main() {
    var depth = parseInt(readLine(), 10);
    let feet = 0; 
    let day = 0; 
    while (feet < depth) {
        feet += 7; 
        // After daytime has passed, if it's already reached the depth, break out before it falls back 2 feets.  
        if (feet >= depth) {
            // After +7 feets, it's another day.  
            day++; 
            break;
        } 
        feet -= 2; 
        // If +7 feets isn't larger than the depth, -2 feets won't be. 
        day++; 
    }
    console.log(day); 
}
