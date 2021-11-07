package pattern.sliding_window

/**
 * Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
 */
object MaxSumSubArrayOfSizeK extends App {

  def calculate(inputArray: Array[Int], k: Int): Int = {
    var j: Int = 0

    var maxSum: Int = 0
    var sum: Int = 0
    inputArray.indices.foreach { i =>
      sum += inputArray(i)
      if (i - j + 1 == k) {
        if (maxSum < sum) {
          maxSum = sum
        }
        sum -= inputArray(j)
        j += 1
      }
    }

    maxSum
  }

  val inputArray = Array(2, 3, 4, 1, 5)
  val k = 2
  println(calculate(inputArray, k))
}
