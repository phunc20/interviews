# Vantix
Vantix seems to be part of VinGroup's AI. The interview was divided into two parts:

01. In the first part, I was asked about my favorite projects in the past, how I implemented the solutions, etc. which took about 30 minutes.
02. The second part also took 30 minutes, which was a coding test on algorithms: One single question around leetcode's medium level.

## Coding Question
The question I met was about sth similar to maximum subarray problem: Given an array $L$ (indexed from $0$) of integers of length $n$, try to find the maximum sum of the form
$$
  \sum_{k=0}^{K} (-1)^{k} L_{i+k}\,,
$$
where $i \in [0 .. \texttt{len}(L)-1]$ and $K$ in permissive range.


## Solutions
01. (Succeeded) `alternating_max_sum_subarray.py`
  - This is an almost brute-force solution: We simply go through subarrays which starting index `i = 0` until `len(L) - 1`, for each of which we find an index `j` until which the alternating subarray from `i` to `j` is maximum among all subarrays starting from `i`.
02. (Failed) I wanted to modify Kadanes's algorithm for this question, but it seemed _impossible_?

