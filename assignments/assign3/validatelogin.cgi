#!/usr/bin/perl

#to debug cgi-bin/cgiwrapd

print "Content-type:text/html\n\n";

print <<TOP;
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>
Web Applications Winter 2009 - Blackjack
</title>
</head>

<body>
TOP

#################### Top Left #########################
print <<TOPLEFT;
<table width="100%" border="1">
<tr height="50%" valign="top">
<td>
<img src="http://www.cse.concordia.ca/images/common/departmentlogo.gif" alt="Logo of Engineering and Computer Science Department of Concordia">
</td>
TOPLEFT
#################### Top Right #########################
print <<TOPRIGHTOPEN;
<td>
<p>Welcome to my Blackjack game!<br />
TOPRIGHTOPEN
$cookie=0;
if ( !($cookie) ) {
	&displayLogin();
}
print <<TOPRIGHTCLOSE;
</td></tr>
TOPRIGHTCLOSE

#################### Bottom Left #########################

#################### Bottom Right #########################



print<<BOTTOM;

at the bottom
 </body></html>
BOTTOM


#############################################################################
sub displayLogin() {
print <<LOGIN;
<form action="validatelogin.cgi" method="get" name="loginform">
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
		alert("Validating form");

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

$filename="passwd.txt";
open (IN, $filename) or &errorPage("The server was unable to open a data file. Please try again.");

#print "This is to validate the info<br />\n ";

($user, $pass) = split (/&/, $ENV{"QUERY_STRING"} , 2);
($junk, $user) = split(/=/, $user, 2);
($junk, $pass) = split(/=/, $pass , 2); 

print "This is the username entered $user <br />\n";

print "This is the password entered $pass <br />\n";

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
	&userNotFound("User not found.");
}
close(IN);

}#end sub login

##############################################################################
sub errorPage {
 my $message = $_[0];  # optional message parameter
 
 print<<ALL;
 <!--<html><head><title>Server Error</title></head><body>-->
  <h2>Server Error Encountered</h2>
  $message 
  If the problem persists, please notify the <a href="mailto:admin\@uweb.edu">webmaster</a>.
 <!--</body></html>-->
ALL
 
exit;   # terminate program since failure to open data file
}

sub userNotFound {
 my $message = $_[0];  # optional message parameter

 print<<ALL;
 <!--<html><head><title>User Not Foundr</title></head><body>-->
  <h2>User Not Found</h2>
  $message
  Please login again <a href="assign3.cgi">assign3.cgi</a>.
 <!--</body></html>-->
ALL

exit;   # terminate program since failure to open data file

}
