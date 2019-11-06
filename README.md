# alfred-did-txt

*An Alfred Workflow to append a timestamed entry to a txt file*

Inspired by [a blog post by Patrick](https://theptrk.com/2018/07/11/did-txt-file/) and the ensuing [thread on Hacker News](https://news.ycombinator.com/item?id=17538697).

## Preferences

The location of your `did.txt` file is specified as Alfred environment variable `{var:filelocation}`.

The editor is set to *MacVim* in the *open file* tile.

## Keywords

### did

*Invoke Alfred* -> enter `did wash the dishes`. This appends `2018-07-21 09:13:14 - wash the dishes` to `{var:filelocation}`.

### didopen

*Invoke Alfred* -> enter `didopen`. This opens the file `{var:filelocation}` in *MacVim*.

## Screenshot

![add did entry](https://github.com/geberl/alfred-did-txt/blob/master/screenshot.png)

## Icon

From [https://icons8.com/icon/6784/todo-list]()
