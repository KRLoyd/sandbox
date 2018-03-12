document.addEventListener("DOMContentLoaded", function(event) {
    let twitterUrl = "https://api.twitter.com/1.1/search/tweets.json?q=%23joke";
    // Need CORS proxy to request data
    // API does not have header "Access-Control-Allow-Origin"
    let corsProxyUrl = "https://cors-anywhere.herokuapp.com/";
    let tweetRequestUrl = corsProxyUrl + twitterUrl;

    let tweetRequest = new XMLHttpRequest();

    tweetRequest.onreadystatechange = function () {
	if (this.readyState == 4 && this.status == 200) {
	    let twitterResponse = JSON.parse(this.responseText);
	    console.log("twitterResponse: ", twitterResponse);
	    oembedTweets(twitterResponse);
	}
    }

    tweetRequest.open("GET", tweetRequestUrl, true);
    tweetRequest.setRequestHeader("Authorization", "Bearer AAAAAAAAAAAAAAAAAAAAAMdZ4wAAAAAAQ7MgKBZzoSM94%2F%2B8GdOp8fR9qOA%3DRsvVtzjFcfmAhx6iOIV0Jt54PFCzFoXE8gSsI5H89WJyotaqpO");
    tweetRequest.send();

    oembedTweets = function(response) {
	let allTweetInfo = makeUrlList(response);
	allTweetInfo.forEach(function (tweet) {
	    renderOembedHtml(tweet);
	})
    }

    makeUrlList = function(response) {
	let tweetList = response['statuses'];
	let tweetInfo = []
	tweetList.forEach(function (tweet) {
	    let singleTweet = []
	    let tweetId = tweet['id_str'];
	    let tweetScreenName = tweet['user']['screen_name'];
	    singleTweet.push(tweetId);
	    singleTweet.push(tweetScreenName);
	    tweetInfo.push(singleTweet);
	});
	return tweetInfo;
    }

    renderOembedHtml = function(aTweet) {
	// use OEmbed to get the HTML to embed tweets
	let oembedUrl = "https://publish.twitter.com/oembed?url=https://twitter.com/" + aTweet[1] + "/status/" + aTweet[0];
	// Need CORS proxy to request data
	// API does not have header "Access-Control-Allow-Origin"
	let oembedRequestUrl = corsProxyUrl + oembedUrl;

	let oembedRequest = new XMLHttpRequest();

	oembedRequest.onreadystatechange = function () {
	    if (this.readyState == 4 && this.status == 200) {
		let oembedResponse = JSON.parse(this.responseText);
		let tweetHtml = oembedResponse['html'];
		let newTweet = document.createElement('div');
		newTweet.innerHTML = tweetHtml;
		console.log("newTweet: ", newTweet);
		document.getElementById('tweets').appendChild(newTweet);
	    }
	}

	oembedRequest.open("GET", oembedRequestUrl, true);
	oembedRequest.setRequestHeader("Authorization", "Bearer AAAAAAAAAAAAAAAAAAAAAMdZ4wAAAAAAQ7MgKBZzoSM94%2F%2B8GdOp8fR9qOA%3DRsvVtzjFcfmAhx6iOIV0Jt54PFCzFoXE8gSsI5H89WJyotaqpO");
	oembedRequest.send();
    }

});
