package pattern.sliding_window

///**
// * Given a string and a list of words, find all the starting indices of substrings
// * in the given string that are a concatenation of all the given words exactly once
// * without any overlapping of words. It is given that all words are of the same length.
// */
//object WordConcatenation1 extends App {
//
//  def findWordConcatenation(str: String, words: List[String]): List[Int] = {
//    var res: List[Int] = List.empty
//
//    val wordLen = words.head.length
//    var wordMap: Map[String, Int] = words
//      .groupBy(ch => ch)
//      .view.mapValues(_.size)
//      .toMap
//
//    var j: Int = 0
//    var matchCount: Int = 0
//    val groupedStr = str.grouped(wordLen).toArray
//    groupedStr.indices.foreach { i =>
//      val word = groupedStr(i)
//
//      if (wordMap.contains(word)) {
//        wordMap = wordMap.updatedWith(word) { case Some(c) => Some(c - 1) }
//        if (wordMap(word) == 0) {
//          matchCount += 1
//        }
//      }
//
//      if (matchCount == wordMap.size) {
//        res = j :: res
//      }
//
//      if (i >= words.length - 1) {
//        val leftWord = groupedStr(j)
//
//        if (wordMap.contains(leftWord)) {
//          if (wordMap(leftWord) == 0) {
//            matchCount -= 1
//          }
//          wordMap = wordMap.updatedWith(leftWord) { case Some(c) => Some(c + 1) }
//        }
//
//        j += 1
//      }
//    }
//
//    res.reverse.map(_ * wordLen)
//  }
//
//  println(findWordConcatenation("catfoxcat", List("cat", "fox")))
//  println(findWordConcatenation("catcatfoxfox", List("cat", "fox")))
//}



/**
 * Given a string and a list of words, find all the starting indices of substrings
 * in the given string that are a concatenation of all the given words exactly once
 * without any overlapping of words. It is given that all words are of the same length.
 */
object WordConcatenation extends App {

  def findWordConcatenation(str: String, words: List[String]): List[Int] = {
    var res: List[Int] = List.empty

    val wordLen = words.head.length
    var wordMap: Map[String, Int] = words
      .groupBy(ch => ch)
      .view.mapValues(_.size)
      .toMap

    for (i <- 0 until (str.length - words.length * wordLen + 1)) {
      var continue: Boolean = true
      var seen: Map[String, Int] = Map.empty

      for (j <- 0 until words.length if continue) {
        val nextWordIdx = i + j * wordLen
        val word = str.substring(nextWordIdx, nextWordIdx + wordLen)

        if (wordMap.contains(word)) {

          seen = seen.updatedWith(word) {
            case None => Some(1)
            case Some(cnt) => Some(cnt + 1)
          }

          if (seen(word) <= wordMap(word)) {
            if (j == words.length - 1) {
              res = i :: res
            }
          } else {
            continue = false
          }
        } else {
          continue = false
        }
      }
    }

    res.reverse
  }

  println(findWordConcatenation("catfoxcat", List("cat", "fox")))
  println(findWordConcatenation("catcatfoxfox", List("cat", "fox")))
}
