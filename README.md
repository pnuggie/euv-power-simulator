# EUV Power Simulator

A simple Python-based EUV lithography power-loss simulator modelling optical power reduction across successive mirrors, with Matplotlib visualisation.

## Why did you make this?

Honest answer: I was procrastinating on my homework. Why must I be forced to sit and read, write notes and do homework? I did eventually finish it. I'm a responsible student, okay!

I also really like EUV lithography. I've created an unfinished personal wiki on Google Docs so I can irritate people with niche EUV knowledge whenever the opportunity arises. It's one of my fixations, alongside DDLC.

## Why did you import Matplotlib as `poop` instead of `plt`?

It works. `plt` is the conventional alias, and I'd probably use it in a more formal project. This is not a formal project.

## What can it do?

- Accept three inputs: starting EUV power, mirror reflectivity, and number of mirrors.
- Validate inputs and reject invalid values.
- Calculate the remaining power after each successive mirror.
- Display the power reduction as a graph using Matplotlib.

Yay!

## The maths behind it

### Simplified calculation

The simulator assumes that every mirror has the same reflectivity, so the output power can be calculated using:

$$
P_{\text{out}} = P_{\text{in}} \times R^n
$$

Where:
- $P_{\text{out}}$ is the final output power.
- $P_{\text{in}}$ is the initial input power.
- $R$ is the reflectivity of each mirror, expressed as a decimal to make calculating it easier.
- $n$ is the number of mirrors.

### A more generalised calculation

In reality, individual mirrors can have different reflectivities (something I'd like to add in the future). This can be represented using the product symbol, $\prod$:

$$
P_{\text{out}} = P_{\text{in}} \prod_{i=1}^{n} R_i
$$

Here, $R_i$ represents the reflectivity of each individual mirror.

The simulator currently uses the simplified calculation, assuming that all mirrors have the same reflectivity. Therefore, don't use this as some 'true perfect EUV power' calculator. Although unlikely, I'd still like to clarify that.

<sub> Formatting that was a massive pain.

## Installation and usage

### Requirements

- Python 3
- Matplotlib

### Installation

Make sure Python 3 is installed. Open Command Prompt and install Matplotlib:

```bash
python -m pip install matplotlib
```

If `python` doesn't work, try `py` instead.

### Running the program

1. Download the repository using **Code -> Download ZIP**, then extract it.
2. Open the extracted folder in File Explorer. Click the address bar, type `cmd`, and press Enter to open Command Prompt in that folder.
3. Run:

   ```bash
   python euvthingamajig.py
   ```

   If needed, use `py euvthingamajig.py` instead.
4. Enter the starting EUV power, mirror reflectivity and number of mirrors when prompted.

The program calculates the remaining optical power and displays a graph using Matplotlib. Isn't that so cool??

*These instructions are for Windows. Apologies to everyone else.*

## What can't it do?

All mirrors currently share the same reflectivity. For example, if you enter 70%, every mirror is treated as having 70% reflectivity. Real EUV optical systems are more complicated, so this is a simplified model rather than an accurate simulation of a complete lithography system.

In real EUV machines, mirrors use multilayer coatings made from alternating molybdenum and silicon layers. Their design can vary depending on the mirror's position and optical requirements, which affects how much light each mirror reflects.

If every mirror in a real machine behaved exactly like the mirrors in this simple program, that would be suspicious, even if very satisfying. Please take it up with the engineers. I am not strong enough for that level of mathematics, yet.

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
