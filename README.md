## Largest subsquare 

### assumption 
For more clarity, you can find below the mathematical description of the problem from wikipedia. 

* Probleme assumption :  https://en.wikipedia.org/wiki/Maximum_subarray_problem

* The probleme describe in wikipidia docs is a one dim array, so we will take the same concept and 
extend it to a 2D array.

* Solution idea : the maximum sum subarray problem is the task of finding a contiguous 
subarray with the largest sum, within a given two-dimensional array A[1...n, 1...m] of numbers. 

* Time complexity  : k * O(n*m) where  n is nbr rows , m is the nbr of columns and k the nbr of 
time we pass thru the matrix (we repeat the loop in ). but since k is a cst so it's an O(n*m).


## usage 
```cmd
python find_square.py --input  test_files\file1.txt,test_files\file2.txt 
```
-- input  : file path, can be one or many and most be separeted by a comma ','.
In the above sample test_files\file1.txt and test_files\file2.txt are two files located in the test_files folder juste for the purpose of this task. 
Nota : map_gen.py file was used to generate those test files.
## License

MIT
[wiki]: https://en.wikipedia.org/wiki/Maximum_subarray_problem
