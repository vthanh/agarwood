// ============================== ALERT ====================================
function ShowAlert(txt) {
    var eheight = $('.malert').height();
    var ewidth = $('.malert').width();
    var leftpx = window.innerWidth - ewidth;
    var toppx = window.innerHeight - eheight;
    // scroll top
    $("html, body").animate({ scrollTop: 0 }, 15);
    if (leftpx < 0)
        leftpx = 0;
    if (toppx < 0)
        toppx = 0;
    if (leftpx >= 0 && toppx >= 0) {
        leftpx = leftpx / 2;
        toppx = toppx / 2;
        $('.alertwrap').attr('style', 'display:block');
        $('.malert').attr('style', 'display:block;left:' + leftpx + 'px; top:' + toppx + 'px');
        $('.malert .text').html(txt);
    }
    else {
        $('.alertwrap').attr('style', 'display:block');
        $('.malert').attr('style', 'display:block');
    }
}
function CloseAlert(cls) {
    $('.alertwrap').attr('style', 'display:none');
    $('.malert').attr('style', 'display:none');
}
function GoAlert(url){
    $('.malert .btn a').attr("onclick","location.href = '"+url+"'");
}
function TitleAlert(txt){
    $('.malert .ptitle h2').html(txt);
}
function DefaultAlert(){
    $('.malert .ptitle').attr('style','background:#a01818;');
    $('.malert .ptitle h2').attr('style','background:#a01818;');
    $('.malert .con .text').attr('style','color:red;');
}
function GreenAlert(){
    $('.malert .ptitle').attr('style','background:#1fa145;');
    $('.malert .ptitle h2').attr('style','background:#1fa145;');
    $('.malert .con .text').attr('style','color:#1fa145;');
}
function ConfirmAlert(fun){
    $('.malert .btn #aok').attr('onclick',fun);
    $('.malert .btn #acancel').show();
}
function BtnOkAlert(fun){
    $('.malert .btn #aok').attr('onclick',fun);
}
function BtnOkOnlyAlert(fun){
    $('.malert .btn #acancel').hide();
    $('.malert .btn #aok').html('OK')
    $('.malert .btn #aok').attr('onclick',fun);
}
function BtnOkText(str){
    $('.malert .btn #aok').text(str);
}
function BtnCancelText(str){
    $('.malert .btn #acancel').text(str);
}
function BtnCancelAlert(fun){
    $('.malert .btn #acancel').attr('onclick',fun);
}
function MinHeightAlert(txt){
    $('.malert .conwrapp').attr('style','min-height:'+txt+'px;');
}
function BtnOkOnlyClose(){
    $('.malert .btn #acancel').hide();
    $('.malert .btn #aok').text('OK');
    $('.malert .btn #aok').show();
    $('.malert .btn #aok').attr('onclick','CloseAlert()');
}