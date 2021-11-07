package pattern.sliding_window

/**
 * Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
 * You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
 * Write a function to return the maximum number of fruits in both baskets.
 */
object MaxFruitCountOf2Types extends App {


  def findLength(chars: Array[Char]): Int = {
    var maxLen = 0

    var j: Int = 0

    var chSet: Map[Char, Int] = Map.empty
    chars.indices.foreach { i =>
      chSet = chSet.updatedWith(chars(i)) {
        case Some(cnt) => Some(cnt + 1)
        case None => Some(1)
      }

      if (chSet.size > 2) {
        while(chSet.size > 2) {
          chSet = chSet.updatedWith(chars(j)) {
            case Some(1) => None
            case Some(cnt) => Some(cnt - 1)
          }
          j += 1
        }
      } else {
        val len = i - j + 1
        if (maxLen < len) {
          maxLen = len
        }
      }
    }

    maxLen
  }

  println(findLength(Array('A', 'B', 'C', 'A', 'C')))
  println(findLength(Array('A', 'B', 'C', 'B', 'B', 'C')))
}
