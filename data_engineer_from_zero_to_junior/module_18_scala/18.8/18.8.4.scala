// Напишите программу, которая вычисляет факториал заданного пользователем целого числа с использованием цикла while.
// Факториал числа n (обозначается n!) — это произведение всех положительных целых чисел от 1 до n.

object FactorialWhile extends App {
  val number = scala.io.StdIn.readInt()
  var factorial = 1
  var i = 1

  while (i <= number) {
    factorial *= i
    i += 1
  }

  println(factorial)
}