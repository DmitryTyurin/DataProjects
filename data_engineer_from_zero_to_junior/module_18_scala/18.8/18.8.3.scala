// На вход программы подаётся два числа n и step.
// Напишите программу, которая выводит все числа от 1 до n, включительно, с шагом step использованием цикла for.

object PrintNumbersFor extends App {
  val n = scala.io.StdIn.readInt()
  val step = scala.io.StdIn.readInt()

  for (i <- 1 to n by step) {
    println(i)
  }
}