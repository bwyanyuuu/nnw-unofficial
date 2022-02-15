$(document).on('click', '.hamburger', function(){
    $(this).addClass('is-active');
    // $('.nav-small').show();
    $('.nav-small').addClass('is-open');
    $('.nav-small').css('opacity', '1');
});
$(document).on('click', '.hamburger.is-active', function(){
    $(this).removeClass('is-active');
    $('.nav-small').removeClass('is-open');
    setTimeout(function(){
        $('.nav-small').css('opacity', '0');
    }, 500)
    // $('.nav-small').hide();
});