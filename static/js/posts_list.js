function hidePost(post_id) {
    var currentButton = document.getElementById(post_id);
    var dataString = "post_id="+post_id;
    $.ajax({
        type: "POST",
        url: "/read",
        data: dataString,
        success: function() {
            $(currentButton).hide();
            var showButton = document.getElementById("show_unread");
            if (showButton.style['display']=="none") {
                $("#post"+post_id).hide();
            }
            return false;
        }
    });
    currentButton.blur();
    return false;
}
