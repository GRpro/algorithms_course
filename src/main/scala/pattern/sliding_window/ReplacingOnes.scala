package pattern.sliding_window

/**
 * Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
 */
object ReplacingOnes extends App {

  def findLength(arr: Array[Byte], k: Int): Int = {
    var maxLen: Int = 0
    var j: Int = 0

    var count1: Int = 0
    arr.indices.foreach { i =>
      val el = arr(i)
      if (el == 1) {
        count1 += 1
      }

      if (i - j + 1 - count1 > k) {
        val leftEl = arr(j)
        if (leftEl == 1) {
          count1 -= 1
        }
        j += 1
      }


      maxLen = math.max(maxLen, i - j + 1)
    }

    maxLen
  }

  println(findLength(Array(0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1), 2))
  println(findLength(Array(0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1), 3))
}
