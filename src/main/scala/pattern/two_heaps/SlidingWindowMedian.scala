package pattern.two_heaps

import scala.collection.mutable

object SlidingWindowMedian extends App {


  // Given an array of numbers and a number ‘k’,
  // find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
  def findSlidingWindowMedian(nums: Array[Int], k: Int): List[Double] = {
    var maxHeap = mutable.PriorityQueue.newBuilder(Ordering.Int).result()
    var minHeap = mutable.PriorityQueue.newBuilder(Ordering.Int.reverse).result()

    var res: Vector[Double] = Vector.empty

    def rebalanceHeaps(): Unit = {
      if (maxHeap.length > minHeap.length + 1) {
        minHeap.enqueue(maxHeap.dequeue())
      } else if (maxHeap.length < minHeap.length){
        maxHeap.enqueue(minHeap.dequeue())
      }
    }

    nums.indices.foreach { i =>

      // add element
      if (maxHeap.isEmpty || maxHeap.head > nums(i)) {
        maxHeap.enqueue(nums(i))
      } else {
        minHeap.enqueue(nums(i))
      }
      rebalanceHeaps()

      if (i >= k - 1) {
        // add median to res list
        val e = if (maxHeap.length == minHeap.length) {
          (maxHeap.head + minHeap.head) / 2.0
        } else {
          maxHeap.head
        }
        res = res.appended(e)

        // remove element
        val eToRemove = nums(i - k + 1)
        if (eToRemove <= maxHeap.head) {
          var removed = false
          maxHeap = maxHeap.filterNot { e =>
            if (removed) false
            else {
              if (e == eToRemove) {
                removed = true
                true
              } else {
                false
              }
            }
          }
        } else {
          var removed = false
          minHeap = minHeap.filterNot { e =>
            if (removed) false
            else {
              if (e == eToRemove) {
                removed = true
                true
              } else {
                false
              }
            }
          }
        }
      }
    }

    res.toList
  }



  var res1 = findSlidingWindowMedian(Array[Int](1, 2, -1, 3, 5), 2)
  System.out.println(s"Sliding window medians are: $res1")

  val res2 = findSlidingWindowMedian(Array[Int](1, 2, -1, 3, 5), 3)
  System.out.println(s"Sliding window medians are: $res2")
}