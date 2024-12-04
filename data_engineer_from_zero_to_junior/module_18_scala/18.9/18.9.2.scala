// Напишите функцию, которая проверяет, является ли заданное число простым.
// Простое число — это число, большее 1, делящееся только на 1 и само на себя.
// Условия:
// Входные данные: целое число n.
// Выходные данные: логическое значение (true или false), указывающее, является ли число n простым.

object PrimeCheck {
  def isPrime(n: Int): Boolean = {
    if (n <= 1) return false
    if (n <= 3) return true

    if (n % 2 == 0 || n % 3 == 0) return false

    var i = 5
    while (i * i <= n) {
      if (n % i == 0 || n % (i + 2) == 0) return false
      i += 6
    }
    true
  }

  def main(args: Array[String]): Unit = {
    val n = scala.io.StdIn.readInt()
    println(isPrime(n))
  }
}