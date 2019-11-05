import sys

UML_STRUCT = '''
{hor_line}
{title}
{hor_line}
{class_name}
{hor_line}
{data_members}
{hor_line}
{methods}
{hor_line}'''

class UML():
    def __init__(self, hor_sep='#', ver_sep='#', class_name='', 
    data_members=[], methods=[]):

        self.hor_sep = hor_sep
        self.ver_sep = ver_sep
        self.title = 'UNIFIED MODELING LANGUAGE'
        self.class_name = class_name
        self.data_members = data_members
        self.methods = methods
        self.output_to_file = False
        self.output_file = None


    def __str__(self):
        return self.renderUML()


    def getUserInput(self) -> None:
        self.commandLineArgs()

        correct = False
        while not correct:        
            self.class_name = input('Class Name : ')
            self.data_members = input('Data Member (provide a list seperated by commas) : ').split(',')
            self.methods = input('Methods (provide a list seperated by commas) : ').split(',')

            print('______________________________')
            print('Class Name: {}'.format(self.class_name))
            print('Dath Members: {}'.format(', '.join(self.data_members)))
            print('methods: {}'.format(', '.join(self.methods)))
            print('______________________________')

            user_input = input('Does this look correct (y/n) ? ')
            if user_input == 'y' or user_input == 'yes':
                correct = True
            else:
                print('Please enter your values again')

        self.handleOutput()


    def renderUML(self) -> str:
        self.tableWidth = len(max([self.title] + [self.class_name] + self.data_members + self.methods, key=len)) + 3
        uml = UML_STRUCT.format(
            hor_line=self.hor_sep * self.tableWidth + self.ver_sep, 
            title=self.formatLine(self.title),
            class_name=self.formatLine(self.class_name),
            data_members=self.formatSection(self.data_members),
            methods=self.formatSection(self.methods))
        return uml


    def formatSection(self, section: list) -> str:
        section_string = ''
        for index, line in enumerate(section):
            end_char = '\n' if index < len(section) - 1 else ''
            section_string += self.formatLine(line) + end_char
        return section_string


    def formatLine(self, line: str) -> str:
        specifier = '<%ss' % (self.tableWidth)
        return format(line.strip(' '), specifier) + self.ver_sep


    def handleOutput(self):
        if self.output_to_file:
            with open(self.output_file, 'w+') as file:
                file.write(self.renderUML())
        else:
            print(self.renderUML())


    def commandLineArgs(self) -> None:
        if len(sys.argv) > 1:
            switches = sys.argv[1]
            if switches[0] == '-':
                if 'h' in switches:
                    self.hor_sep = input('What do you want the horizontal seperator to be? ')
                if 'v' in switches:
                    self.ver_sep = input('What do you want the vertical seperator to be? ')
                if 'o' in switches:
                    try:
                        self.output_to_file = True
                        self.output_file = sys.argv[2]
                    except IndexError:
                        print('\033[1;31;40m No provided file path (must be provieded with the "-o" case is present)' )
                        exit()
            if '--help' in sys.argv:
                print('this is the help info')



if __name__ == '__main__':
    new_uml = UML()
    new_uml.getUserInput()
