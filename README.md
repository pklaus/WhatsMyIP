### WhatsMyIP

This tool is a very simple HTTP Server:
It returns the `REMOTE_ADDR` to connecting HTTP clients.
In other words: *It tells you what your current IP is*.

#### Installation

All this server needs is Python 3.3+ (there's a branch with support for Python 2.7+ too).
So, get Python first, then download the project from <https://github.com/pklaus/WhatsMyIP>
or clone the repository.

#### Usage

Start the tool like this:

    ./whatsmyip.py --host :: --port 8080

It should be run a a computer or server that's reachable over the Internet.
Then any client requesting http://serveraddress:8080/ will receive its
IP address (IPv4 or IPv6) back from the server.

#### Inspired by

* <http://wiki.python.org/moin/BaseHttpServer>
* and <http://www.righto.com/2011/02/ipv6-web-serving-with-arc-or-python.html>

#### Author

* Philipp Klaus  
  <philipp.l.klaus@web.de>.
