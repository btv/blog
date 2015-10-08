Title: Connecting to a Riak node using Haskell and viewing Riak buckets
Date: 2013-12-17 17:26
Author: Bryce
Tags: Haskell, Riak
Slug: connecting-to-a-riak-node-using-haskell-and-viewing-riak-buckets

Recently at $DAYJOB I've been lucky enough to start playing with
[Riak](http://basho.com/riak/) for a couple of projects that I thought
it would be great for. So far I've been extremely impressed with Riak's
speed, configurability, and overall ease of use, and I look forward to
using it more in the future. For capacity planning reasons, I performed
speed tests using Bash and Curl, Python and Urllib, and even moved on to
using Python and Riak's protocol buffered client. (Also fixed a bug in
the
[documentation](https://github.com/basho/riak-python-client/pull/288),
WINNING!). But one day the question came to me, (this shouldn't be a
surprise to anyone whose been following this blog): "can I connect to
Riak with Haskell?" The answer is "Yes!" you can use the
[Network.Riak](https://github.com/janrain/riak-haskell-client) library.

I went looking through the documentation for some quick examples to
quickly get started, but I couldn't find any. I guess I'm so spoiled by
all the examples within the Python documentation, I just assumed that
would exist. So instead I just decided to make my own. I'll be doing a
mini-series of posts showing how to do various things using Riak and
Haskell. Let's get started.

I'm going to assume that you already have both the Haskell platform and
the riak-haskell-client installed (`cabal install riak`). Also, Riak
should be installed and running (basic configuration is fine) on your
local machine. If you're not connectingto your local machine, there is a
line commented out in the code that will show you how to connect to a
remote node.

Let's copy a command from the Riak documentation so we have something to
test with:

```bash
curl -v -XPOST http://localhost:8098/buckets/test/keys/test_key \
-H 'Content-Type: text/plain' \ 
-d 'this is a test'
```

You should see output similar to:

```text
* About to connect() to 127.0.0.1 port 8098 (#0)
*   Trying 127.0.0.1...
* Adding handle: conn: 0xd1f3e0
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0xd1f3e0) send_pipe: 1, recv_pipe: 0
* Connected to 127.0.0.1 (127.0.0.1) port 8098 (#0)
> POST /buckets/test/keys/test_key HTTP/1.1
> User-Agent: curl/7.33.0 > Host: 127.0.0.1:8098
> Accept: */* > Content-Type: text/plain > Content-Length: 14
>
* upload completely sent off: 14 out of 14 bytes 
< HTTP/1.1 204 No Content
< Vary: Accept-Encoding
* Server MochiWeb/1.1 WebMachine/1.10.5 (jokes are better explained) is not blacklisted
< Server: MochiWeb/1.1 WebMachine/1.10.5 (jokes are better explained)
< Date: Sun, 08 Dec 2013 07:42:19 GMT
< Content-Type: text/plain < Content-Length: 0
< * Connection #0 to host 127.0.0.1 left intact
```

And with just a quick verification we know that there is data now in the
server:

```bash
curl http://127.0.0.1:8098/buckets/test/keys/test_key
this is a test
```

Now onto the Haskell part! Copy and paste the code below into a file,
riak\_get\_buckets.hs:

```haskell
module Main where 
import qualified Network.Riak as R
import qualified Data.ByteString.Lazy as L 

main :: IO ()main = do
    let client = R.defaultClient
    -- If you want to connect to a remote Riak server use this line
    -- let client = R.Client "FQDN_or_IP_address" "8087" (L.empty)
    con <- R.connect client
    buckets <- R.listBuckets con
    print buckets
```

Now run the code:

```bash
$runhaskell riak_get_buckets.hs
fromList ["test"]
```

Viola! You have now gotten a
[Seq](http://www.haskell.org/ghc/docs/latest/html/libraries/containers-0.5.0.0/Data-Sequence.html)
of your buckets. I think the code is pretty easy to explain and should
look familiar to anyone who's connected to a database through a
programming language before. In the first line you create a connection
to the server:  

```haskell
con <- R.connect client
```

The next line is communicating with the server to get the buckets from
the server:

```haskell
buckets <- R.listBuckets con
```

Finally, we print the response out:  

```haskell
print buckets
```

In the next port or two I will show you how to "GET" and "POST" data
into Riak using the Network.Riak library.
