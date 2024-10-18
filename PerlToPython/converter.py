# converter.py

class PerlToPythonConverter:
    def __init__(self):
        pass

    def convert_print_statement(self, line):
        """Convert Perl print to Python print."""
        if 'print' in line:
            line = line.replace('print ', 'print(').replace(';', ')')
            line = line.replace("\\n", "")
            return line
        return line

    def convert_variable_declaration(self, line):
        """Convert Perl variable declarations to Python variables."""
        if 'my $' in line:
            line = line.replace('my $', '').replace(';', '')
            return line
        return line

    def convert_foreach_loop(self, line):
        """Convert Perl foreach loop to Python for loop."""
        if 'foreach' in line:
            line = line.replace('foreach my $', 'for ').replace('(@', 'in ').replace(')', ':')
            return line
        return line

    def convert_array_declaration(self, line):
        """Convert Perl arrays to Python lists."""
        if 'my @' in line:
            line = line.replace('my @', '').replace('(', '[').replace(')', ']').replace(';', '')
            return line
        return line

    def convert_code(self, perl_code):
        """Convert Perl code to Python."""
        python_code = []
        for line in perl_code.splitlines():
            # Apply conversion functions to each line
            line = self.convert_print_statement(line)
            line = self.convert_variable_declaration(line)
            line = self.convert_array_declaration(line)
            line = self.convert_foreach_loop(line)
            python_code.append(line)
        return '\n'.join(python_code)
