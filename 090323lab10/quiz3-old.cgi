#!/encs/bin/perl
#use strict;

print "Content-type: text/html\n\n";

##### global variables #####
use DBI;
my $dbhandle = DBI -> connect("DBI:CSV:f_dir=/www/home/v/v_cook/teaching/soen498a/090323lab10/quizdb") #directory of database must be 777
	or print "Can't connect to database". DBI->errstr();
my $file_life_span = 1.0/24; # 1/24 = 1 hour
my $time_out = 1.0/24;
my $cache_limit = 300;
my $state_table_name = "states";
my $quiz_table_name = "quizdb";	
my %stateHash=();
my %formHash=();
### end global variables

### ap logic ##############
print "opening the database.";

$dbhandle->{'quiz3'}->{'quizdb'} = { 'file' => 'quizdb'};
my $sth= $dbhandle->prepare("SELECT * FROM quiz");




if ($formHash{"request"} eq "begin_quiz"){
	&begin_quiz;
}elsif($formHash{"request"} eq "grade_question"){
	&grade_question;
}else{
	&welcome_page;
}

#####subroutines ######
sub begin_quiz(){
	print "begin quiz\n";
}

sub grade_question(){
	print "grade question\n";
}

sub welcome_page(){
	print "welcome :)";
}

sub error_page(){
	print "There was an error.@_";
}
