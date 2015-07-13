# Equilibria

Equilibria is a simple IP load-balancing forwarding/proxy socket
server.  The user creates one or more listener/target-set pairs;
Equilibria listens for traffic at the specified listener and forwards
the traffic to one of the specified targets (selected at random) in
the target set.  Any traffic received back from the target is
forwarded to the client machine over the original socket.  This
back-and-forth forwarding of traffic continues until the client closes
the connection or the target fails (at which point another target is
chosen at random for the client).

Equilibria is under active development (after being resurrected after
a many-year hiatus) and needs some work to flesh it out to be usable
for what I now need it to do; additional documentation will be added
once this first round of improvements are in place.

## Quick Start

Syntax:

`# equilibria listener_port:target_address:target_port,target_address:target_port,...`

This will open a TCP socket listening on `listener_port`, and each
incoming connection will choose one of the subsequent
`target_address:target_port` combinations to forward to.


[![Join the chat at https://gitter.im/mej/equilibria](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mej/equilibria?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
