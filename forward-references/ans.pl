#!/usr/bin/perl
#
# Forward reference
# creates a back reference to a regex that would appear later.
# only useful inside a repeated group
# 
$Regex_Pattern = '^(\2tic|(tac))+$';
$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}
