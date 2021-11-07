package pattern.sliding_window

/**
 * Given a string and a pattern, find out if the string contains any permutation of the pattern.
 * Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
 */
object StringPermutation extends App {

  def findPermutation(str: String, pattern: String): Boolean = {
    var freeChars: Map[Char, Int] = pattern.toList
      .groupBy(ch => ch)
      .view.mapValues(_.size)
      .toMap

    var j: Int = 0
    var matchCount: Int = 0
    str.indices.foreach { i =>
      val ch = str(i)

      if (freeChars.contains(ch)) {
        freeChars = freeChars.updatedWith(ch) { case Some(c) => Some(c - 1) }
        if (freeChars(ch) == 0) {
          matchCount += 1
        }
      }

      if (matchCount == freeChars.size) {
        return true
      }

      if (i >= pattern.length - 1) {
        val leftCh = str(j)

        if (freeChars.contains(leftCh)) {
          if (freeChars(leftCh) == 0) {
            matchCount -= 1
          }
          freeChars = freeChars.updatedWith(leftCh) { case Some(c) => Some(c + 1) }
        }

        j += 1
      }
    }

    false
  }

  println(findPermutation("aabbc", "abc"))
  println(findPermutation("oidbcaf", "abc"))
  println(findPermutation("odicf", "dc"))
  println(findPermutation("bcdxabcdy", "bcdyabcdx"))
  println(findPermutation("aaacb", "acb"))
  println(findPermutation("bbbcas", "bbb"))
  println(findPermutation("ppqp", "pqq")) // ?
}
