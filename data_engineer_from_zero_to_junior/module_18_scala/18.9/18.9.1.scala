// Напишите рекурсивную функцию, которая вычисляет факториал заданного числа.
// Факториал числа n (обозначается n!) — это произведение всех положительных целых чисел от 1 до n.
// Условия:
// Входные данные: целое число n.
// Выходные данные: факториал числа n.

object FactorialFunction {
  def factorial(n: Int): Int = {
    if (n == 0) 1
    else n * factorial(n - 1)
  }

  def main(args: Array[String]): Unit = {
    val n = scala.io.StdIn.readInt()
    println(factorial(n))
  }
}