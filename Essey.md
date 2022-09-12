# реферат


### _Урок 1. Знакомство с контролем версий (лекции)_  
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
### _Урок 2. Установка и настройка системы контроля версий_

1. проверяем установлен ли гит:  
`git --version` . 
git   version 2.32.1 (Apple Git-133)
1. если нет, то `git init`  
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
8. "вытолкнуть" изменения на GitHub
   `git push`
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
Создание репозиториев

1. Создание своего репозитория с нуля (push -u origin master)
2. Клонирование удаленного репозитория ( clone)
3. Участие в чужом проекте (Fork)

Как создать удаленный репозиторий (на примере Github)
Вы создали локальный репозиторий, теперь, например, вам нужно добавить его на Github, тем самым вы фактически создадите удаленный репозиторий.

Перейдите на https://github.com и войдите в свой аккаунт. Нажмите кнопку New repository (Новый репозиторий). На открывшейся странице введите имя репозитория (Repository name) и нажмите кнопку Create repository.

В своем локальном репозитории теперь выполните команду:

git remote add origin https://github.com/username/myproject.git
Данная команда добавит удаленный репозиторий с именем origin, который указывает на ваш Github-репозиторий. Пока мы только добавили запись об удаленном репозитории.

Теперь можно выполнить команду git push, чтобы отправить все ваши изменения на удаленный репозиторий:

git push -u origin master
Вам нужно будет ввести логин и пароль аккаунта в Github. Результат команды будет примерно следующим:

$ git push -u origin master
Username for 'https://github.com': youremail@email.com
Password for 'https://youremail@email.com@github.com':
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 252 bytes | 252.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote: https://github.com/username/myproject/pull/new/master
remote:
To https://github.com/username/myproject.git
* [new branch] master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
В команде git push мы использовали ключ -u. Данный ключ используется для того, чтобы связать локальную ветку master с удаленной origin/master (в нашем случае удаленной ветки не существовало, она автоматически была создана). Так как связь установлена, то последующие выполнения git push из ветки мастер можно выполнять без указания веток. То есть вместо git push origin master), можно просто выполнять команду git push.