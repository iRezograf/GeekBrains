# реферат

***Урок 1.*** Знакомство с контролем версий — Введение в контроль версий (лекции)
Ильнар Шафигуллин
git https://gb.ru/lessons/256996
https://www.youtube.com/watch?v=g1k48cVIynw&t=61s

Доступ к странице со справочной информацией по любой Git-команде:


 `$ git help <команда>`<br>
 `$ git <команда> --help`<br>
 `$ man git-<команда>`<br>


1. проверка что гит установлен:
   `% git --version`  git   version 2.32.1 (Apple Git-133)
2. `git add Essey-Summary`
3. git diff
4. git commit -m "Убрал расширение md у файла Essay-Summary"
5. можно отправить изменения на сервер
   git push
6. создаем новую ветку<br>
   git branch VersionControl
7. делаем ее актуальной
   git checkout VersionControl
8. коммитим
   git commit -m "New branch for new lesson"
9. можно создать локальный клон git clone https://github.com/iRezograf/GeekBrains он создасться в том же каталоге

*19.08 Илья Кротов*
