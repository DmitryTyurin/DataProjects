// Создайте изменяемое множество с несколькими элементами, а именно с числами от 1 до 4, добавьте новый элемент и удалите один из существующих элементов.
// Выведите все элементы множества на экран.

import scala.collection.mutable.Set

object MutableSetExample extends App {
  val mutableSet = Set(1, 2, 3, 4)

  mutableSet += 5
  mutableSet -= 3

  println("Измененное множество:")
  println(mutableSet)
}