# реферат


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
`git --version` . 
git   version 2.32.1 (Apple Git-133)
2. смотрим настройки:  
`git config -l`  
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