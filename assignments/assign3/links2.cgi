#!/usr/bin/perl
print "Content-type:text/html\n\n";

$dataDir = "/wrong/path/to/file/";  # so that the &errorPAge function is called 
																		# when the program tries to open the websites.txt file

open (INFILE, "$dataDir"."websites.txt") or &errorPage("The server was unable to open a data file. Please try again.");

%websites=();
while($line = <INFILE>) {
  chomp $line;
  ($name, $url) = split(/=/, $line);
  $websites{$name} = $url;
}
close(INFILE);

print <<TOP;
<html><head><title>A list of websites</title></head><body>
  <h1>Happy Surfing!</h1>
 <ul>
TOP

foreach $name (keys %websites) {
  print "<li><a href=\"http://$websites{$name}\n\">$name</a></li>\n";
}

print<<BOTTOM;
  </ul>
 </body></html>
BOTTOM

##############################################################################
sub errorPage {
 my $message = $_[0];  # optional message parameter
 
 print<<ALL;
 <html><head><title>Server Error</title></head><body>
  <h2>Server Error Encountered</h2>
  $message 
  If the problem persists, please notify the <a href="mailto:admin\@uweb.edu">webmaster</a>.
 </body></html>
ALL
 
exit;   # terminate program since failure to open data file
}

