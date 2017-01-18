# Docker_ebooks

This is a Docker wrapper around the [Python port](https://github.com/tommeagher/heroku_ebooks) of [@harrisj's](https://twitter.com/harrisj) [iron_ebooks](https://github.com/harrisj/iron_ebooks/) Ruby script. Using docker and chrod, you can post to an _ebooks Twitter account based on the corpus of an existing Twitter at pseudorandom intervals. Currently, it is the magic behind [@adriennelaf_ebx](http://www.twitter.com/adriennelaf_ebx) and [@stevebuttry_ebx](http://www.twitter.com/stevebuttry_ebx).

## Setup

In order to run this, you simply have to supply a couple of variable to to docker. Simply do a `docker run` like this:

```bash
docker run -e CONSUMER_KEY="<your twitter consumer key>" \
    -e CONSUMER_SECRET="<your twitter consumer secret>" \
    -e ACCESS_TOKEN_KEY="<your twitter access token>" \
    -e ACCESS_TOKEN_SECRET="<your twitter access token secret>" \
    -e SOURCE_ACCOUNTS="<your real twitter @ handle>" \
    -e TWEET_ACCOUNT="<your _ebooks twitter @ handle>" \
    -e FREQUENCY="<how frequently to run the script>" # see below \
    -e ODDS="1"  # see below \
    -e ORDER="2" # see below \
    -it \
  emptyflash/docker_ebooks
```


## Configuring

There are several parameters that control the behavior of the bot. You can adjust them by setting them in your `local_settings.py` file. 

```
-e FREQUENCY="daily"
```

This is how frequently the script to generate a status will be run. Can be one of 5 values: 
* 15min
* daily
* hourly
* monthly
* weekly

```
-e ODDS=8
```

The bot does not run on every invocation. It runs in a pseudorandom fashion. At the beginning of each time the script fires, `guess = random.choice(range(ODDS))`. If `guess == 0`, then it proceeds. If your `ODDS = 8`, it should run one out of every 8 times, more or less. You can override it to make it more or less frequent. To make it run every time, you can set it to 0.


By default, the bot ignores any tweets with URLs in them because those might just be headlines for articles and not text you've written.

```
- e ORDER=2
```

The ORDER variable represents the Markov index, which is a measure of associativity in the generated Markov chains. 2 is generally more incoherent and 3 or 4 is more lucid. I tend to stick with 2.

## Debugging

If you want to test the script or to debug the tweet generation, you can skip the random number generation and not publish the resulting tweets to Twitter.

First, adjust the `DEBUG` variable in `local_settings.py`.

```
-e DEBUG=True 
```

If you want to avoid hitting the Twitter API and instead want to use a static text file, you can do that. First, create a text file containing a Python list of quote-wrapped tweets. Then set the `STATIC_TEST` variable to `True`. Finally, specify the name of text file using the `TEST_SOURCE` variable.


## Credit
As I said, this is just a docker wrapper around [heroku_ebooks](https://github.com/tommeagher/heroku_ebooks) (I didn't really change much), which is based almost entirely on [@harrisj's](https://twitter.com/harrisj) [iron_ebooks](https://github.com/harrisj/iron_ebooks/). 
