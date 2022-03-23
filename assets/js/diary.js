var mem = $('html').attr('id');
$(document).ready(function() {
    var winWide = window.screen.width;
    console.log(winWide);
    // initial diary content
    updateDiary(mem, $('.diary-list ul li:first-child').attr('id'));
    if(winWide > 768){
        $('.nav').hide();
        
        setTimeout(function(){
            
            $('.nav').fadeIn(1000);
            $('.diary-list').fadeIn(1000);
            $('.diary').show();
            $('.diary-list').css("display", "flex");
            $('.diary').css("display", "flex");
        },1000);
        setTimeout(function(){
            $('.diary-content').fadeIn(1000);
            
            $('img.diary-img').show();
        },2500);
    }
    else{
        setTimeout(function(){
            $('.bg-color').show();
            $('img.diary-img').show();
        }, 2000)
    }
    
    
    var isShow = false;
    var url = ''
    $('img.diary-img').click(function () { 
        var hito = $(this);
        if(!isShow){
            url = './images/diary/' + mem + '-1.png'
            $(".diary-imglist").addClass("show");
            hito.attr("src", url);
            isShow = true;
        }
        else{
            url = './images/diary/' + mem + '-2.png'
            $(".diary-imglist").removeClass("show");
            hito.attr("src", url);
            isShow = false;
        }
    });    
});

$(document).on('click', '.diary-list li', function(){
    var id = $(this).attr("id");
    if($('.diary-content').attr("date") != id){
        $(".diary-content").fadeOut(500);
        setTimeout(function(){
            updateDiary(mem, id);
            $(".diary-content").scrollTop(0);
            $(".diary-content").fadeIn(500); 
        }, 500);
        
    }
});

$(document).on('click', '.diary-imglist', function(){
    var th = $(this);
    th.addClass('go');
    th.css("z-index", "8")
    setTimeout(function(){
        $('.bg').fadeIn(500);
    }, 1000)
    setTimeout(function(){
        var url = th.attr('href');
        window.location.href = url;
    }, 1600)
});

function updateDiary(mem, date){
    var url = 'https://raw.githubusercontent.com/linxiii/nnw-unofficial/main/content/' + date + '-' + mem 
    var txt = httpGet(url)
    $(".diary-content").html(txt);
    $(".diary-content").attr('date', date);
    $('.slick-box-diary').slick({ 
        dots: true,
        arrows: false,
        adaptiveHeight: true,
    });
}

function httpGet(theUrl){
    let xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            return xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", theUrl, false);
    xmlhttp.send();
    
    return xmlhttp.response;
}


Breakpoints.defaults = {
    s: {
        min: 0,
        max: 767
    },
    m: {
        min: 768,
        max: 1200
    },
    l: {
        min: 1200,
        max: Infinity
    }
};

Breakpoints.get('s').on({
    enter: function(){
        $('html').addClass('s')
    },
    leave: function(){
        $('html').removeClass('s')
    }
});
Breakpoints.get('m').on({
    enter: function(){
        $('html').addClass('m')
    },
    leave: function(){
        $('html').removeClass('m')
    }
});
Breakpoints.get('s').on({
    enter: function(){
        $('html').addClass('l')
    },
    leave: function(){
        $('html').removeClass('l')
    }
});