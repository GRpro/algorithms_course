package pattern.sliding_window

/**
 * Given a string and a pattern, find all anagrams of the pattern in the given string.
 * Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N! permutations (or anagrams) of a string having N characters.
 */
object StringAnagrams extends App {

  def findStringAnagrams(str: String, pattern: String): List[Int] = {
    var res: List[Int] = List.empty

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
        res = j :: res
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

    res.reverse
  }

  println(findStringAnagrams("ppqpq", "pq"))
  println(findStringAnagrams("ppqp", "pq"))
  println(findStringAnagrams("abbcabc", "abc"))
}
