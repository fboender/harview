HARview
=======

About
-----

HARview is a HAR (HTTP Archive) viewer. HAR is a JSON-encoded recording of HTTP
requests, responses and timings. .har Files can be exported from Chrome's
Developer Tools' "Network" tab by capturing some traffic, right-clicking in the
results pane and selecting 'Save as HAR with content'.

HARView is a commandline tool which takes as input a .har (HTTP Archive) file
and dumps a human-readable summary of it to the console. It is mostly useful
for long dumps with many requests (such as debugging SAML / OAuth / etc). These
can be captured in Chrome by enabling the "Preserve Log upon Navigation" button
in the Network analyser.

More information is available here: http://www.electricmonk.nl/log/2013/09/16/quick-n-dirty-har-http-archive-viewer/

Requirements
------------

Python.


Usage
-----

From the `--help`:

    usage: harview.py [-h] [-v] [--filter-img] [--filter-refs] [--filter-all]
                      [--nocolor]
                      har_file
    
    positional arguments:
      har_file
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Show more. Can be used multiple times
      --filter-img   Filter out requests for images
      --filter-refs  Filter out requests for CSS, JS, etc
      --filter-all   All filters
      --nocolor

Example:

    harview.py -vv --filter-all img ./login.myorg.com.har

The output of which would look something like:

    301 GET http://electricmonk.nl/
        Request headers
        Response headers (status = 301)

    200 GET http://www.electricmonk.nl/
        Request headers
            DNT: 1
            Accept-Encoding: gzip,deflate,sdch
            Host: www.electricmonk.nl
            Accept-Language: en-US,en;q=0.8,nl-NL;q=0.6,nl;q=0.4
            User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (
                        KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chro
                        me/28.0.1500.71 Safari/537.36
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/
                    *;q=0.8
            Cookie: PHPSESSID=210cd55ffbe6a18e104495ecee1e4356
            Connection: keep-alive
        Response headers (status = 200)
            Date: Mon, 16 Sep 2013 18:02:05 GMT
            Transfer-Encoding: chunked
            Server: Apache
            Connection: Keep-Alive
            Keep-Alive: timeout=15, max=100
            X-Pingback: http://www.electricmonk.nl/log/xmlrpc.php
            Content-Type: text/html; charset=UTF-8

    200 GET http://fonts.googleapis.com/css?family=Jura
        Request headers
            DNT: 1
            Accept-Encoding: gzip,deflate,sdch
            Host: fonts.googleapis.com
            Accept-Language: en-US,en;q=0.8,nl-NL;q=0.6,nl;q=0.4
            User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (
                        KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chro
                        me/28.0.1500.71 Safari/537.36
            Accept: text/css,*/*;q=0.1
            Referer: http://www.electricmonk.nl/
            Connection: keep-alive
        Response headers (status = 200)
            Date: Mon, 16 Sep 2013 18:02:05 GMT
            X-Content-Type-Options: nosniff
            Server: GSE
            X-Frame-Options: SAMEORIGIN
            Content-Type: text/css
            Alternate-Protocol: 80:quic
            Cache-Control: private, max-age=86400
            Timing-Allow-Origin: *
            Content-Length: 239
            X-XSS-Protection: 1; mode=block
            Expires: Mon, 16 Sep 2013 18:02:05 GMT


License
-------

Harview is open source, released under the MIT license. Please see the
`LICENSE` file for a full copy of the MIT license.

