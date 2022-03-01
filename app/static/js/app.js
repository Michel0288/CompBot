/* Add your Application JavaScript */
$(window).resize(function() {
    if ($(window).width() <= 991) {
        $("#navbarNavAltMarkup").addClass("border-bottom");
    }else{
        $("#navbarNavAltMarkup").removeClass("border-bottom");
    }
});