#!/encs/bin/perl
$| = 1;
print "Content-type: text/html\n\n";
print "<html><title>Date/Time Functions Demo</title><body>\n";
print "<h1>Date/Time Functions Demo</h1>\n";
print "<p>The current time and date is <em>\n";
system("/bin/date");
print "</em>\n</body></html>\n";
