# main.py

from converter import PerlToPythonConverter

# Sample Perl code
perl_code = """
#!/usr/bin/perl
use strict;
use warnings;

my $name = "Alice";
my $age = 30;

print "Name: $name\\n";
print "Age: $age\\n";

my @numbers = (1, 2, 3, 4, 5);
foreach my $num (@numbers) {
    print "$num\\n";
}
"""

def main():
    # Create an instance of the PerlToPythonConverter
    converter = PerlToPythonConverter()

    # Convert Perl code to Python
    python_code = converter.convert_code(perl_code)

    # Output the converted Python code
    print("Converted Python Code:\n")
    print(python_code)

if __name__ == "__main__":
    main()
