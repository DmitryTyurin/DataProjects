//Напишите программу для подсчета среднего балла студентов.
//  Используйте переменные типа var для хранения оценок и переменную типа val для хранения имени студента.
//  Программа должна рассчитывать и выводить средний балл.
//  В коде программы необходимо дозаполнить следующие данные:
//  Имя студента - Alice
//    Оценка по математике - 90
//Оценка по науке - 85
//Оценка по литературе - 88
//Самостоятельно написать формулу расчета среднего значения

object StudentGrades extends App {
  val studentName: String = "Alice"
  var mathGrade: Int = 90
  var scienceGrade: Int = 85
  var literatureGrade: Int = 88

  var averageGrade: Double = (mathGrade + scienceGrade + literatureGrade) / 3.0

  println(s"Студент: $studentName")
  println(s"Математика: $mathGrade, Наука: $scienceGrade, Литература: $literatureGrade")
  println(f"Средний балл: $averageGrade%.2f")
}

