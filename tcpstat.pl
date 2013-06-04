#!/usr/bin/env perl
################################################################################
# Quickly count TCP states (significantly faster than netstat)
# Linux only!
#
#
# Tom Taylor 26/06/2012
################################################################################
use strict;
use vars qw/%TCP_STATE %count/;

%TCP_STATE = (
    '01' => 'ESTABLISHED',
    '02' => 'SYN_SENT',
    '03' => 'SYN_RECV',
    '04' => 'FIN_WAIT1',
    '05' => 'FIN_WAIT2',
    '06' => 'TIME_WAIT',
    '07' => 'CLOSE',
    '08' => 'CLOSE_WAIT',
    '09' => 'LAST_ACK',
    '0A' => 'LISTEN',
    '0B' => 'CLOSING',
);

sub count_state($) {
    my $fn = shift;
    open FH, "<$fn" or die "Couldn't open $fn, $!\n";
    <FH>;
    while (<FH>) {
	#print substr $_, 3;
	$count{$TCP_STATE{(split ' ', $_)[4]}}++;
    }
    close FH;
}

count_state('/proc/net/tcp');
count_state('/proc/net/tcp6') if -f '/proc/net/tcp6';

printf ("%-20s%d\n", $_, $count{$_}) for (sort keys %count);
