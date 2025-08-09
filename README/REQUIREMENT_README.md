# Project requirements

## Overview

This project has very few exteneral dependencies making it very easy to run on all systems.
The only one external libary that must be installed and thta is Colorama
All other libaries are a part of the Python Standard Libary and do not require a seperate installation

## System requirements 
```
- Python 3.10+ (3.12 recommended)
- PIP (python package installer)
- Windows, Linux, WSL or MacOS
```

## How to run
After colorama is installed

```
python connect_four.py
```

> If 'Colorama' is not installed the project will inform you and exit imediately


## Dependencies

### Colorama 0.4.6

Install with

```
pip install colorama
```
or 
```bash
pip install -r requirements.txt
```

#### Purpose
Colorama is used to output color into the terminal. And is used to inhance the game's experience

#### Use in project
- Colorama is used in the project to help make each diffrent players peice be clearly different
- It is also used to show the winning line (if any) making it clear to the player(s) where the wining line is

### Risks / considerations
- colorama is a lightweight package and therefore does not have much risk assosiated.
- It is still a dependancy so ensure its kept updated

## Standard Packages
All other imported and used libaries are inbult to python and do not require an install
```
- math
- random
```

Because of this there is very little risk or considerations to keep in mind.