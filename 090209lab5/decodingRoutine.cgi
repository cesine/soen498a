#! /usr/bin/perl
print "Content-type: text/html\n\n";

if ($ENV{"REQUEST_METHOD"} eq "POST") {
  read(STDIN, $datastring, $ENV{"CONTENT_LENGTH"});		
}
elsif (exists $ENV{"REQUEST_METHOD"}) {		# data from GET transaction (or HEAD or other)
  $datastring = $ENV{"QUERY_STRING"};
}
else {
  print "Offline execution detected\n";
  print "Please enter some data.\n";
  $datastring = <>;
  chomp $datastring;
  print "== data accepted == HTML output follows ==\n\n";
}

###decode######################################################
$datastring =~s/%0D%0A/\n/g;                    			#step to deal with line 
																											#breaks in text areas
																											
@nameValuePairs = split(/&/, $datastring);						#step 1
foreach $pair (@nameValuePairs) {
  ($name, $value) = split(/=/, $pair);								#step 2
  
  $name =~tr/+/ /;                                 		#step 3
  $name =~s/%([\da-fA-F]{2})/pack("C",hex($1))/eg; 		#step 3
  $value =~tr/+/ /;                                		#step 3
  $value =~s/%([\da-fA-F]{2})/pack("C",hex($1))/eg;		#step 3
  
  if(exists $formHash{$name}) {												#improved step 4,
    $formHash{$name} = $formHash{$name}.";".$value;		#handles multiple
  }																										#select menus
  else {
    $formHash{$name} = $value;
  }   	
}
###done decoding###############################################


## Note that this file contains the final version of the decoding routine, which
## has the extra features to remove the extra line breaks from submitted text areas
## and which deals with multiple name=value pairs which share the same name.
