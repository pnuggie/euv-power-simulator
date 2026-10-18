# EUV Power Simulator

A simple Python-based EUV lithography power-loss simulator modelling optical power reduction across successive mirrors, with Matplotlib visualisation.

## Why did you make this?

Honest answer: I was procrastinating on my homework. Why must I be forced to sit and read, write notes and do homework? I mean, I obviously will. I'm a responsible student. Don't worry.

I also really like EUV lithography. I've created an unfinished personal wiki on Google Docs so I can irritate people with niche EUV knowledge whenever the opportunity arises. It's one of my fixations, alongside DDLC.

## Why did you import Matplotlib as `poop` instead of `plt`?

It works. `plt` is the conventional alias, and I'd probably use it in a more formal project. This is not a formal project.

## What can it do?

- Accept three inputs: starting EUV power, mirror reflectivity, and number of mirrors.
- Validate inputs and reject invalid values.
- Calculate the remaining power after each successive mirror.
- Display the power reduction as a graph using Matplotlib.

Yay!

## Installation and usage

### Requirements

- Python 3
- Matplotlib

### Installation

Make sure Python 3 is installed on your computer. Then open Command Prompt and run:

```bash
python -m pip install matplotlib
```

If `python` doesn't work, try `py` instead.

### Running the program

1. Download this repository using **Code -> Download ZIP**, then extract the ZIP file.
2. Open the folder containing `euvthingamajig.py` in File Explorer. Click the address bar at the top, type `cmd`, and press Enter. This opens Command Prompt in that folder.
3. Run the program:

   ```bash
   python euvthingamajig.py
   ```

   If `python` doesn't work, try `py euvthingamajig.py` instead.

4. Follow the prompts to enter the starting EUV power, mirror reflectivity and number of mirrors.

The program will calculate the remaining power and display a graph using Matplotlib. Isn't that so cool??

These instructions are for Windows. Apologies to everyone else.

## What can't it do?

All mirrors currently share the same reflectivity. For example, if you enter 70%, every mirror is treated as having 70% reflectivity. Real EUV optical systems are more complicated, so this is a simplified model rather than an accurate simulation of a complete lithography system.

## The file name is inappropriate.

Ugh, *sorry*.

## What's coming in the future?

Hopefully:

- Interactive sliders
- Different reflectivities for individual mirrors
- More calculation options
- A better-looking graph
- Pretty colours
- A Tkinter interface instead of a command-line interface
- ~~A job~~
