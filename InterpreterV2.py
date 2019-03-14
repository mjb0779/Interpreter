import Method_Grabber
import Attrib_Grabber
import constant
import class_maker
import os.path
from array import *


class Interpreter(object):
    file = ''
    file_contents = []
    my_classes = []
    str = ''
    fin = ''

    def __init__(self, file):
        self.file = file
        self.dict = {}

        if self.file_extension_check():
            #print()
            self.read_file()
            self.data_parser()
            print(self.dict)
            # for x in self.dict:
            #     print(self.dict[x])




    def file_extension_check(self):
        (self.file_holder, self.file_extension) = os.path.splitext(self.file)

        if self.file_extension != '.txt':
            return False
        else:
            return True

    def read_file(self):
        try:
            with open(self.file, "r") as file:
                contents = file.readlines()
                for line in contents[1:]:
                    if line == '@startuml\n' or line == '@enduml':
                        continue  # Takes out the header and footer parts of the txt file
                    if line == '\n':
                        continue  # Takes out the extra lines
                    else:
                        self.file_contents.append(line)  # only adds the vital information to the actual content array

                return self.file_contents
                #     if line == '\n':
                #         continue #Takes out the extra lines
                #     else:
                #         self.file_contents.append(line) # only adds the vital information to the actual content array
                #
                # return self.file_contents



        except FileNotFoundError:
            print("File does not exist")

    def data_parser(self):
        count = 0
        class_count = 0
        temp_str = ''
        temp_fin = ''
        for line in self.file_contents:

            if 'class' in line and '{\n':
                temp = line.split(' ')
                self.my_classes.append(temp[1])
                #print(self.my_classes)
                class_count += 1
                count = 1
                continue
            elif '}\t\n' in line or '}\n' in line:
                count = 0

            # else:


            if count == 1:
                temp_str += ''.join(line)
            else:
                self.fin = temp_str
                self.dict[self.my_classes[class_count-1]] = self.fin

                temp_str = ''

            #self.my_classes
        return self.dict

