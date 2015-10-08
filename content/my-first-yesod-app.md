Title: My First Yesod App
Date: 2013-02-01 05:54
Author: Bryce
Tags: Haskell, Yesod
Slug: my-first-yesod-app

First off, I just wanted to say that I hope everyone had a relaxing and
enjoyable holiday season and that you enjoyed your New Year's
celebration. Whatever you did that day or night, don't name it after me.

In my last [post](http://scrollingtext.org/first-flask-web-app"), I
showed you how to create a simple web service that responded to three
different URLs and interacted with a database using Python and the Flask
framework. Now I'm going to show you how to program the same thing in
Haskell using the Yesod framework. For those of you too “efficient” to
look them up on the previous page HERE, I'm going to repost the
requirements:

```
Using python with gevent 0.13.x and your choice of additional libraries and/or
frameworks, implement a single HTTP server with API endpoints that provide the
following functionalities:

$ curl -s 'http://127.0.0.1:8080/fib/13'
{"response": 233}

$ curl -s 'http://127.0.0.1:8080/fib/12'
{"response": 144}

$ curl -s 'http://127.0.0.1:8080/google-body'
{"response": "272cca559ffe719d20ac90adb9fc4e5716479e96"}

$ curl -d 'value=something' 'http://127.0.0.1:8080/store'
$ curl 'http://127.0.0.1:8080/store
'{"response": "something"}
```

Like the last post, I'm going to talk about the individual functions
first, then post the whole code at the end. Let's start with the first
requirement, creating a good old Fibonacci sequence:

```haskell
handleFibR :: Int -> Handler RepJson
handleFibR num = jsonToRepJson $ object ["response" .= show_fib]  
    where
        show_fib = show $ fib num
        fib :: Int -> Int
        fib 0 = 0
        fib 1 = 1
        fib n = fib (n - 1) + fib (n – 2)
```

I'm going to go ahead and describe the code from the bottom up - it's a
little weird but it's a lot easier to explain that way, trust me. The
show\_fib function is just a simple function to sum the values created
from the Fibonacci sequence. The result of that function is used as the
“value” component of a Pair type that is created with the “.=” operator
and the “response” string, and is contained within a list. The object
function takes a list of Pairs as its input and creates a
[Value](http://hackage.haskell.org/packages/archive/yesod-json/1.1.2/doc/html/Yesod-Json.html#t:Value)
type, which is described in the documentation as “A JSON value
represented as a Haskell value.” This Value is then passed as the input
into the jsonToRepJson function. All of these functions come together
beautifully so that when you point your browser to
<http://localhost:3000/fib/24>, you get this response:  

```
{"response":"46368"}
```

For my next trick, I'm going to pull a SHA1 hash out from the Google
homepage source code.

```haskell
gGoogR :: Handler RepJson
getGoogR = do
    body <- try (simpleHttp "http://www.google.com”)
    case body of
        Left (SomeException ex) -> jsonToRepJson $ object [“response” .= (“ERROR:  “ ++ (show ex))]
        Right val -> jsonToRepJson $ object [“response” .= (showDigest $ sha1 val)]
```

Much like the last function, this function will return a Handler
containing a RepJson . First I use the simpleHttp function to travel to
the interwebs and pull the Google homepage. Because simpleHttp will
throw an HttpException with any non 200 status code, I have the function
called within a try function, putting the result into “body”. Body is of
the Either type, which means it can have one of two possible values
(like Schrodinger's cat). If something went wrong, the value would be in
the “Left” side of the Either type. If that's what happened, I don't
really care what went wrong so I just return a generic error message. If
everything flowed smoothly like all code does (snicker), the data would
be on the “Right” side of Either, allowing me to pull the data out using
the Right function and named val. The code after this point is extremely
similar to the previous example, the difference being the output. The
website source code is used as input for the sha1 function, creating a
Digest type, then I carry that over to showDigest, which returns a
string 160 characters long. All of this is bubbled up to the handler and
the user sees:

```
{"response":"ddd27a244477532f7be5207582afca72b9f74224"}
```

Your results will differ! For dealing with the database, we need
functions that can handle both GET and POST requests. Before I explain
those functions, I want to take a quick moment to share the database
schema and the “runDB” function:

```haskell
share [mkPersist sqlSettings, mkMigrate "migrateAll"] [persist|
Stuff
    value Text
    deriving Show
|]

runDB action = do
    Challenge pool <- getYesod
    runSqlPool action pool
```

If you are a little confused by these two things, don't fear. I will do
my best to describe them in a moment. If that still doesn't help then
maybe viewing the entire code base below will. The first code block
above is responsible for creating the Stuff database which holds a
single column, called “value”. It reminds me of user defined datatypes
created with the “data” Haskell keyword.

The second block is really me [cargo cult
programming](http://en.wikipedia.org/wiki/Cargo_cult_programming). I've
seen this technique used in a lot of the examples of the Yesod book, so
I copied it while I was writing this project. The best way I can
describe it is as a wrapper function for using an item from a pool of
database connectors, and using some of those connectors to to run the
query.

Now that you know what the database looks like and how we access it, we
can move onto the functions that interact with it. Here is the code for
the POST request:

```haskell
postStoreR :: Handler ()
postStoreR = do
    mvalue <- runInputPost $ ireq textField "value"
    runDB $ insert $ Stuff mvalue
    sendResponseStatus status200 ()
```

This function just returns a Handler unit. Using the ireq function, we
look through the POST request for the expected input keyed as “value”.
The output of that function goes through the runInputPost, and deposits
the contents into mvalue. We take mvalue, change it to become a Stuff
type, pass that to the insert function which, when it runs, returns an
automatically created key. and then moving that along to runDB, which
inserts our data into the database. The last line returns the 200 status
back to the client, using the sendResponseStatus.

Finally, for the GET request we have:

```haskell
getStoreR :: Handler RepJson
getStoreR = do
    mvalue <- runDB $ selectFirst [] [Desc StuffValue, LimitTo 1]
    case mvalue of
        Nothing -> jsonToRepJson $ object ["response" .= (show "NO DATA IN DATABASE")]
        Just mvalue' -> jsonToRepJson $ object ["response" .= (show . stuffValue $ entityVal mvalue')]
```

The result of the selectFirst function provides the input for runDB. The
first argument for selectFirst is an empty list, this argument is for
filtering on some kind of value( greater than, less than, not equal to,
etc). I have left it blank because I really don't care what the value of
“value” is; I just want it. The second list is telling the database to
put the column values in descending order. The first line is the Haskell
equivalent of the following SQL code:

```sql
SELECT * FROM Stuff GROUP BY VALUE DESC LIMIT 1;
```

The results of which are named mvalue. Since it's possible to have
nothing in the response, I use the case statement to dig inside mvalue
and look around. If “Nothing” was returned, I send back a little json
blurb letting the user know that nothing was found, most likely because
there isn't data in the database. If something was returned, pull that
value out, and mix it all in the with json recipe you've seen me using
thus far, and then send the data on its way.

As the title says, this was my first Yesod web app. I know that I have
only scratched the surface of what this framework can do and I'm really
interested in creating more with it. I will admit that I initially found
the interaction with the database a little cumbersome when compared to
Django or Flask. That doesn't mean I don't like it, it's just a little
awkward when I was first trying to understand how to work with it. Once
I got over those differences, I realized that it mentally translates to
SQL better than the other frameworks. Again, I really like Yesod and
look forward to using it in the future.

As always, I and my code welcome questions, comments, and the occasional
funny and creative insult.

```haskell
{-# LANGUAGE TypeFamilies, QuasiQuotes, MultiParamTypeClasses, TemplateHaskell #-}
{-# LANGUAGE GADTs,OverloadedStrings,FlexibleContexts, FlexibleInstances #-}
import Yesod as Y
import Data.Text (pack, Text)
import Network.HTTP.Conduit (simpleHttp)
import Network.HTTP.Types (status200)
import Data.Digest.Pure.SHA (showDigest, sha1)
import Database.Persist.Sqlite
import Data.Maybe
import Control.Exception.Lifted hiding (Handler)
import Data.ByteString.Lazy.Internal (ByteString)

share [mkPersist sqlSettings, mkMigrate "migrateAll"] [persist|Stuff
    value Text
    deriving Show
|] 

data Challenge = Challenge ConnectionPool

mkYesod "Challenge" [parseRoutes|
/fib/#Int FibR
/google-body GoogR GET
/store StoreR POST GET
|]

instance Yesod Challenge

instance RenderMessage Challenge FormMessage where
    renderMessage _ _ = defaultFormMessage

 instance YesodPersist Challenge where
    type YesodPersistBackend Challenge = SqlPersist

    runDB action = do
        Challenge pool <- getYesod
        runSqlPool action pool 

handleFibR :: Int -> Handler RepJson
handleFibR num = jsonToRepJson $ object ["response" .= show_fib]
    where
        show_fib = show $ fib num
        fib :: Int -> Int
        fib 0 = 0
        fib 1 = 1
        fib n = fib (n - 1) + fib (n - 2)

getGoogR :: Handler RepJson
getGoogR = do
    body <- try (simpleHttp "http://www.google.com")
    case body of
        Left (SomeException ex) -> jsonToRepJson $ object ["response" .= ("ERROR: " ++ (show ex))]
        Right val -> jsonToRepJson $ object ["response" .= (showDigest $ sha1 val)]

postStoreR :: Handler ()
postStoreR = do
    mvalue <- runInputPost $ ireq textField "value"
    runDB $ Y.insert $ Stuff mvalue
    sendResponseStatus status200 ()

getStoreR :: Handler RepJson
getStoreR = do
    mvalue <- runDB $ Y.selectFirst [] [Y.Desc StuffValue, Y.LimitTo 1]
    case mvalue of
        Nothing -> jsonToRepJson $ object ["response" .= (show "NO DATA IN DATABASE")]
        Just mvalue' -> jsonToRepJson $ object ["response" .= (show . stuffValue $ Y.entityVal mvalue')]

 main = withSqlitePool ":memory:" 10 $ \pool -> do
    runSqlPool (runMigration migrateAll) pool
    warpDebug 3000 $ Challenge pool
```
