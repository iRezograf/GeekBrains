# реферат
git remote add origin https://github.com/iRezograf/Lesson3.git
git push --set-upstream origin master


### _Урок Введение в контроль версий (лекции)_  
*(Ильнар Шафигуллин)*

#### Использованые мною материалы
[Лекция Введение в контроль версий](https://gb.ru/lessons/256996)  
[-The same in youtube](https://www.youtube.com/watch?v=g1k48cVIynw&t=61s)  
["Pro Git book" Scott Chacon and Ben Straub](https://git-scm.com/book/ru/v2)  
[Git Documentation](https://docs.github.com/en)  
[Getting Started with Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)    

Доступ к странице со справочной информацией по любой Git-команде:

```
`$ git help <команда>`  
`$ git <команда> --help`  
`$ man git-<команда>`  
```


1. проверяем установлен ли гит:  
`git --version` или
`git status`
git   version 2.32.1 (Apple Git-133)
2. смотрим настройки:  
`git config -l`  
2. возможно придется проинициализировать некоторые параметры:
   ```
   $ git config --global user.name "Rafael Rezyapov"
   $ git config --global user.email Rezograf@gmail.com  
   
   git config -l  
   ...  
   user.email=rezograf@gmail.com  
   user.name=Rafael Rezyapov  
   ...
3. базовый набор сохранения изменений:
- `git status`  
- `git diff`
- `git add Essey-Summary`
- `git commit -m "comment about commit"`
- отправить изменения на сервер  
   `git push`
- создать новую ветку  
   `git branch NewBranch`  
- сделать ее актуальной  
   `git checkout NewBranch`
8. коммитим
   `git commit -m "New branch for new lesson"`  
8. можно даже переименовать последний коммит  
   `git commit --amend -m "Новое имя для последнего коммита"`
9. можно создать локальный клон  
`git clone https://github.com/iRezograf/GeekBrains`  
он создасться в том же каталоге
### _Урок 3. Углубляемся в контроль версий_

##### _Цель: научиться работать с совместными проектами, с размещением репозитория на GitHube для обеспечения доступа коллег_

>##### сделал commit - можешь себе позволить все,
>##### сделал push - можешь позволить себе еще больше ...
1. регистрация на GitHub.ru
1. создание своего репозитория в GitHub
   * создаем рабочий каталог
      * `mkdir Lesson3`
      * `mkfile Essey-Summary.md`
   *  _памятка:_
         > * ##### mkdir "dirname"  
         > * ##### mkfile "filename"
         > * ##### rm -d "dirname"
         > * ##### rm "filename" 
   * открываем его в VSCode 
   * инициализируем git для этого каталога
      * `git init`
   * "привяываем свои "идентификаторы"
      * `$ git config --global user.name "Rafael Rezyapov"`
      * `$ git config --global user.email Rezograf@gmail.com` 
   * готовим дальше
   * `git status`
      * `git add Essey-Summary.md` (или `git add .`)
      * `git commit -m "Initialisation commit"` 
2. твой первый пуш
3. твой первый форк
3. pull request


### MarkDown   
[Basic Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


### Введение в контроль версий (семинары)  
*(19.08 Илья Кротов)*
![](/2.%20Version%20Control/%D0%98%D0%BB%D1%8C%D1%8F_%D0%9A%D1%80%D0%BE%D1%82%D0%BE%D0%B2.png)

[Урок 1. Первое использование контроля версий](https://gb.ru/lessons/257073)  

 
[Git для новичков (часть 2):](https://habr.com/ru/post/542616/)  
...
каждом новом commit следует оставлять коммент и в нем описывать суть изменений.

Переключаться между ветками можно такой командой:  
`git checkout <название_ветки>`  
После того, как вы завершили работу над своей задачей, ветку можно слить в `master` . Для этого нужно переключиться в ветку master и выполнить следующую команду:

```
# Переключаемся в master
git checkout master
# Обновляем локальную ветку с сервера
git pull origin master

# Делаем merge вашей ветки, в ветку в которой вы находитесь
# В данном примере это master
git merge <название_ветки>
```
***Совет❗️*** _Перед тем как сливать новый merge , стоит обновить локальную ветку `master` , во избежания дальнейших проблем._

Команда merge берет все изменения из ветки (например bugFix) и добавляет их в ветку master.

Для того чтобы посмотреть текущее состояние ветки, например, какие файлы добавлены или не добавлены для создания commit, можно выполнить команду:

`git status`  
Другие пользователи не увидят вашу ветку, пока она не будет отправлена на удаленный репозиторий. Поэтому, после того как вы слили все изменения в `master` , нужно отправить их в GitHub. Для этого обязательно нужно находиться в ветке master :

`git checkout master`

### Отправляем наши изменения в GitHub
`git push origin master`  
Теперь все ваши изменения, в ветке master улетели в GitHub. Таким же образом, можно отправить любую другую ветку:

`git checkout <название_ветки>`  
`git push origin <название_ветки>`  

***Совет.*** _Каждый коммит, лучше заливать сразу в удаленный репозиторий. Никто не застрахован, поломки собственного ПК. Поэтому чтобы не потерять все наработки, не забывайте сливать ваши изменения на GitHub._

## Домашнее задание 3
Работа с репозиториями

### Task1. Создание своего репозитория с нуля (push -u origin master)
* `git init`
* `git add .`
* `git commit -m "Initial commit"`
*  зайти на https://github.com/iRezograf/ и создать репозиторий Task1 
```
git remote add origin https://github.com/iRezograf/Task1.git
git branch -M master
git push -u origin master
```

### Task2. Клонирование удаленного репозитория ( clone)
1. Подготовительная работа: создание удаленного репозитория 
* заходим на https://github.com/iRezograf в раздел "your repositiories"
* нажимаем кнопку NEW 
* вводим имя репозитория, например Task2.git
* заполняем остальные поля. Сохраняем/
2. В VSCode открываем новое окно.
3. Выбираем Clont Git Repostory ...
4. В окне вводим/выбираем путь к клонируемому репозиторию, например https://github.com/iRezograf/Task2
5. Создаем этот текст. Сохраняем. Пушим на Github
* `git add Task2.md`
* `git commit -m "Создали файл Task2.md"`
* `git push`
* 
### Task3. Участие в чужом проекте (Fork)
1. Заходим в совместный проект, например:
https://github.com/killkuruzzza/git_lesson_3
2. В верхнем правом углу нажимаем Fork->Create new Fork
3. Создаем свою копию и открываем ее на локальном компьютере. См - `Task2. Клонирование удаленного репозитория ( clone)`
4. Создаем новую ветку, например Task3
   * `git branch RRA_Task3`
   * `git checkout RRA_Task3` 
5. Правим этот файл.
6. Сохраняем, пушим:
   ```
   git add .
   git commit -m "Добавлен файл Task3.md"
   git push --set-upstream origin RRA_Task3
   ```  
7. Заходим на `https://github.com/iRezograf/git_lesson_3`
8. Нажимаем кнопку "Pull Request@

## Введене в языки программирования

### C#
1. Ввод -вывод
```
string s = Console.ReadLine();
Console.WriteLine("input your string");
```
1. Форматированный вывод:
```
Console.WriteLine($"{lengthBetween(points):F2}");
Console.WriteLine( "{0, 10:F2}",lengthBetween(points) );
                     ^
                     |
                     * ----- порядковый номер параметра
```

Скомпилированную порграмму можно уже запустить в каталоге:
```
.\task19\bin\Debug\net6.0\ 
open task19
```


### Знакомство с базами данных

Языки баз данных
В СУБД поддерживается несколько специализированных по своим
функциям подъязыков. Их можно разбить на две категории:
* язык определения данных БД DDL — Data Definition Language;
* язык манипулирования данными DML — Data Manipulation Language). 

[Справочник по Transact-SQL (T-SQL)](https://learn.microsoft.com/ru-ru/sql/t-sql/queries/queries?source=recommendations&view=sql-server-ver16)

Компактные и бесплатные БД  
[MySQL](https://www.mysql.com/)  
[PostgreSQL](https://www.postgresql.org/download/macosx/)

### Python

1. Ввод -вывод
``` 
name = input("Your name: ")  
age = input("Your age: ")
print(f"Name: {name}  Age: {age}")
```

### Java

1. Ввод -вывод
``` 
public  class MainMenu {
    public static void main(String[] args) {
        System.out.println("Наконец-то!!!");
        
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();
          
        System.out.printf("Your number: %d \n", num);
        in.close();        
    }
}
```
2. Скомпилировать
```
javac MainMenu.java
```
3. Запустить
```
java MainMenu
```

### Регулярные выражения

##### Половина хлопот при написании регулярного выражения связана с тем, чтобы оно совпадало в нужных местах. Другая половина — с тем, чтобы регулярное выражение не совпадало в ненужных местах. 
`
https://docs.microsoft.com/ru-ru/dotnet/api/system.text.regularexpressions.regex?view=net-6.0
`