package pattern.sliding_window

/**
 * Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
 */
object MinimumWindowSubstring extends App {

  def findSubstring(string: String, substring: String): String = {
    var resI: Int = 0
    var resJ: Int = 0
    var resLen: Int = -1

    var j: Int = 0
    var smallest: String = ""

    var symbols: Map[Char, Int] = substring
      .groupBy(ch => ch)
      .view.mapValues(_.length)
      .toMap

    var matchCount: Int = 0
    string.indices.foreach { i =>
      val ch = string(i)
      if (symbols.contains(ch)) {
        symbols = symbols.updatedWith(ch) {
          case Some(c) => Some(c - 1)
        }
        if (symbols.get(ch).contains(0)) {
          matchCount += 1
        }
      }

      if (matchCount == symbols.size) {

        // try to narrow the window
        while(matchCount == symbols.size) {
          if (resLen == -1 || resI - resJ > i - j) {
            resI = i
            resJ = j
          }

          val leftCh = string(j)
          if (symbols.contains(leftCh)) {
            if (symbols(leftCh) == 0) {
              matchCount -= 1
            }
            symbols = symbols.updatedWith(leftCh) { case Some(c) => Some(c + 1) }
          }

          j += 1
        }
      }
    }

    if (resLen != -1) {
      string.substring(resJ, resI + 1)
    } else ""
  }

  println(findSubstring("aabdec", "abc"))
  println(findSubstring("abdbca", "abc"))
  println(findSubstring("adcad", "abc"))
}
