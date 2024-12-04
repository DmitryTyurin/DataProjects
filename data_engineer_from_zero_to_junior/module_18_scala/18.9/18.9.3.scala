// Напишите функцию, которая принимает список целых чисел и возвращает их сумму.
// Условия:
// Входные данные: список целых чисел List[Int].
// Выходные данные: сумма чисел в списке.

object SumList {
  def sumList(numbers: List[Int]): Int = {
    // Вычисление суммы списка
    numbers.sum
  }

  def main(args: Array[String]): Unit = {
    val input = scala.io.StdIn.readLine()

    // Разделение строки на список чисел
    val numbersList = input.split(",").map(_.trim.toInt).toList

    println(sumList(numbersList))
  }
}