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
            list.append('<div class="github-item"><a href="'+ this.url +'"><h4>' + this.full_name + 
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