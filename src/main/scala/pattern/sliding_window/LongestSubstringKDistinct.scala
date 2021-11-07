package pattern.sliding_window

/**
 * Given a string, find the length of the longest substring in it with no more than K distinct characters.
 */
object LongestSubstringKDistinct extends App {

  def findLength(str: String, k: Int): Int = {

    var j: Int = 0
    var characters: Map[Char, Int] = Map.empty

    var maxLen = 0
    str.indices.foreach { i =>
      val ch = str(i)
      characters += ch -> (characters.getOrElse(ch, 0) + 1)

      val len = i - j + 1
      if (characters.size > k) {
        while(characters.size > k) {
          val firstCh = str(j)
          characters = characters.updatedWith(firstCh) {
            case Some(1) => None
            case Some(cnt) => Some(cnt - 1)
          }
          j += 1
        }
      } else {
        if (maxLen < len) {
          maxLen = len
        }
      }
    }

    maxLen
  }


  println(findLength("araaci", 2))
  println(findLength("araaci", 1))
  println(findLength("cbbebi", 3))
  println(findLength("cbbebi", 10))
}
