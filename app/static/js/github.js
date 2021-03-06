jQuery.githubUser = function(username, callback) {
    jQuery.getJSON("https://api.github.com/users/" + username + "/repos", callback);
}

jQuery.fn.loadRepositories = function(username) {
    this.html("<span>Querying GitHub for repositories...</span>");

    var target = this; 
    $.githubUser(username, function(data) {
        console.log("HELLO")
        var repos = data;
        console.log(repos)
        sortByNumberOfWatchers(repos);

        var list = $('<div class="github-container"/>');
        target.empty().append(list);
        $(repos).each(function() {
            // console.log(this)
            list.append('<div class="github-item col-xs-12 col-md-12"><a style="text-decoration:none;" target="_blank" href="'+ this.html_url +'"><h4 class="underline">' + this.full_name + 
            '</h4></a><p>' + this.description + '</p>' + '<p class="portfolio-language">' + 
            this.language + '</p></div>');
        });
    });

    function sortByNumberOfWatchers(repos) {
        repos.sort(function(a,b) {
        return b.watchers - a.watchers;
        });
    }
};