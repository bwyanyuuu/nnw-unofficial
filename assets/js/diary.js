$(document).ready(function() {
    // $('.diary').hide();
    setTimeout(function(){
        $('.diary-list').fadeIn(1000);
        $('.diary').show();
        $('.diary-list').css("display", "flex");
        $('.diary').css("display", "flex");
    },1000);
    setTimeout(function(){
        // $('.diary').show()
        $('.diary-content.active').fadeIn(1000);
        $('img.diary-img').show();
        // $('.diary-content').css("display", "")
    },2500);
    // $('.diary').delay(2500).css("display", "flex");
    // $('.diary').style("display:flex");
    $('.day').click(function(){
        var id = $(this).attr("id");
        if($('.diary-content.active').attr("id").substring(1, 7) != id){
            $('.diary-content.active').fadeOut(500);
            $('.diary-content.active').removeClass("active");
            $('#d' + id).addClass("active");
            $('#d' + id).delay(500).fadeIn(500);
            // $('#d' + id).find('.diary-content')
            // alert("click!");
            console.log($('.diary-content.active').attr("id").substring(1, 7) + " " + id)
        }
        
    });
    var isShow = false;
    $('img.diary-img').click(function () { 
        console.log("in");
        var hito = $(this);
        if(!isShow){
            $(".diary-imglist").removeClass("hide");
            $(".diary-imglist").addClass("show");
            $(".diary-imglist").hide();
            // hito.fadeOut(50).delay(10).fadeIn(100);
            // setTimeout(function(){
                hito.attr("src", "./images/man2.png");
                
                
                $(".diary-imglist").fadeIn(1000);
                
                isShow = true;
            // }, 60);
        }
        else{
            // hito.fadeOut(50).delay(10).fadeIn(100);
            $(".diary-imglist").removeClass("show");
            $(".diary-imglist").addClass("hide");
            $(".diary-imglist").fadeIn(1000);
            // $(".diary-imglist").fadeOut(1000);
            // setTimeout(function(){
                hito.attr("src", "./images/man.png");
                isShow = false;
            // }, 60);
            // setTimeout(function(){
                
            // }, 1060);
        }
    });
    
});