package pattern.sliding_window

/**
 * Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
 */
object AverageOfSubarrayOfSizeK extends App {

  def calculate(inputArray: Array[Int], k: Int): Array[Double] = {
    val res = Array.ofDim[Double](inputArray.length - k + 1)

    var i: Int = 0
    var j: Int = 0

    var windowSum: Int = 0
    while (i < inputArray.length) {
      windowSum += inputArray(i)
      if (i - j + 1 == k) {
        res(j) = (windowSum / k).toDouble
        windowSum -= inputArray(j)
        j += 1
      }
      i += 1
    }

    res
  }

  val inputArray = Array(1, 3, 2, 6, -1, 4, 1, 8, 2)
  val k = 5
  println(calculate(inputArray, k).mkString(","))
}
