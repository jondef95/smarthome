// Submit post on submit
$('#button-push').on('submit', function(event){
    event.preventDefault();
    console.log("button pushed!")  // sanity check
    create_post();
});

// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#post-text').val())
};