// Создайте изменяемый массив с 5 элементами, от 1 до 5, измените значение одного из элементов и выведите все элементы на экран.

object ArrayExample extends App {
  val numbers = Array(1, 2, 3, 4, 5)

  numbers(2) = 10

  println("Измененный массив:")
  for (number <- numbers) {
    println(number)
  }
}