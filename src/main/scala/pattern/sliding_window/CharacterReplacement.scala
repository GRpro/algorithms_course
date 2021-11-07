package pattern.sliding_window

/**
 * Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
 */
object CharacterReplacement extends App {

  def findLength(str: String, k: Int): Int = {
    var j: Int = 0
    var repetitionNum: Map[Char, Int] = Map.empty
    var maxRepetitionNum: Int = 0
    var maxLen: Int = 0

    str.indices.foreach { i =>
      val ch = str(i)
      repetitionNum = repetitionNum.updatedWith(ch) {
        case None => Some(1)
        case Some(num) => Some(num + 1)
      }
      maxRepetitionNum = math.max(maxRepetitionNum, repetitionNum(ch))

      // current window size is from j to i, overall we have a letter which is
      // repeating 'maxRepetitionNum' times, this means we can have a window which has one letter
      // repeating 'maxRepetitionNum' times and the remaining letters we should replace.
      // if the remaining letters are more than 'k', it is the time to shrink the window as we
      // are not allowed to replace more than 'k' letters
      if (i - j + 1 - maxRepetitionNum > k) {
        val leftCh = str(j)
        repetitionNum = repetitionNum.updatedWith(leftCh) {
          case Some(1) => None
          case Some(num) => Some(num - 1)
        }
        j += 1
      }

      maxLen = math.max(maxLen, i - j + 1)
    }

    maxLen
  }

  println(findLength("aabccbb", 2))
  println(findLength("abbcb", 1))
  println(findLength("abccde", 1))
}
