package pattern.sliding_window

/**
 * Given a string, find the length of the longest substring, which has no repeating characters.
 */
object NoRepeatSubstring extends App {

  def findLength(str: String): Int = {
    var j: Int = 0

    var maxLen: Int = 0

    var chars: Set[Char] = Set.empty
    str.indices.foreach { i =>
      val ch = str(i)
      if (chars(ch)) {
        while(chars(ch)) {
          chars -= str(j)
          j += 1
        }
      } else {
        chars += ch
      }

      val len = i - j + 1
      if (maxLen < len) {
        maxLen = len
      }
    }

    maxLen
  }

  println(findLength("aabccbb"))
  println(findLength("abbbb"))
  println(findLength("abccde"))
}
