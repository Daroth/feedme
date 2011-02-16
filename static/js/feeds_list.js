$(document).ready(function() {
    $("#show_all").hide();
    $("#show_all").click(function() {
        $(".is_read").show();
        $("#show_all").hide();
        $("#show_unread").show();
        return false;
    });
    $("#show_unread").click(function() {
        $(".is_read").hide();
        $("#show_unread").hide();
        $("#show_all").show();
        return false;
    })
});

function blurButton(button) {
    button.blur();
    return false;
}
