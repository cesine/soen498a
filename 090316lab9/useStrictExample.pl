#!/usr/bin/perl
#This script demonstrates how use strict can catch typo bugs. There is a mistake in one of the variable names,  fix the typo adn then the code will compile


use strict;

#all variables need to be declared using my at their first use
my @allFiles = glob("*"); # a list of all files
for(my $i=0; $i<@allFiles; $i++) {
	print $allfiles[$i]."\n";
}
print "\n";

