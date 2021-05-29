from textstrings import TextStrings
from termcolors import  bcolors
import math

class ObjectStats:
    
    def __init__(self, actor_name="", actor_name_len = 1, actor_name_color = bcolors.OKGREEN, current_value=100, value_max=100, bar_size=20, stat_name="ST", newline:bool=True, tick_char="█", bar_color=bcolors.OKGREEN):
        self.actor_name = actor_name
        self.actor_name_len = actor_name_len
        self.actor_name_colour = actor_name_color
        self.current_value = current_value
        self.value_max = value_max
        self.bar_size = bar_size
        self.stat_name = stat_name
        self.newline = newline
        self.tick_char = tick_char
        self.bar_ticks_size = (value_max) / (bar_size)
        self.bar_color = bar_color
        self.bar = ""

    def print_stats(self):
        
        bar_ticks = 0
        
        while bar_ticks < self.current_value:
            if math.floor(bar_ticks + self.bar_ticks_size) <= self.current_value:
                self.bar += self.tick_char
            bar_ticks += self.bar_ticks_size

        print( F"{(self.actor_name_colour)}{(self.actor_name).ljust(self.actor_name_len)}{bcolors.ENDC}   {str(self.current_value).ljust(4)}/{str(self.value_max).ljust(4)} {bcolors.ENDC}|{self.bar_color}{self.bar.ljust(self.bar_size)}{bcolors.ENDC}|{self.stat_name}", end='')
        if self.newline == True:
            print("")