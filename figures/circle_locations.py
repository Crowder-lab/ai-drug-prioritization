#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "cmocean",
#     "matplotlib",
#     "numpy",
# ]
# ///
import math

import cmocean
import numpy as np


def clamp_to_zero(num: float, epsilon: float = 1e-6) -> float:
    return 0 if abs(num) < epsilon else num


def circle_locations(num_points: int, scale: float) -> list[tuple[float, float]]:
    """
    Produce a list of tuples that specify the coordinates of equally spaced points in a circle.
    The first point will always be located on the positive y-axis.
    Points will be produced clockwise.
    Scale scales the points locations by that amount.
    """

    angles = [(2 * math.pi * (i + 1) / num_points) + math.pi / 2 for i in range(num_points)]
    angles.reverse()
    points = [(scale * clamp_to_zero(math.cos(angle)), scale * clamp_to_zero(math.sin(angle))) for angle in angles]
    return points


if __name__ == "__main__":
    SCALE = 6
    NAMES = (
        r"\textit{MAPK8IP3}/JIP3 modulators",
        r"Increase neurotransmitter signaling",
        r"Reduce oxidative stress",
        r"Anti-inflammatory",
        r"Neuro\-protectives",
        r"Increase neuro\-plasticity",
        r"Kinase inhibitors",
        r"Immuno\-modulators",
        r"Anti\-microbials",
        r"Symptomatic relief",
    )
    NUM_POINTS = len(NAMES)
    LINEAR_POINTS = np.linspace(0.1, 0.85, num=NUM_POINTS)
    CMAP = cmocean.cm.ice
    RGB_VALS = CMAP(LINEAR_POINTS, bytes=True)

    locations = circle_locations(NUM_POINTS, SCALE)
    print(r"""\documentclass{article}
\usepackage{fontspec}
\usepackage{geometry}
\usepackage{tikz}

\geometry{margin=0.25in}
\setmainfont{Arial}

\begin{document}
\begin{center}
\begin{tikzpicture}
    [circ/.style={circle, draw=black, text=white, minimum size=85pt, text width=65pt, align=center}]
    \node at (0, 0.4) {\includegraphics[height=160pt]{biorender.png}};
    \begin{scope}[line width=3pt]""")
    for name, location, rgb_val in zip(NAMES, locations, RGB_VALS):
        print(
            fr"        \node [circ, fill={{rgb,255:red,{rgb_val[0]}; green,{rgb_val[1]}; blue,{rgb_val[2]}}}] at {location} {{\textbf{{{name}}}}};"
        )
    print(r"""    \end{scope}
\end{tikzpicture}
\end{center}
\end{document}""")
