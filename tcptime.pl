#!/usr/bin/env perl
use strict;
use warnings;
use Time::HiRes qw/usleep ualarm gettimeofday tv_interval/;
use IO::Socket;
use vars qw/$t0 $t1 $t0_t1/;

my $server = 'www.tommyt.co.uk';
my $port = 80;

sub get_time($$;$) {
    my $server = shift;
    my $port = shift;
    my $TIMEOUT = shift || $TIMEOUT = 5;
    $t0 = [gettimeofday];
    eval {
        local $SIG{ALRM} = sub { die "Timed out\n" };
        alarm $TIMEOUT;
        my $socket = new IO::Socket::INET(
            PeerAddr => $server,
            PeerPort => $port,
            Proto    => 'tcp',
            timeout  => $TIMEOUT);
        alarm 0;
    close $socket;
    };
    $t1 = [gettimeofday];
    $t0_t1 = tv_interval $t0, $t1;
    return $t0_t1;
}

while (1) {
    printf ("%0d %0.06f\n", time, get_time($server, $port, 5));
    sleep 1;
};
