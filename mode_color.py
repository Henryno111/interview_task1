#!/usr/bin/python3

import statistics

colors = {"Monday": ["green", "yellow", "green", "brown", "blue", "pink",
                     "blue", "yellow", "orange", "cream", "orange", "red", "white", "blue",
                     "white", "blue", "blue", "blue", "green"],
          "Tuesday": ["ash", "brown", "green", "brown", "blue", "blue", "blue",
                      "pink", "pink", "orange", "orange", "red", "white", "blue", "white",
                      "white", "blue", "blue", "blue"]
          "Wednesday": ["green", "yellow", "green", "brown", "blue", "pink", "red", "yellow",
                        "orange", "red", "orange", "red", "blue", "blue", "white", "blue",
                        "blue", "white", "white"]
          "Thursday": ["blue", "blue", "green", "white", "blue", "brown", "pink", "yellow",
                       "orange", "cream", "orange", "red", "white", "blue", "white", "blue",
                       "blue", "blue", "green"]
          "Friday": ["green", "white", "green", "brown", "blue", "blue", "black", "white",
                     "orange", "red", "red", "red", "white", "blue", "white", "blue",
                     "blue", "blue", "white"]

all_colors = [color for colors_list in colors.values() for color in colors_list]

          color_counts = Counter(all_colors)
          most_mode_color = color_counts.most_common(1)[0][0]

          print("The color mostly worn throughout the week is:", most_mode_color)
