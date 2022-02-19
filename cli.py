#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application cli view
"""

__author__ = 'Mohamed Ouertani'

from view_obj import View
import cmd2


class CLI(cmd2.Cmd,View):

    def __init__(self,controller):
        cmd2.Cmd.__init__(self)
        View.__init__(self,controller)
        self.entries_values = {entry:"" for entry in self.entries}
        

    def get_value(self, key):
        return self.entries_values[key]

    def do_insert(self,args):
        """Get person informations to be inserted"""
        self.entries_values = {entry:"" for entry in self.entries}
        for entry in self.entries:
            self.entries_values[entry] = str(input(f"Saisir {entry} : "))
        print(self.entries_values)
        self.controller.command_handle("Inserer")
    
    def insert_result(self,insertion_message):
        """Print insertion result"""
        print(insertion_message)
    

    def do_delete(self,args):
        """Get person informations to be deleted"""
        self.entries_values = {entry:"" for entry in self.entries}
        self.entries_values["Nom"] = str(input(f"Saisir Nom : "))
        self.controller.command_handle("Effacer")
    
    def delete_result(self,deleted_elements):
        """Print deletion results"""
        self.poutput(cmd2.style(deleted_elements, fg=cmd2.Fg.RED))

    
    def do_search(self,args):
        """Get person informations to be searched"""
        self.entries_values["Nom"] = str(input("Saisir Nom : "))
        self.controller.command_handle("Chercher")

    def search_result(self, found_persons_list):
        """Print search results"""
        if not found_persons_list:
            result = "No persons were found"
            self.poutput(cmd2.style(result, fg=cmd2.Fg.RED))
        else:
            result = "the following persons were found : "
            self.poutput(cmd2.style(result, fg=cmd2.Fg.GREEN))
            for person in found_persons_list:
                self.poutput(cmd2.style(person, fg=cmd2.Fg.BLUE))

    def main(self):
        self.cmdloop()

if __name__ == "__main__":
    test = CLI()
    test.main()
