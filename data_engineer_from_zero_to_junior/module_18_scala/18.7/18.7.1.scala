// Создайте неизменяемый список покупок со значениями Молоко, Хлеб и Яблоки, добавьте новый элемент в начало списка и выведите все элементы на экран.

object ShoppingList extends App {
  // Создаем неизменяемый список покупок
  val shoppingList = List("Молоко", "Хлеб", "Яблоки")

  // Добавляем Сыр в начало списка
  val newShoppingList = "Сыр" :: shoppingList

  println("Список покупок:")
  println(newShoppingList)
}