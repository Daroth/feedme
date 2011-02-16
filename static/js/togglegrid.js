$(document).ready(function() {
    $("body").append("<div id='debug'>grid: <a href='' id='togglegrid'>"
            + gridstate() + "</a></div>");
    $("#debug").css('position', 'absolute');
    $("#debug").css('bottom', '0');
    $("#togglegrid").click(toggle_grid);
    if (!$(".container").hasClass('showgrid')) {
        $(".container").toggleClass('showgrid');
    }
});

function toggle_grid() {
    $(".container").toggleClass('showgrid');
    $("#togglegrid").text(gridstate());
    return false;
}

function gridstate() {
    if ($(".container").hasClass('showgrid')) {
        return 'off';
    } else {
        return 'on';
    };
}
