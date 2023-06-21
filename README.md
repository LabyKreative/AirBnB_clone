# AirBnB clone - The console (team project)

![Logo](https://cdn.freebiesupply.com/logos/large/2x/airbnb-2-logo-png-transparent.png)

## Project description

- AirBnB clone - The console project represents a simple version of AirBnB web
  app. It performs mini features of AirBnB app as interpreted in the command line. The basic idea of the project is to learn the fundamental concepts
  of HLP(Higher Level Programming) using python then later introduce Flask: ![alt text](https://i.morioh.com/200817/4e495d78.webp)
  <https://flask.palletsprojects.com/en/2.3.x>

## Command interpreter description

### How to start the console

- First of all, you'll have to own this repository by:

```bash
  git clone https://github.com/LabyKreative/AirBnB_clone.git
```

- Navigate to the AirBnB directory:

```bash
cd AirBnB_clone
```

### How to use the console

- The console has two mode you can run it as:

a. **Interactive Mode:** which you can run with

```bash
./console
(hbnb) help

Documented commands (type <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

b. **Non-Interactive Mode:** which you can run with

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Examples

- The codes were tested using **unittest** module and **flake8** for pycodestyle
- The tests cases are in test directories in different level in the project
- And the `console.py` works perfectly as expected

### Example 0: Create an object

```bash
(hbnb) create BaseModel
```

```bash
(hbnb) create BaseModel
1234567890
(hbnb)
```

#### Example 1: Show an object

```bash
(hbnb) show 1234567890
[BaseModel] (1234567890) {'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

#### Example 2: Destroy an object

```bash
(hbnb) destroy BaseModel 1234567890
(hbnb) show BaseModel 1234567890
** no instance found **
(hbnb)
```

#### Example 3: Update an object

```bash
(hbnb) update BaseModel 1234567890 first_name "person"
(hbnb) show BaseModel 1234567890
[BaseModel] (1234567890) {'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

#### Example 0: Show all User objects

```bash
(hbnb) User.all()
["[User] (1234567890) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (1234567890) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 1: Destroy a User

```bash
(hbnb) User.destroy("1234567890")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (1234567890) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 2: Update User (by attribute)

```bash
(hbnb) User.update("1234567890", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (1234567890) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '1234567890', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 3: Update User (by dictionary)

```bash
(hbnb) User.update("1234567890", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (1234567890) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '1234567890', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

### Authors

- **Credoecspa** [GitHub](https://github.com/Credoecspa) ~ [Email](ezejioforchiemerie708@gmail.com)
- **LabyKreative** [GitHub](https://github.com/LabyKreative) ~ [Email](labykreative@yahoo.com)
