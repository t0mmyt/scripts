#!/bin/sh
# Clean expired or revoked gpg keys from keyring
# Tom Taylor <tom@tommyt.co.uk>
# Released under WTFPL <http://www.wtfpl.net/>

gpg --list-keys | awk '
/(expired|revoked)/{ 
    keys[i] = substr($2, length($2) - 7);
    i++;
} 

END{ 
    for (k in keys) {
        list = list keys[k] " "
    };
    print "gpg --delete-key "list
}'
