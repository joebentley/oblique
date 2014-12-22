#!/usr/local/bin/python
import random, sys

f = open('strategies', 'r')
strategies = f.readlines()
sys.stdout.write(random.choice(strategies))

