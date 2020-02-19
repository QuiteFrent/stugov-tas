$(document).ready(function () {
    $(".upvoteButton").on("click", function () {
        let id = this.dataset.post;
        jQuery.getJSON(`${id}/vote`, function (data) {
            if (data.votes != null)
                $("#votes_count").text(data.votes);
            else
                window.location.replace("/accounts/login");
            console.log(data.votes)
        })
    });
});
