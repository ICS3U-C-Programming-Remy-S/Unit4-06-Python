#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 19, 2023
# This program will display all valid RGB
# colors with nested loops


def main():
    # display message about program
    print("This program will display all valid RB colors.")
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                # Print the colored text
                print(
                    "\033[38;2;{};{};{}mRGB({}, {}, {}) \033[38;2;255;255;255m".format(
                        red, green, blue, red, green, blue
                    )
                )


if __name__ == "__main__":
    main()
