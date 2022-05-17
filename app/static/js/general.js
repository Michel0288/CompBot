$('#first').on("click", ()=>{
    $('#message-to-send').prop("disabled", true);
    // GENERAL
    if($('#general.tab-pane').hasClass('active')){
        $('#message-to-send').prop("disabled", false);
        alert("general");
    }
});