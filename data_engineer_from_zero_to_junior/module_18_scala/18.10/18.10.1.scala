// Напишите функцию высшего порядка filterList, которая принимает список целых чисел и функцию предиката (функцию, которая возвращает Boolean).
// Функция filterList должна возвращать новый список, содержащий только те элементы, для которых предикат возвращает true.

object SumList {
  def filterList(numbers: List[Int], predicate: Int => Boolean): List[Int] = {
    numbers.filter(predicate)
  }

  def main(args: Array[String]): Unit = {
    val input = scala.io.StdIn.readLine()
    // Разделение строки на список чисел
    val numbers = input.split(",").map(_.trim.toInt).toList

    val operator = scala.io.StdIn.readLine()
    val value = scala.io.StdIn.readLine().toInt

    val predicate: Int => Boolean = operator match {
      case ">"  => (x: Int) => x > value
      case ">=" => (x: Int) => x >= value
      case "<"  => (x: Int) => x < value
      case "<=" => (x: Int) => x <= value
      case "==" => (x: Int) => x == value
    }

    val filteredNumbers = filterList(numbers, predicate)
    println(filteredNumbers)
  }
}
