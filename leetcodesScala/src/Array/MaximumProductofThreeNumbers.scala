/**
  * Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
  */

import scala.math

object MaximumProductofThreeNumbers {
    def maximumProduct(nums: Array[Int]): Int = {
        val nums_sorted = nums.sorted.reverse
        val candidate1 = nums_sorted(0) * nums_sorted(1) * nums_sorted(2)
        val candidate2 = nums_sorted(0) * nums_sorted(nums.length - 2) * nums_sorted.last
        if(candidate1 > candidate2) candidate1 else candidate2
    }

    def maximumProductSingleScan(nums: Array[Int]): Int = {
        var max1, max2, max3 = Integer.MIN_VALUE
        var min1, min2 = Integer.MAX_VALUE

        for(num <- nums){
            if(num >= max1){
                max3 = max2
                max2 = max1
                max1 = num
            }else if(num >= max2){
                max3 = max2
                max2 = num
            }else if(num >= max3){
                max3 = num
            }
            if (num <= min1 ){
                min2 = min1
                min1 = num
            }else if(num <= min2){
                min2 = num
            }
//            println(max1, max2, max3, min1, min2)
        }

        val candidate1 = max1 * max2 * max3
        val candidate2 = max1 * min1 * min2
        if(candidate1 > candidate2) candidate1 else candidate2
    }

    def main(args: Array[String]): Unit = {
        println(maximumProductSingleScan(Array( -1,-2,-3, -4)))
    }
}