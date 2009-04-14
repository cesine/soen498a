#!/encs/bin/perl
#http://www.perlmeme.org/tutorials/parsing_csv.html

    use strict;
    use warnings;
    #use Text::CSV;
    use DBI::CSV;

    my $file = 'quizdb.csv';

    #my $csv = Text::CSV->new();
    my $csv = DBI::CSV->new();


    open (CSV, "<", $file) or die $!;

    while (<CSV>) {
        if ($csv->parse($_)) {
            my @columns = $csv->fields();
            print "@columns\n";
        } else {
            my $err = $csv->error_input;
            print "Failed to parse line: $err";
        }
    }
    close CSV;

