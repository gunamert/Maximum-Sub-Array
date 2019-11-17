# Maximum-Sub-Array



We can find the maximum possible sum of the adjacent array A [1 ... n] of a series of numbers of a certain size by means of the Maximum subarray problem.
When we look at the example below, we see that the maximum sub-array is scanned in yellow. For the given array, the largest sum of contiguous sub-arrays [4, -1, 2, 1] is a total of 6.

The program work in O(n), O(nlogn) and O(n^2) time.

Brute force is an algorithm that uses step by step applications to solve the problem, it is seen as a simple approach by looking at the expression of the problem.
For major problems (sorting, searching, sequence matching, etc.), the brute-force approach provides reasonable algorithms with practical values, without limiting sample size. 
Brute force algorithm can still be useful for solving small-size instances of a problem. The Brute force algorithm solves the problem in a simple, direct and clear way.

The array starts at 0 and we can calculate the sum of each possible sub-sequence starting with element A [0] as shown in the figure above. 
We then calculate the sum of each possible sub-sequence starting with A [1], A [2]. We can say that this is not a very good method, because as the array size increases, the number of possible subarrays increases, thus increasing the computational complexity.
