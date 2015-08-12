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


`# equilibria [listener_address:]listener_port>>>target_address:target_port,target_address:target_port,...`

This will open a TCP socket listening on `listener_address` at
`listener_port`, and each incoming connection will choose one of the
subsequent `target_address:target_port` combinations to forward to.
The default address to bind the listening socket is `0.0.0.0` for IPv4
or `[::0]` for IPv6.  Numeric IPv6 addresses must be enclosed in
square brackets (e.g., `[2060:3ac1:60::88b2]:443`).

The listening socket is entirely separate from the target socket, so
specifying different families for each is fully supported.  For
example, an IPv6 listening socket can proxy to an IPv4, IPv6, or even
UNIX socket, and vice versa.


## TODO

* Add new capabilities to the control socket for doing runtime
  manipulation of listeners and targets.
* Unify the control socket handling in multi-fork mode so the user
  only needs to interact with the primary daemon instead of having
  each daemon have its own independent control socket.
* Packet socket support (i.e., AF_PACKET) to enable raw socket
  proxying.
* Add loadable module support for pluggable target selection rather
  than hard-coding the current choose-at-random algorithm.
* Add support for Docker integration so that target identities can be
  automatically ascertained via Docker REST queries instead of
  hard-coded addresses or DNS lookups.  Should also be dynamically
  updated.
* Add support for SSL sockets for secure tunneling of otherwise
  insecure/vulnerable protocols.  Potential alternative to stunnel,
  SSH tunneling, etc.



[![Join the chat at https://gitter.im/mej/equilibria](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mej/equilibria?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
