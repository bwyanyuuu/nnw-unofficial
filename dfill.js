$(document).ready(function(){
    for(var i = 1; i <8; i+=1){
        var id = "nnw" + i;
        $('html').attr('id', id);
        var url = './images/mem' + i + '.png';
        for(var j = 1; j <8; j+=1){
            var cnt = 1;
            if(j != i){
                url = './images/m' + j + '.jpg'
                $('.diary-imglist')[i].attr('href', url)
                url = 'p' + j
                $('.diary-imglist')[i].addClass(url)
                cnt += 1;
            }
        }
        console.log($('html'));
    }    
})
