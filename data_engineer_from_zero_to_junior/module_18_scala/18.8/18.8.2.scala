// Напишите программу, которая принимает три целых числа и определяет, какое из них наибольшее. После чего выводит на экран максимальное число.
// В ходе решения необходимо использовать двойные логические условия (блок условных операторов объединенных с помощью && или ||).


object MaxOfThree extends App {

  val num1 = scala.io.StdIn.readInt()
  val num2 = scala.io.StdIn.readInt()
  val num3 = scala.io.StdIn.readInt()

  var maxNum = num1
  if ((num2 > num1) && (num2 > num3)) {
    maxNum = num2
  } else if (num3 > maxNum) {
    maxNum = num3
  }

  println(maxNum)
}