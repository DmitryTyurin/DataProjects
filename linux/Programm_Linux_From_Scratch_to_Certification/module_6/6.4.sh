#– Создайте папку с именем «Favorite_movies» в домашнем каталоге вашего пользователя.
#- Измените свою текущую локацию на новую папку, которую вы только что создали.
#- Создайте там файл с именем «my_top_10_movies.txt».
#- Заполните файл своими любимыми фильмами.
#- Выведите в окно терминала содержимое файла командой more.

cd /home
mkdir Favorite_movies
cd Favorite_movies/
cat > my_top_10_movies.txt
more my_top_10_movies.txt


#– Создайте папку с именем «Favorite_actors» в домашнем каталоге вашего пользователя.
#- Измените свою текущую локацию на новую папку, которую вы только что создали.
#- Создайте там файл с именем «my_top_10_actors.txt».
#- Заполните файл своими любимыми актерами.
#- Выведите в окно терминала содержимое файла командой more.

mkdir Favorite_actors
cd Favorite_actors/
cat > my_top_10_actors.txt
more my_top_10_actors.txt


#– Переместите файл «my_top_10_movies.txt» в папку «Favorite_actors».
#- Удалите пустую папку «Favorite_movies».
#- Переименуйте папку «Favorite_actors» в «Top_movies_and_actors».

mv my_top_10_movies.txt Favorite_actors
rm -r  Favorite_movies/
mv Favorite_actors Top_movies_and_actors