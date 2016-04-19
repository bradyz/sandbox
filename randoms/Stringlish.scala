object Stringlish {

  def main (args: Array[String]): Unit = {
    val test = "What is the length of the word 'test'"
    val bad_test = "What is thasdfasdfe length of the word 'test'"
    val proptypeexpr = "What is the (.*) of the (.*) '(.*)'".r

    def isValidQuery (toMatch: String) = toMatch match {
      case proptypeexpr(property, kind, expression) => {
        val rightKind = kind match {
          case "word" => true
          case "sentence" => true
          case _ => false
        }

        rightKind
      }
      case _ => false
    }

    println(isValidQuery(test));
    println(isValidQuery(bad_test));
  }
}

