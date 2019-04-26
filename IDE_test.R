# This is my test file for building R IDE on Atom
# It will show how the code run on Atom with packages
# to set the spelling, you need open the command window (cmd-shift-p) and
# run: Editor: Log Cursor Scope
# and then paste it into the spell-check grammar source part

library(tidyverse)
library(igraph)

data(mtcars)

head(mtcars)
names(mtcars)
hist(mtcars$mpg)
