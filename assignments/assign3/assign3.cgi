#!/usr/bin/perl 

#to debug cgi-bin/cgiwrapd

print "Content-type:text/html\n\n";

&printHeader();

&printTopLeft();

print "<td>Welcome to my Black Jack game!";

&parseURL();
if (!$user){
	&printLogin();
}else{
	&userValidate();
}

print "</td></tr>";

print "<tr><td>";

if ($found){
	@deck1= &createDeck();
	#print @deck1;
	#shuffle
		

        if ($user eq "supervisor"){
                print "Here is the deck: </p>";
		print @deck1;
        }

	print "<p>Here are your cards: </p>";
	$card1= pop(@deck1);
	$card2=pop(@deck1);
	print "<p>$card1 </p>";
	print "<p>$card2</p>";

}

print "</td></tr></table>";

#################################################
sub createDeck{
my @holderDeck = ("Ace Diamonds", "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds", "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds", "Queen Diamonds", "King Diamonds", "Ace Hearts", "2 Hearts", "3 Hearts", "4 Hearts", "5 Hearts", "6 Hearts", "7 Hearts", "8 Hearts", "9 Hearts", "10 Hearts", "Jack Hearts", "Queen Hearts", "King Hearts", "Ace Clubs", "2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs", "7 Clubs", "8 Clubs", "9 Clubs", "10 Clubs", "Jack Clubs", "Queen Clubs", "King Clubs", "Ace Spades", "2 Spades", "3 Spades", "4 Spades", "5 Spades", "6 Spades", "7 Spades", "8 Spades", "9 Spades", "10 Spades", "Jack Spades", "Queen Spades", "King Spades");
return @holderDeck;
}#end createDeck


sub deal{

}#end deal




sub parseURL{
	print "Inside the parse url\n";
	($user, $pass) = split (/&/, $ENV{"QUERY_STRING"} , 2);
	($junk, $user) = split(/=/, $user, 2);
	($junk, $pass) = split(/=/, $pass , 2); 

	print "This is the username entered $user <br />\n";

	print "This is the password entered $pass <br />\n";

}#end parseURL

sub printLogin{
	print "Inside the print Login\n";
	print <<LOGIN;
<form action="assign3.cgi" method="get" name="loginform">
<table border="1">
<tr><td align="left">Username: </td><td align="right">
<input type"text" name="user" value="" size="30" /></td>

<tr><td> Password:</td><td>
<input type="password" name="pass"  value="" size="30" /></td></tr>

</table>
<input type="submit" value="Submit" /> 
<input type="reset"  value="Reset The Form" /><br />
</form>
<script language="JavaScript">
<!--

//put the curser at user when the page loads
document.loginform.user.focus();

document.loginform.onsubmit=validate;
	function validate() {
		var password=document.loginform.pass.value;
		//alert("Validating form");

		if ( (password.length<7 ) ) {
			alert("Password is too short, please try again.");
			document.loginform.pass.focus();
			document.loginform.pass.select();
			return false;
		}
		
		//http://www.javascriptkit.com/javatutors/redev3.shtml	
		var securepass = password.search(/[^a-zA-Z]/);
		//alert(securepass);
		if ( (securepass == -1) || (countchar(password," ")>0) ) {
			alert("Password must contain no spaces and one non alphabetical character, please try again.");
			document.loginform.pass.focus();
                        document.loginform.pass.select();
                        return false;

		}
		return true;
	}
	
	function countchar(thestring,thechar){
		var count=0;
		for (var x=0 ; x<thestring.length; x++) {
			if(thestring.charAt(x)==thechar){
				count++;
			}
		}		
		return count;

	}
//-->
</script>

New user? <a href="register.html">Register</a></p>
<p>&nbsp</p>
LOGIN

}#end printLogin


sub userValidate{
#print "In the user validate";
$filename="passwd.txt";
open (IN, $filename) or &errorPage("The server was unable to open a data file. Please try again.");

#print "This is to validate the info<br />\n ";

#print "This is the username entered $user <br />\n";

#print "This is the password entered $pass <br />\n";

$found = 0;
while($line = <IN>){
	#print $line;
	@info = split(/\W/,$line);
	#print "Here is the user @info[0]";
	if ($user eq @info[0]){
		$found = 1;
		if ($pass eq @info[1]) {
			print "Welcome $user!";
		}else{ 
			print "User valid, but password does not match.";
		}#end if for valid user
		last;
	}#end if for valid user
	
}#end while for input file loop
if ($found != 1){
	print "User not found.";
	&printLogin();
}
close(IN);
}#end user validate


sub printHeader {
print <<HEADER;
	    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>
Web Applications Winter 2009 - Blackjack
</title>
</head>

<body>
HEADER
}

sub printTopLeft{
print <<TOPLEFT;
<table width="100%" border="1">
<tr height="50%" valign="top">
<td>
<img src="http://www.cse.concordia.ca/images/common/departmentlogo.gif" alt="Logo of Engineering and Computer Science Department of Concordia">
</td>
TOPLEFT

}

