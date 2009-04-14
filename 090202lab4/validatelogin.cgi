#!/usr/bin/perl 
#alarm=60;
#
print "Content-type: text/html\n\n";

#print "This is to validate the info<br />\n ";

print "The ENV contents\n";
my $key;
foreach $key( keys %ENV){
	print "$key => $ENV{$key}\n";
}#end foreach 

($user, $pass) = split (/&/, $ENV{"QUERY_STRING"} , 2);
($junk, $user) = split(/=/, $user, 2);
($junk, $pass) = split(/=/, $pass , 2); 

#print "This is the username entered $user <br />\n";

#print "This is the password entered $pass <br />\n";
$filename="passwd.txt";
open("IN","<".$filename);

$found = 0;
while($line = <IN>){
	#print $line;
	@info = split(/\W/,$line);
	#print "Here is the user @info[0]";
	if ($user eq @info[0]){
		$found = 1;
		if ($pass eq @info[1]) {
			print "Login successful";
		}else{ 
			print "User valid, but password does not match.";
		}#end if for valid user
		last;
	}#end if for valid user
	
}#end while for input file loop

if ($found != 1){
	print "User not found.";
}
