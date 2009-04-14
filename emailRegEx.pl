if($email =~ /^\w+@\w+\.[a-zA-Z]{2,3}$/) {	# note the ‘\’ before the ‘.’
						# to denote that it is not
						# an excape sequence
	print “This email begins with at least one letter (or underscore)”;
	print “ followed by an ‘@’, at least one letter (or underscore),”;
	print “ a period, and between 2 to three letters.\n”;
}
