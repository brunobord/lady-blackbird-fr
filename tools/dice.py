#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
import cmd
import sys


class Command(cmd.Cmd):
    prompt = 'What do you do? '

    def do_d(self, args):
        "Roll dice. Usage: 'd <nb>'"
        nb = int(args)
        rolls = [random.randint(1, 6) for x in xrange(nb)]
        successes = sum(1 for roll in rolls if roll >= 4)
        print "Rolls:", rolls
        print "Success: %d" % successes

    def do_quit(self, args):
        "Simply exits"
        print
        print "Bye"
        sys.exit()
    do_EOF = do_quit
    do_exit = do_quit


if __name__ == '__main__':
    cmd = Command()
    try:
        cmd.cmdloop('Please...')
    except KeyboardInterrupt, e:
        sys.exit('\nbye')
