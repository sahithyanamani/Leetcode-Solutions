<h1 align="center">Two Sum Problem</h1>

<p align="center">
A classic algorithm problem solved using an efficient Hash Map approach.
</p>

<hr>

<h2>📌 Problem Statement</h2>

<p>
Given an array of integers <b>nums</b> and an integer <b>target</b>, return the indices of the two numbers such that they add up to the target.
</p>

<ul>
<li>You may assume that each input has <b>exactly one solution</b>.</li>
<li>You may <b>not use the same element twice</b>.</li>
<li>You can return the answer in <b>any order</b>.</li>
</ul>

<hr>

<h2>📥 Examples</h2>

<h3>Example 1</h3>

<pre>
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9
</pre>

<h3>Example 2</h3>

<pre>
Input:
nums = [3,2,4]
target = 6

Output:
[1,2]
</pre>

<h3>Example 3</h3>

<pre>
Input:
nums = [3,3]
target = 6

Output:
[0,1]
</pre>

<hr>

<h2>⚙️ Constraints</h2>

<ul>
<li>2 ≤ nums.length ≤ 10<sup>4</sup></li>
<li>-10<sup>9</sup> ≤ nums[i] ≤ 10<sup>9</sup></li>
<li>-10<sup>9</sup> ≤ target ≤ 10<sup>9</sup></li>
<li>Only one valid solution exists.</li>
</ul>

<hr>

<h2>💡 Approach</h2>

<p>
The optimal solution uses a <b>Hash Map</b> to store numbers and their indices while iterating through the array.
</p>

<ul>
<li>For each element, calculate the <b>complement</b> = target − current number.</li>
<li>Check if the complement already exists in the map.</li>
<li>If it exists, return the stored index and the current index.</li>
<li>Otherwise, store the current number and its index in the map.</li>
</ul>

<hr>

<h2>🧠 Time & Space Complexity</h2>

<table border="1" cellpadding="6">
<tr>
<th>Complexity</th>
<th>Value</th>
</tr>
<tr>
<td>Time Complexity</td>
<td>O(n)</td>
</tr>
<tr>
<td>Space Complexity</td>
<td>O(n)</td>
</tr>
</table>

<hr>

<h2>💻 Python Implementation</h2>

<pre>
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
</pre>

<hr>

<h2>🚀 Key Concepts</h2>

<ul>
<li>Hash Map</li>
<li>Array Traversal</li>
<li>Complement Lookup</li>
<li>Optimal O(n) Solution</li>
</ul>

<hr>

<p align="center">
⭐ If you find this repository helpful, consider giving it a star!
</p>
