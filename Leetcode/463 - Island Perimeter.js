// https://leetcode.com/problems/island-perimeter/
// Tags - Hash Table

/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    if(!grid.length || !grid[0].length)
        return 0
    
    let land = 0
    let border = 0
    
    for(let r=0; r<grid.length; r++)
        for(let c=0; c<grid[0].length; c++){
            if(grid[r][c]===1){
                land++
                if((r< grid.length-1) && grid[r+1][c]===1)
                    border++
                if((c< grid[0].length-1) && grid[r][c+1]===1)
                    border++
            }
        }
    return (4*land - 2*border)
};
