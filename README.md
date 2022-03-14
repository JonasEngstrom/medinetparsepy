# Medinet ParsePy

Parses data from the Medinet Scheduling system, developed by [Medical Networks Scandinavia AB](https://www.medinetworks.se), for analysis in Python, aiding scheduling and follow up. This project is in no way connected to the developers of Medinet.

Prefer working in R? No problem! Check out Medinet ParsePy’s sister package [Medinet ParseR](https://github.com/JonasEngstrom/medinetparser).

## Installing the *medinetparsepy* Package

The following steps describe how to install `medinetparsepy` from GitHub.

### 1. In the shell, use *pip* to download the package

```bash
pip install git+https://github.com/JonasEngstrom/medinetparsepy
```

### 2. Start Python

### 3. Import the needed functions

#### Method 1

The package is structured with one function per file, so a suggested way of importing them is as follows.

```python
from medinetparsepy.load_tidy_schedule import load_tidy_schedule
```

The functions can be can then be accessed directly.

```python
tidy_schedule = load_tidy_schedule('schedule.html')
```

#### Method 2

If you choose to import all functions at once (not recommended).

```python
from medinetparsepy import *
```

You must remember to add the module name when calling the function.

```python
tidy_schedule = load_tidy_schedule.load_tidy_schedule('schedule.html')
```

## Get Started Using Medinet ParsePy

Medinet ParsePy currently does not support scraping data directly from Medinet, as this would require handling login credentials. Therefore data must first be downloaded manually, by following the subsequent steps.

1. Go to the [Medinet Website](https://medinet.se).

2. Log in.

3. If you work in several departments, you will be prompted to choose one at this point. If not, skip ahead to the next step.

4. Click *Schema*.

5. Make sure *Schemavy* is set to *Vecka vs användare*.

6. Choose the weeks you are interested in analyzing.

7. Use the web brower’s save command.

8. Save the page in HTML format. This will be your input file to Medinet ParsePy.
