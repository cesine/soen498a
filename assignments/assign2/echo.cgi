#!/usr/bin/perl 

#this line is needed for all cgi scripts or else it wont work
print "Content-type: text/html\n\n";

print "This page is to validate the info<br />\n ";

#this splits the url into 3 variables on the &
($user, $pass, $pass2) = split (/&/, $ENV{"QUERY_STRING"} , 3);
#this splits the user into two variables on the =
($junk, $user) = split(/=/, $user, 2);
($junk, $pass) = split(/=/, $pass , 2); 

($junk, $pass2) = split(/=/, $pass2 , 2);

print "This is the username entered $user <br />\n";

print "This is the password entered $pass <br />\n";

print "This is the second password entered $pass2 <br />\n";


