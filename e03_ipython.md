# Ipython

 >- `ipython`: interactive Python interpreter console, see [here](https://ipython.org/ipython-doc/stable/overview.html)
 >- ipython tutorial: [here](https://ipython.readthedocs.io/en/stable/interactive/index.html)


## Start `ipython`:

 > in the system terminal (Linux) or in the Anaconda Prompt (Windows) write `ipython`.
 ![Lunch ipython](./img/ipython.png)


## Keyboard shortcuts:

 - `TAB` - completes and suggests syntax  
 - `name_object + ?` e.g. `myFunction?` display description (doc string) if available
 - `%hist / %hist n` - displays history of entered commands / with rows numbering
 - `ctrl + o` - put a new line behind the cursor
 - `ctrl + a` - moves the cursor to the beginning of the line
 - `ctrl + e` - moves the cursor to the end of the line
 - `ctrl + l` - cleans screen
 - `ctrl + c` - interrupts the current action
 - `ctrl + u` - deletes the entire text line


## Magic commands

In the `ipython` console you can run the so-called magic commands. These commands are preceded by the `%` character, e.g .:

- `% ls` shows the contents of the current directory
- `% cd` allows you to change the current directory

List and description of available commands: [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html#line-magics) 


# Saving (logging) a session

All work done in ipython can be saved to a text file using one of the magic commands:

 >- %logstart
 >- %history / %hist
 >- %save

Example with `%hist`:

 > `%hist -n -o -f path_to_my_history_file.txt`



